api-up:
	@echo "Running api on port 8005"
	@uvicorn src.just_listened_core.external_interfaces.just_listened_api.main:app --reload --host 0.0.0.0 --port 8005

clean:
	@echo "Running black and isort"
	@black . && isort .

lint:
	@echo "Running flake8"
	@flake8 --isort-show-traceback

before-commit: clean lint