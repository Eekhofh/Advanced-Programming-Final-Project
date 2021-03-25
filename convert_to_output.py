import csv
import json


def convert_to_csv(dict):
    with open('csv_output.csv', 'w') as csv_file:
        fieldnames = ['line', 'metadata', 'scene boundary', 'scene description', 'actor', 'dialogue', 'time']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

        writer.writeheader()
        line_number = ""
        metadata = ""
        scene_boundary = ""
        scene_description = ""
        actor = ""
        line_text = ""
        time = ""

        for line in dict:
            line_number = line
            if dict[line] == None:
                break
            metadata = dict[line].get("M", "")
            scene_boundary = dict[line].get("S", "")
            scene_description = dict[line].get("N", "")
            actor = dict[line].get("C", "")
            line_text = dict[line].get("D", "")
            time = dict[line].get("timestamp", "")
            writer.writerow({'line': line_number, 'metadata': metadata,
                            'scene boundary': scene_boundary,
                            'scene description': scene_description,
                            'actor': actor, 'dialogue': line_text,
                            'time': time})

        return csv_file


def convert_to_json(dict):
    with open('output.json', 'w') as json_file:
        json_file = json.dump(dict, json_file, indent = 2)

    return json_file
