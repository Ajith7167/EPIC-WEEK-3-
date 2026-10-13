import logging

logger = logging.getLogger(__name__)

def create_employee(self, employee):
    # Keep your existing validation and save logic here.

    # Log only after the employee has been saved successfully.
    logger.info(
        "Employee created successfully: %s",
        employee.employee_id
    )

    # After a successful update
logger.info("Employee updated successfully: %s", employee_id)

# After a successful deletion
logger.info("Employee deleted successfully: %s", employee_id)

# After a successful search
logger.info("Employee searched successfully: %s", employee_id)

# When validation fails
logger.warning("Employee validation failed")

# When an unexpected operation error occurs
logger.exception("Unexpected error during employee operation")