import os
import json
import label


def add_test(script, srt, current_folder, dest):
    new_script = os.path.join(current_folder, 'labeled_script.txt')
    with open(new_script, 'w', encoding='utf8') as new_f:
        with open(script, 'r', encoding='utf8') as f:
            for line in f:
                new_f.write(label.label_line(line))

    new_text='Dummy'

    with open(dest, 'w') as new_f:
        new_f.write(json.dumps(new_text))

    os.remove(script)
    os.remove(srt)
