data = {
    "name": "Riya",
    "age": 21,
    "city": "Mumbai"
}
try: 
    del data["age"]
    print(data)
except KeyError:
    print("age key does not exist in data dictonary")
