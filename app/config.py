import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent


def load_runtime_env() -> None:
    env_name = (os.getenv("APP_ENV") or "local").strip().lower()

    env_file_map = {
        "local": ROOT_DIR / ".env.local",
        "development": ROOT_DIR / ".env.local",
        "docker": ROOT_DIR / ".env.docker",
        "test": ROOT_DIR / ".env.test",
        "production": ROOT_DIR / ".env.production",
    }

    env_file = env_file_map.get(env_name, ROOT_DIR / ".env.local")

    if env_file.exists():
        load_dotenv(env_file, override=True)


load_runtime_env()


def get_database_url() -> str:
    value = os.getenv("DATABASE_URL")
    if value:
        return value
    return "sqlite:///./app.db"


def get_api_key() -> str:
    return os.getenv("API_KEY", "my-secret-api-key")

def get_slack_bot_token() -> str:
    return os.getenv("SLACK_BOT_TOKEN", "")


def get_slack_signing_secret() -> str:
    return os.getenv("SLACK_SIGNING_SECRET", "")


def get_slack_manager_channel_id() -> str:
    return os.getenv("SLACK_MANAGER_CHANNEL_ID", "")


def get_slack_user_channel_id() -> str:
    return os.getenv("SLACK_USER_CHANNEL_ID", "")
