import json
employee = {
    "name": "Riya",
    "department": "HR",
    "skills": ["Communication", "Recruitment", "Management"]
}

json_str = json.dumps(employee)
print(json_str)
print("Type", type(json_str))