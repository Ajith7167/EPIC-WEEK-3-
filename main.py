from models.employee import Employee
from services.employee_service import EmployeeService
from exceptions.employee_exceptions import (
    InvalidEmployeeIDError,
    InvalidAgeError,
    InvalidEmailError,
    InvalidSalaryError,
    EmployeeNotFoundError,
    DuplicateEmployeeError
)


def main():
    service = EmployeeService()

    try:
        employees = [
            Employee("EMP0011", "John Doe", 30, "john.doe@example.com", "HR", 50000),
            Employee("EMP0012", "Varun Smith", 31, "varun.smith@example.com", "IT", 60000),
            Employee("EMP0013", "Rahul Sharma", 28, "rahul.sharma@example.com", "Finance", 45000),
            Employee("EMP0014", "Priya Reddy", 26, "priya.reddy@example.com", "Marketing", 40000),
            Employee("EMP0015", "Sneha Kumar", 29, "sneha.kumar@example.com", "IT", 55000)
        ]

        for employee in employees:
            service.add_employee(employee)

        # View Employees
        print("\nViewing all employees:")
        service.view_employee()

        # Update Employee
        print("\nUpdating employee:")

        update_employee = Employee(
            "EMP0012",
            "Ajith Smith",
            31,
            "john.smith@example.com",
            "IT",
            60000
        )

        service.update_employee(update_employee)

        # View Employees After Update
        print("\nViewing all employees after update:")
        service.view_employee()

        # Delete Employee
        print("\nDeleting employee:")
        service.delete_employee("EMP013")

        # View Employees After Deletion
        print("\nViewing all employees after deletion:")
        service.view_employee()

    except (
        InvalidEmployeeIDError,
        InvalidAgeError,
        InvalidEmailError,
        InvalidSalaryError,
        EmployeeNotFoundError,
        DuplicateEmployeeError,
        ValueError
    ) as error:
        print("Error:", str(error))


if __name__ == "__main__":
    main()


