import json
from json.decoder import JSONDecodeError

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# JSON to Python

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Python to JSON

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x, indent=2, sort_keys=True)

# the result is a JSON string:
print(y)


# # Open external JSON
# with open("states.json") as f:
#     data = json.load(f)

# for state in data["states"]:
#     print(state["name"], state["abreviation"])

# # # write the new json
# with open("new_states.json", "w") as f:
#     json.dump(data, f, indent=2)


# # other example of multilevel JSON
# data = json.loads("some_source_file.json")
# usd_rates = dict()

# for item in data["list"]["resources"]:
#     name = item["resource"]["fields"]["name"]
#     price = item["resource"]["fields"]["price"]
#     usd_rates[name] = price

# print(50 * float(usd_rates["USD/INR"]))
