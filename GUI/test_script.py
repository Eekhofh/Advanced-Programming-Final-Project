import os
import json


def add_test(script, srt, dest):
    with open(script, 'r') as f:
        script_test = f.readlines()

    with open(srt, 'r') as f:
        srt_test = f.readlines()

    new_text = ''.join(script_test) + ' ' + ''.join(srt_test)

    with open(dest, 'w') as new_f:
        new_f.write(json.dumps(new_text))

    os.remove(script)
    os.remove(srt)
