import json

data = {
    "employee": {
        "name": "Ravi",
        "details": {
            "department": "IT",
            "salary": 50000
        }
    }
}

with open("employee.json", "w") as file:
    json.dump(data, file, indent=4)


data["employee"]["details"]["salary"] = 55000

with open("employee.json", "w") as file:
    json.dump(data, file, indent=4)
