
import json

from employee_management.config.settings import DATA_FILE, logger


def load_employees():
    try:
        if not DATA_FILE.exists():
            DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
            DATA_FILE.write_text("[]", encoding="utf-8")

        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Employee JSON data must be a list.")

        return data

    except json.JSONDecodeError:
        logger.exception("Employee JSON file contains invalid JSON")
        raise

    except Exception:
        logger.exception("Failed to load employee data")
        raise


def save_employees(employees):
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)

        logger.info("Employee data saved successfully")

    except Exception:
        logger.exception("Failed to save employee data")
        raise
