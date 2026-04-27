import os

def write_json(filename):
    data = {
        "people": [
            {"name": "john Doe", "age": 30},
            {"name": "jane smith", "age": 25}
        ]
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Wrote {filename} successfully")

def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        for person in data["people"]:
            print(f"Name: {person['name']}, Age: {person['age']}")

def delete_json(filename):
