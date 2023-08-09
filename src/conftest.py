import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError


@pytest.fixture(scope="session")
def client():
    from just_listened_core.external_interfaces.just_listened_api.main import app

    return TestClient(app)


def drop_all(engine):
    from just_listened_core.database import JustListenedCoreBaseModel as Base

    with engine.begin() as conn:
        conn.exec_driver_sql("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
    Base.metadata.drop_all(bind=engine)


def _run_alembic_upgrade():
    config = Config("alembic.ini")
    command.upgrade(config, "head")


@pytest.fixture(scope="session")
def db_engine():
    from just_listened_core.database import get_engine

    engine = get_engine()
    try:
        engine.connect()
    except OperationalError as err:
        if "Connection refused" in str(err):
            suggestion = "Is your db up and running?\nsuggestion: docker-compose up -d"
        elif "does not exist" in str(err):
            suggestion = (
                "Did you create a local test database?\n"
                "suggestion: docker-compose exec db createdb -U test -0 test testd"
            )
        else:
            raise err

        raise AssertionError(suggestion) from err

    drop_all(engine)

    _run_alembic_upgrade()
    yield engine

    drop_all(engine)
    engine.dispose()


@pytest.fixture
def db_session(db_engine):
    from just_listened_core.database import SessionLocal

    with SessionLocal(bind=db_engine) as db:
        _run_alembic_upgrade()
        yield db
        db.rollback()
        drop_all(db_engine)


@pytest.fixture(autouse=True)
def self_destructible_db(db_engine):
    """
    Ensure db is in a clean state before and after the test.
    """
    drop_all(engine=db_engine)
    _run_alembic_upgrade()

    yield

    drop_all(engine=db_engine)
    _run_alembic_upgrade()
