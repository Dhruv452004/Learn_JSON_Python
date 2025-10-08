import json

data = {"name": "Loha", "age": 21, "city": "Ayodhya"}

# Python dict → JSON string
json_str = json.dumps(data)

print("Python Dict:", data)
print("JSON String:", json_str)
