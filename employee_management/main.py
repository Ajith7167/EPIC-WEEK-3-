import logging

from employee_management.config.logging_config import (
    setup_logging,
)

logger = logging.getLogger(__name__)


def main():
    setup_logging()

    logger.info("Application started")

    try:
        # Call your existing Employee Management System here.
        # Example:
        # employee_service.create_employee(employee)

        logger.info("Application operations completed")

    except Exception:
        logger.exception("Unexpected error in application")
        raise

    finally:
        logger.info("Application stopped")


if __name__ == "__main__":
    main()