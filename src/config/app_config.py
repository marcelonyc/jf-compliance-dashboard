import yaml
import os
import configparser
from configparser import ConfigParser
import logging
from functools import lru_cache


class AppConfig:

    def __init__(self) -> None:
        # Set Root before importing project modules
        os.environ["DASH_APP_ROOT"] = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../../"
        )
        os.environ["APP_ROOT"] = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../"
        )

        # self.run_mode = os.getenv("RUN_MODE")
        # if not self.run_mode:
        #     raise ValueError("RUN_MODE not set. It is required")

        self.APP_ROOT = os.getenv("APP_ROOT")
        self.DASH_APP_ROOT = os.getenv("DASH_APP_ROOT")

        self.APP_CONFIG_FILE = os.getenv("APP_CONFIG_FILE")

        if self.APP_CONFIG_FILE is None or self.APP_CONFIG_FILE == "":
            self.APP_CONFIG_FILE = os.path.join(self.APP_ROOT, "config.ini")

        print(f"APP_CONFIG_FILE: {self.APP_CONFIG_FILE}")
        config = configparser.ConfigParser()
        config.sections()
        config.read(self.APP_CONFIG_FILE)
        self.APP_TITLE = config.get("appcfg", "title")

        # Handle configs with secrets
        # look for the syntax ${vault:secret_name} and replace with the secret
        self.db_url = config.get("appcfg", "db_url")

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


@lru_cache
def get_settings() -> AppConfig:
    return AppConfig()
