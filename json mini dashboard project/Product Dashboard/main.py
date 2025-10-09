import json

with open(r"C:\Users\dhruv\Desktop\json project\Product Dashboard\products.json", "r") as file:
    data = json.load(file)

found = False

for product in data["products"]:
    total_stock = product["stock"]["warehouse"] + product["stock"]["store"]
    if total_stock > 20:
        print(product["name"])
        found = True
if not found:
    print("not found")