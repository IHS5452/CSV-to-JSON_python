import csv
import json

# Replace the text with the FULL file path you have the CSV file saved at
csv_file = 'FULL_FILE_PATH_FOR_CSV_FILE'
# Replace the text with the FULL file path you want the JSON to be saved at
json_file = 'FULL_FILE_PATH_FOR_NEW_JSON_FILE'

data = []

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        key = row[0]
        values = {}
        for i in range(1, len(headers)):
            values[headers[i]] = row[i]
        data.append({key: values})

with open(json_file, 'w') as file:
    json.dump(data, file)
