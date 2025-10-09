import json

with open(r"C:\Users\dhruv\Desktop\json project\User_Data_Dashboard\users.json", "r") as file:
    data = json.load(file)


is_active = False

for user in data["users"]:
    if user["active"] == True:
        print(f"{user['name']} from {user['city']} is active")
        is_active = True
if not is_active:
    print("no active")