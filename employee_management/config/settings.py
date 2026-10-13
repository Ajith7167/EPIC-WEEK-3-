import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load environment variables from the project root
load_dotenv(BASE_DIR / ".env")


APP_NAME = os.getenv(
    "APP_NAME",
    "Employee Management System"
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
).upper()

LOG_FILE = BASE_DIR / os.getenv(
    "LOG_FILE",
    "logs/application.log"
)

DATA_FILE = BASE_DIR / os.getenv(
    "DATA_FILE",
    "data/employees.json"
)

# Ensure required directories exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)