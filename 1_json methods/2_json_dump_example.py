import json

data = {"language": "Python", "framework": "Flask"}

# File me JSON likhna
with open("data.json", "w") as f:
    json.dump(data, f)

print("✅ Data written to data.json file successfully!")

# Run karne ke baad same folder me ek file banegi 👉 data.json