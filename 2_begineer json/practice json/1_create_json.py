import json
student = {
    "name": "Amit",
    "age": 21,
    "courses": ["Math", "Physics", "Computer Science"]
}

with open("student.json", "w") as f:
    json.dump(student, f, indent=4)


print("✅ Data written to data.json file successfully!")