from decouple import config

PROJECT_NAME = config("PROJECT_NAME", default="shortlink")

SQLALCHEMY_DATABASE_URI = config("DATABASE_URL")

API_V1_STR = "/api/v1"
