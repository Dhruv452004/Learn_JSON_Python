import json

# File se JSON padhna
with open("data.json", "r") as f:
    data = json.load(f)

print("Data read from file:", data)
print("Type:", type(data))
