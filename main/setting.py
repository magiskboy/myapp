import os
from starlette.config import Config

__all__ = ["get_setting"]

_config = Config()

def _get_key(name, cast, default):
    global _config
    return _config(f"MYAPP_{name}", cast, default)


class BaseSetting:
    ROOTDIR = os.getcwd()

    ENV = "production"

    DATABASE_URI = _get_key("DATABASE_URI", str, "sqlite:///:memory:")

    DEBUG = _get_key("DEBUG", bool, False)

class DevelopmentSetting(BaseSetting):
    DEBUG = True

    ENV = "development"

class TestingSetting(BaseSetting):
    ENV = "testing"

    DEBUG = True

    DATABASE_URI = "sqlite:///:memory"

class ProductionSetting(BaseSetting):
    pass

def get_setting(setting_name: str) -> BaseSetting:
    return dict(
        development=DevelopmentSetting(),
        testing=TestingSetting(),
        production=ProductionSetting(),
    ).get(setting_name)