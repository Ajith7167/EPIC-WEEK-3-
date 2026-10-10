class Employee:
    def __init__(self,employee_id, name, age, email,department, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'department': self.department,
            'salary': self.salary
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['employee_id'],
            data['name'],
            data['age'],
            data['email'],
            data['department'],
            data['salary'])
    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Department:", self.department)
        print("Salary:", self.salary)   