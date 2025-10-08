import json

with open("student.json", "r") as f:
    data = json.load(f)

print(f"Student name is: {data['name']} and age is: {data['age']} and Cources is {data['courses']}")
print("Type", type(data))