# config/models.py
from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    app_name: str = Field(..., description="Name of the application")
    debug: bool = Field(default=False, description="Debug mode")
    version: str = Field(..., description="Application version")


# config/loader.py
import yaml
from .models import AppConfig


def load_config(file_path: str) -> AppConfig:
    with open(file_path, "r") as file:
        config_data = yaml.safe_load(file)
    return AppConfig(**config_data)
