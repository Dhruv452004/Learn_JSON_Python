import json

data = {
    "students": [
        {"name": "Amit", "marks": 85},
        {"name": "Riya", "marks": 72},
        {"name": "Ravi", "marks": 90},
        {"name": "Priya", "marks": 67}
    ]
}

with open(r"C:\Users\dhruv\Desktop\json\intermediate json\jsonfile\student.json", "w") as file:
    json.dump(data, file, indent=4)


# Print the name of the student with marks above 80

with open(r"C:\Users\dhruv\Desktop\json\intermediate json\jsonfile\student.json", "r") as file:
    student_data = json.load(file)

for student in student_data["students"]:
    if student["marks"] > 80:
        print(f"the name of the student with marks above 80 is: {student['name']} and marks is: {student['marks']}")