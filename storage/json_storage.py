import json
from pathlib import Path

Data_file=(Path(__file__).resolve().parent.parent / "data" / "employees.json")
def load_employees():
    Data_file.parent.mkdir(parents=True, exist_ok=True)
    if not Data_file.exists():
        save_employees([])
        return []
    with open(Data_file, 'r',encoding='utf-8') as file:
        return json.load(file)
    

def save_employees(employees):                                                                                                                                                                                                                                                                                  
    Data_file.parent.mkdir(parents=True, exist_ok=True)
    with open(Data_file, 'w',encoding='utf-8') as file:
        json.dump(employees, file, indent=4)
print("Employee data saved to:",Data_file.resolve())