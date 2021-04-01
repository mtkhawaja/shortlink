from decouple import config


PROJECT_NAME = config("PROJECT_NAME", default="Shortlink")
API_V1_STR = "/api/v1"
HOST_NAME = config("HOST_NAME", default="0.0.0.0")
HOST_PORT = config("HOST_PORT", default=8888)
DEBUG = config("DEBUG", default=True, cast=bool)
SQLALCHEMY_DATABASE_URI = config("DATABASE_URL")
NOT_FOUND_REDIRECT = config(
    "NOT_FOUND_REDIRECT", default="http://localhost:8000/pages/404"
)
