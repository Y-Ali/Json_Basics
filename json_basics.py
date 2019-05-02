import json
import pdb

car = {"engine": "electric" , "brand": "Tesla"}
print(type(car))
print(car["engine"])

string_car = json.dumps(car)
print(type(string_car)) # .dumps changes the json to a formatted string
print(string_car)
print(string_car[0])

# Saving / Creating / Encoding Jsn
# to open a file, you need to first create a path using the 'with open' built-in function
with open('example_json_car_file', 'w') as this_is_the_path_name_for_the_file:
    json.dump(car, this_is_the_path_name_for_the_file)

# Opening / Loading / Decoding Json
with open('example_json_car_file') as json_file_to_load:
    json_loaded_obj = json.load(json_file_to_load)
    #breakpoint()
    print(json_loaded_obj)
    print(type(json_loaded_obj))
    for key in json_loaded_obj:
        print("this is a key: ", key)
        print("this is a value: ", json_loaded_obj[key],"\n")