from json2table import *
import json
with open("data.json", "r") as f:
    json_object = json.loads(f.read())
    build_direction = "LEFT_TO_RIGHT"
    table_attributes = {"style": "width:100%"}
    input = convert(
        json_object, build_direction=build_direction, table_attributes=table_attributes
    )
print(input)
