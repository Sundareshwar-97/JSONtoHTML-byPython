# print("hi")
#x = int(input("enter some number"))
#print("Number you entered", x)
from json2table import *
json_object = {"key": "value"}
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style": "width:100%"}
input = convert(
    json_object, build_direction=build_direction, table_attributes=table_attributes
)
print(input)
