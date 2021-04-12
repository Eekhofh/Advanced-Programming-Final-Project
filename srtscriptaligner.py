#!/usr/bin/python3
import sys
import json
import os
import ast
import convert_to_output


def load_file(filescript):
    # Loads a file and returns a list of the all the lines

    with open(filescript, encoding='latin-1') as f:
        data = f.readlines()

    return data


def clean_srt(srt_file):
    # places srt file content in dictionary
    # remove spaces around the items
    clean_lines = [item.strip() for item in srt_file if item.strip()]

    srt_dict = {}
    empty_list = []

    for item in clean_lines:
        if item.isnumeric():
            # if there is data in list save it to dictionary
            if empty_list:
                srt_dict[line_dict] = empty_list

            # saves the line number
            line_dict = item
            srt_dict[line_dict] = ""
            empty_list = []

        else:
            empty_list.append(item)

    return srt_dict


def clean_script(text_script):
    # reads script, removes empty lines and convert to dictionary
    script_dict = {}
    counter = 0

    for element in text_script:
        # removes wrong quotes
        if not element.isspace():
            # convert to dictionary
            x = ast.literal_eval(element)
            script_dict[counter] = x
            counter += 1

    return script_dict


def main():

    filescript = 'dialogue_aligned.txt'
    text_script = load_file(filescript)
    text_script = clean_script(text_script)

    root_folder = os.path.dirname(os.path.abspath(__file__))
    file_srt = os.path.join(root_folder, 'uploads', 'subs.srt')
    srt_file = load_file(file_srt)
    cleaned_srt = clean_srt(srt_file)

    # iternate over the script
    for line_numer, text in text_script.items():
        if type(text) is dict:
            # check if current dictionary is dialogue
            if "D" in text.keys():
                # get value from dialogue
                dialogue = text["D"]
                # iternate over dictionary and search for dialogue
                if dialogue != "":
                    for srt_key, srt_value in cleaned_srt.items():
                        if len(srt_value) > 1:

                            timestamp = srt_value[0]
                            current_dialogue = srt_value[1]

                            if dialogue in current_dialogue:
                                text["timestamp"] = timestamp

                                del cleaned_srt[srt_key]
                                break

    # Convert to json
    convert_to_output.convert_to_json(text_script)

    # Convert to csv
    convert_to_output.convert_to_csv(text_script)


if __name__ == '__main__':
    main()
