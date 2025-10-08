import json

with open("student.json", "r") as file:
    student_data = json.load(file)

with open("extra.json", "r") as file:
    extra_data = json.load(file)


merged_data = {**student_data, **extra_data}

with open("merged.json", "w") as file:
    json.dump(merged_data, file, indent=4)
