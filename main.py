import argparse
from dotenv import load_dotenv
from settings import Settings
from pathlib import Path


def export_envs(environment: str = "dev") -> None:
    if environment == "dev":
        load_dotenv(dotenv_path=Path("env.dev"))
    elif environment == "prod":
        load_dotenv(dotenv_path=Path("env.prod"))
    elif environment == "test":
        load_dotenv(dotenv_path=Path("env.test"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
