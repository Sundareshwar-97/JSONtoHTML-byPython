from json2table import *

json_object = {    "Sample": [
        {
            "col1": "val1",
            "col2": "val2"
        }
    ]}
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style": "width:100%"}
input = convert(
    json_object, build_direction=build_direction, table_attributes=table_attributes
)
print(input)
