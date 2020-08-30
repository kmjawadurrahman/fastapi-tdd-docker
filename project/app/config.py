import logging
import os
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger(__name__)


class Settings(BaseSettings):
    # defines the environment (i.e. dev, stage, prod)
    environment: str = os.getenv("ENVIRONMENT", "dev")
    # defines whether or not we are in testing mode
    testing: bool = os.getenv("TESTING", 0)


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
