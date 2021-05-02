from json2html import *
import json
with open("data.json", "r") as f:
    json_object = json.loads(f.read())

#print(json_object)
html = json2html.convert(json = json_object)
print(html)