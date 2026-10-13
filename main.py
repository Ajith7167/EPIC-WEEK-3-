
import logging

from employee_management.models.employee import Employee
from employee_management.services.employee_service import EmployeeService
from employee_management.config.settings import (
    APP_NAME,
    logger,
)
from employee_management.exceptions.employee_exceptions import (
    InvalidEmployeeIDError,
    InvalidAgeError,
    InvalidEmailError,
    InvalidSalaryError,
    EmployeeNotFoundError,
    DuplicateEmployeeError,
)


def main():
    logger.info("%s started", APP_NAME)
    service = EmployeeService()

    try:
        employees = [
            Employee(
                "EMP0011", "John Doe", 30,
                "john.doe@example.com", "HR", 50000
            ),
            Employee(
                "EMP0012", "Varun Smith", 31,
                "varun.smith@example.com", "IT", 60000
            ),
            Employee(
                "EMP0013", "Rahul Sharma", 28,
                "rahul.sharma@example.com", "Finance", 45000
            ),
            Employee(
                "EMP0014", "Priya Reddy", 26,
                "priya.reddy@example.com", "Marketing", 40000
            ),
            Employee(
                "EMP0015", "Sneha Kumar", 29,
                "sneha.kumar@example.com", "IT", 55000
            ),
        ]

        # Add employees only if they do not already exist.
        for employee in employees:
            try:
                service.add_employee(employee)
            except DuplicateEmployeeError:
                logger.info(
                    "Skipping existing employee: %s",
                    employee.employee_id,
                )

        print("\nAll employees:")
        service.view_employee()

        # Search
        print("\nSearching employee EMP0012:")
        employee = service.search_employee("EMP0012")
        employee.display_info()

        # Update: pass the Employee object as expected by the service.
        print("\nUpdating employee:")
        updated_employee = Employee(
            "EMP0012",
            "Ajith Smith",
            31,
            "ajith.smith@example.com",
            "IT",
            65000,
        )
        service.update_employee(updated_employee)

        print("\nEmployees after update:")
        service.view_employee()

        # Delete an existing sample employee.
        print("\nDeleting employee EMP0015:")
        service.delete_employee("EMP0015")

        print("\nEmployees after deletion:")
        service.view_employee()

    except (
        InvalidEmployeeIDError,
        InvalidAgeError,
        InvalidEmailError,
        InvalidSalaryError,
        EmployeeNotFoundError,
        DuplicateEmployeeError,
        ValueError,
    ) as error:
        logger.error("Application operation failed: %s", error)
        print("Error:", error)

    except Exception:
        logger.exception("Unexpected application error")
        print("An unexpected error occurred. Check the application log.")

    finally:
        logger.info("%s stopped", APP_NAME)


if __name__ == "__main__":
    main()
