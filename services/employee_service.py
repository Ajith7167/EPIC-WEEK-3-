
import logging

from employee_management.models.employee import Employee
from employee_management.storage.json_storage import (
    load_employees,
    save_employees,
)
from employee_management.config.settings import logger
from employee_management.utils.validators import (
    validate_employee_id,
    validate_name,
    validate_email,
    validate_salary,
    validate_department,
)
from employee_management.exceptions.employee_exceptions import (
    DuplicateEmployeeError,
    EmployeeNotFoundError,
)


class EmployeeService:

    def __init__(self):
        self.employees = [
            Employee.from_dict(data)
            for data in load_employees()
        ]
        logger.info("Employee service initialized")

    def save(self):
        save_employees([
            employee.to_dict()
            for employee in self.employees
        ])

    def validate_employee(self, employee):
        try:
            validate_employee_id(employee.employee_id)
            validate_name(employee.name)
            validate_email(employee.email)
            validate_salary(employee.salary)
            validate_department(employee.department)
        except Exception:
            logger.warning("Employee validation failed")
            raise

    def add_employee(self, employee):
        try:
            self.validate_employee(employee)

            for existing in self.employees:
                if existing.employee_id == employee.employee_id:
                    raise DuplicateEmployeeError(
                        "Employee with ID already exists."
                    )

            self.employees.append(employee)
            self.save()

            logger.info("Employee created: %s", employee.employee_id)
            print("Employee added successfully.")

        except Exception:
            logger.exception("Failed to add employee")
            raise

    def view_employee(self):
        if not self.employees:
            print("No employees found.")
            return

        for employee in self.employees:
            employee.display_info()
            print("-" * 20)

    def search_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                logger.info("Employee searched: %s", employee_id)
                return employee

        logger.warning("Employee not found: %s", employee_id)
        raise EmployeeNotFoundError(
            f"Employee with ID {employee_id} not found."
        )

    def update_employee(self, updated_employee):
        try:
            self.validate_employee(updated_employee)

            existing_employee = self.search_employee(
                updated_employee.employee_id
            )

            index = self.employees.index(existing_employee)
            self.employees[index] = updated_employee

            self.save()

            logger.info(
                "Employee updated: %s",
                updated_employee.employee_id,
            )
            print("Employee updated successfully.")

        except Exception:
            logger.exception("Failed to update employee")
            raise

    def delete_employee(self, employee_id):
        try:
            employee = self.search_employee(employee_id)
            self.employees.remove(employee)
            self.save()

            logger.info("Employee deleted: %s", employee_id)
            print("Employee deleted successfully.")

        except Exception:
            logger.exception("Failed to delete employee")
            raise
