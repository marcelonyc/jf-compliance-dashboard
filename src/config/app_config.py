import yaml
import os
import configparser
from configparser import ConfigParser
import logging
from functools import lru_cache


class AppConfig:

    def __init__(self) -> None:
        os.environ["APP_ROOT"] = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../"
        )
        self.APP_ROOT = os.getenv("APP_ROOT")

        self.APP_CONFIG_FILE = os.getenv("APP_CONFIG_FILE")

        os_env = False
        if self.APP_CONFIG_FILE is None or self.APP_CONFIG_FILE == "":
            os_env = True

        if not os_env:
            config = configparser.ConfigParser()
            config.sections()
            config.read(self.APP_CONFIG_FILE)

            # Handle configs with secrets
            # look for the syntax ${vault:secret_name} and replace with the secret
            self.db_url = config.get(
                "appcfg",
                "db_url",
            )

            # Logging
            self.log_level = config.get("appcfg", "log_level").upper()
            _log_level = {
                "DEBUG": logging.DEBUG,
                "INFO": logging.INFO,
                "WARN": logging.WARN,
                "ERROR": logging.ERROR,
            }
            logging.getLogger().setLevel(
                _log_level.get(self.log_level, logging.INFO)
            )

            self.JF_URL = config.get("jfrog", "jf_url")
            self.JF_TOKEN = config.get("jfrog", "jf_token")
        else:
            self.db_url = f"{os.getenv('DB_DRIVER')}://{os.getenv('JFROG_USER')}:{os.getenv('JFROG_PASSWORD')}@{os.getenv('JFROG_DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('JFROG_DB')}"

            # Logging
            self.log_level = os.getenv("LOG_LEVEL").upper()
            _log_level = {
                "DEBUG": logging.DEBUG,
                "INFO": logging.INFO,
                "WARN": logging.WARN,
                "ERROR": logging.ERROR,
            }
            logging.getLogger().setLevel(
                _log_level.get(self.log_level, logging.INFO)
            )

            self.JF_URL = os.getenv("JF_URL")
            self.JF_TOKEN = os.getenv("JF_TOKEN")
            self.JFROG_UPDATE_SHORT_INTERVAL = int(
                os.getenv("JFROG_UPDATE_SHORT_INTERVAL")
            )
            self.JFROG_UPDATE_LONG_INTERVAL = int(
                os.getenv("JFROG_UPDATE_LONG_INTERVAL")
            )
            self.REDIS_HOST = os.getenv("REDIS_HOST", "jfrog_redis")


@lru_cache
def get_settings() -> AppConfig:
    return AppConfig()
