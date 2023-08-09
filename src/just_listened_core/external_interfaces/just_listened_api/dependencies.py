from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


def app_factory(title: str = "FastAPI"):
    allow_origins = ["*"]

    init_config = dict(
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=allow_origins,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=[
                    "Origin",
                    "X-Origin",
                    "Access-Control-Request-Method",
                    "Access-Control-Request-Headers",
                    "X-Access-Control-Request-Method",
                    "X-Access-Control-Request-Headers",
                    "Authorization",
                ],
                expose_headers=[
                    "Origin",
                    "X-Origin",
                    "Access-Control-Request-Method",
                    "Access-Control-Request-Headers",
                    "X-Access-Control-Request-Method",
                    "X-Access-Control-Request-Headers",
                    "Authorization",
                ],
            )
        ]
    )

    app = FastAPI(**init_config, title=title)
    return app
