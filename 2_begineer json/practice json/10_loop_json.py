import json

data = {
    "students": [
        {"name": "Amit", "age": 22},
        {"name": "Riya", "age": 21},
        {"name": "Ravi", "age": 25}
    ]
}

with open("student.json", "w") as file:
    for index in data["students"]:
        index["age"] +=1
    json.dump(data, file, indent=4)
