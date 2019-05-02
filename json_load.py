import json

with open("new_json_car_file") as json_file:
    car = json.load(json_file)

print(car["engine"])