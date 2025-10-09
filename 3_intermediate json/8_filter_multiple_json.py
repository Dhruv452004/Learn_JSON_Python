import json

with open(r"C:\Users\dhruv\Desktop\json\3_intermediate json\jsonfile\multiple_students.json", "r") as file:
    data = json.load(file)


found = False #check if any student >80 found
for student in data["students"]:
    if student["Marks"] > 80:
        print(f"{student['Name']} scored {student['Marks']} marks")
        found = True
if not found:
    print("No student scored above 80 marks.")