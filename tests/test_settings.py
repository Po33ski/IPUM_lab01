import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from settings import Settings


def test_settings_are_loaded_correctly():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "TestApp"
    assert settings.SECRET_API_KEY == "fake-test-api-key"
