import json

with open(r"C:\Users\dhruv\Desktop\json project\Mini E-Commerce Dashboard\ecommerce.json", "r") as file:
    data = json.load(file)



for order in data["orders"]:
    if order["status"] == "delivered":
        total_amount = 0
        for item in order["items"]:
            amount = item["qty"] * item["price"]
            total_amount += amount
        print(f"Order Id: {order['order_id']}, Customer: {order['customer']['name']}, Total Amount: {total_amount}")

for order in data["orders"]:
    if order["status"] == "pending":
        order["status"] = "processing"

with open(r"C:\Users\dhruv\Desktop\json project\Mini E-Commerce Dashboard\ecommerce.json", "w") as file:
    json.dump(data, file, indent=4)