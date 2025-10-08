import json

with open(r"C:\Users\dhruv\Desktop\json\intermediate json\jsonfile\student.json", "r") as file:
    data = json.load(file)

print(data)

marks_list = []
for student in data["students"]:
    marks_list.append(student["marks"])
#  maximum marks
max_marks = max(marks_list)

for student in data["students"]:
    if student["marks"] == max_marks:
        topper = student["name"]
        break
print(f"Topper is {topper} with {max_marks} marks")

#  jo upr jo code likha marks_list vala usme bhi same kaam hora hein aur jo ye niche likha hein vo bhi same kaam kr rha h bs ye niche vala code upr vala short version hein. kaam dono same hi kar rhe hein bs mene socha ki agr koi mera code dekhra ho begineer tho use koi dikakt na ho. is method ka naam hein.....
#________________________________List comprehension method____________________________________# 

max_list = [student["marks"] for student in data["students"]]
max_marks = max(max_list)
for student in data["students"]:
    if student["marks"] == max_marks:
        topper = student["name"]
        break
print(f"Topper is {topper} with {max_marks} marks")