import os


def add_test(file, dest):
    with open(file, 'r') as f:
        text_test = f.readlines()

    new_text = ''.join(text_test) + '1234'

    with open(dest, 'w') as new_f:
        new_f.write(new_text)

    os.remove(file)
