import csv
import json


def convert_to_csv(dict):
    with open('csv_output.csv', 'w') as csv_file:
        fieldnames = ['line', 'actor', 'dialogue', 'time']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

        writer.writeheader()
        for line in dict:
            line_number = line.split()[1]
            actor = dict[line]['actor']
            line_text = dict[line]['line']
            time = dict[line]['time']
            writer.writerow({'line': line_number, 'actor': actor,
                            'dialogue': line_text, 'time': time})

        return csv_file


def convert_to_json(dict):
    with open('json_output.json', 'w') as json_file:
        json_output = json.dump(dict, json_file)

    return json_file
