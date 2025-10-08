import json

data = {
    "students": [] # empty list to store multiple students
}
times = 3 # number of inputs

while times > 0:
    name = input("Enter your name: ")
    marks = float(input("Enter your marks: "))

     # add this student to the list
    student = {"Name" : name, "Marks" : marks} 
    data["students"].append(student)
    times -= 1

#  add data in mulitple_students.json file
with open(r"C:\Users\dhruv\Desktop\json\intermediate json\jsonfile\multiple_students.json", "w") as file:
    json.dump(data, file, indent=4)