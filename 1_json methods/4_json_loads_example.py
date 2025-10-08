import json

json_str = '{"fruit": "Mango", "color": "Yellow"}'

# JSON string → Python dict
data = json.loads(json_str)

print("JSON String:", json_str)
print("Python Dict:", data)
