import json

json_data = '{"name": "Ravi", "age": 25, "city": "Delhi"}'

json_str = json.loads(json_data)

print(f"{json_str['name']} is {json_str['age']} years old and lives in {json_str['city']}")