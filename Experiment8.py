import csv
import json

# convert csv to json
input_file = "students.csv"
output_file = "students.json"

with open(input_file, "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

with open(output_file, "w" ) as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV file '{input_file}' converted to JSON file '{output_file}' successfully!")
print("JESON file created:", output_file)