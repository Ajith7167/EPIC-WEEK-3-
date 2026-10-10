import re
from exceptions.employee_exceptions import (InvalidEmployeeIDError,InvalidEmailError,InvalidAgeError,InvalidSalaryError)

def validate_employee_id(employee_id):
    if not employee_id.strip():
        raise InvalidEmployeeIDError("Employee ID cannot be empty.")

def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty.")

def validate_age(age):
    if age < 18 or age > 65:
        raise InvalidAgeError("Age must be between 18 and 65.")

def validate_email(email):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.fullmatch(pattern,email):
        raise InvalidEmailError("Invalid email format.")

def validate_salary(salary):
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")

def validate_department(department):
    if not department.strip():
        raise ValueError("Department cannot be empty.") 