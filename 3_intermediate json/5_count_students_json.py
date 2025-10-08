import json

with open(r"C:\Users\dhruv\Desktop\json\intermediate json\jsonfile\student.json", "r") as file:
    data = json.load(file)

print(data)

total_student = len(data["students"])

print(f"Total number of students: {total_student}")

print("Here are thier names:")

for student in data["students"]:
    print(student["name"])