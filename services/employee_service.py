from models.employee import Employee
from storage.json_storage import load_employees, save_employees
from exceptions.employee_exceptions import DuplicateEmployeeError
from utils.validators import (
    validate_employee_id,
    validate_name,
    validate_email,
    validate_salary,
    validate_department
)

from exceptions.employee_exceptions import (
    EmployeeNotFoundError,
    DuplicateEmployeeError)

class EmployeeService:
    def __init__(self):
        self.employees=[Employee.from_dict(data)
                        for data in load_employees()]

    def save(self):
        save_employees([employee.to_dict() for employee in self.employees])

    def validate_employee(self, employee):
        validate_employee_id(employee.employee_id)
        validate_name(employee.name)
        validate_email(employee.email)
        validate_salary(employee.salary)
        validate_department(employee.department)

    def add_employee(self, employee):
        self.validate_employee(employee)
        for existing in self.employees:
            if existing.employee_id == employee.employee_id:
                raise DuplicateEmployeeError("Employee with ID already exists.")
        self.employees.append(employee)
        self.save()
        print("employee added successfully.")

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
                return employee
        raise EmployeeNotFoundError(f"Employee with ID {employee_id} not found.")
    def update_employee(self,employee_id):
        employee=self.search_employee(employee_id)
        print("Enter new details for the employee (leave blank to keep current value):")
        name=input("Name:").strip()
        age=input("Age:").strip()
        email=input("Email:").strip()
        department=input("Department:").strip()
        salary=float(input("Salary:").strip()) 

        updated_employee=Employee(
            employee_id,name,age,email,department,salary)

        self.validate_employee(updated_employee)

        index=self.employees.index(employee)
        self.employees[index]=updated_employee
        self.save()
        print("Employee updated successfully.") 
    def delete_employee(self,employee_id):
        employee=self.search_employee(employee_id)
        self.employees.remove(employee)
        self.save()
        print("Employee deleted successfully.")