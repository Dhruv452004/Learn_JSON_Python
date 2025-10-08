import json

with open("student.json", "r") as file:
    data = json.load(file)
print(data)


#  student.json se data ko pretty.json mein transfer kra aur shi format mein usme add kra

with open("pretty_student.json", "w") as file:
    json.dump(data, file, indent=4)
print(data)