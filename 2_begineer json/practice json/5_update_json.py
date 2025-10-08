import json

with open("student.json", "r") as f:
    data = json.load(f)


#  update student.json

#  update age
data["age"] = 22

#  add new cource 
data["courses"].append("Chemistry")


#  updated data ko file mein write krenge ab

with open("student.json", "w") as f:
    json.dump(data, f)

print(data)