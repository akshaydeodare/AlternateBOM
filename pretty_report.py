import json
import sys
print("Usage: python pretty_report.py path/to/dependency-check-report.json")
with open(sys.argv[1],"r") as json_file:
    json_object = json.load(json_file)

json_file.close()
value=json.dumps(json_object, indent=1)
myfile=open("dependency-check-report.json","w")
myfile.write(value)
myfile.close()
