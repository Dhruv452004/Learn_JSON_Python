import json

name = input("Enter the name: ")
age = int(input("Enter your age: "))
city = input("Which city are you from: ")

data = {
    "Name" : name,
    "Age" : age,
    "City" : city
}

with open(r"C:\Users\dhruv\Desktop\json\intermediate json\jsonfile\user.json", "w") as file:
    json.dump(data, file, indent=4)