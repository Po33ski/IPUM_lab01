from pydantic_settings import BaseSettings
from pydantic import field_validator, ValidationError


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    SECRET_API_KEY: str

    @field_validator("ENVIRONMENT")
    def validate_environment(value):
        env_values = ["dev", "test", "prod"]
        if value in env_values:
            return value
        else:
            raise ValidationError
