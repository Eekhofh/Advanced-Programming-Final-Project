from flask import Flask, render_template, request, send_from_directory, redirect, url_for, after_this_request, send_file
import os
from test_script import *


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index_page():
    # TODO: When user leaves, restore page to standard.
    # TODO: Create two upload buttons. One for script and other for SRT.
    # TODO: Change the upload buttons to the files themselves, files can be replaced if needed! User error?

    # Checks if the uploads folder exists, if not create an uploads folder.
    upload_folder = APP_ROOT + '/uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    return render_template('index.html', file_exist_in=os.path.isfile(os.path.join(upload_folder, 'test.txt')),
                           file_exist_out=os.path.isfile(os.path.join(upload_folder, 'out_test.txt')))


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # TODO: Make it only accept SRT and Script files.
    # TODO: Rename the input files to script and subs
    upload_folder = os.path.join(APP_ROOT, 'uploads')
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        dest = f'{upload_folder}/{filename}'
        f.save(dest)
        return redirect(url_for('process'))


@app.route('/process')
def process():
    # TODO: Make it process script and subs files. Return JSON file.
    upload_folder = os.path.join(APP_ROOT, 'uploads')
    file_in = os.path.join(upload_folder, 'test.txt')
    file_out = os.path.join(upload_folder, 'out_test.txt')
    add_test(file_in, file_out)
    return redirect(url_for('index_page'))


@app.route('/uploads/<name>', methods=['GET', 'POST'])
def download(name):
    # TODO: FIX THE DOWNLOAD PROCESS
    # TODO: Make it download the appropriate output file
    upload_path = os.path.join(APP_ROOT, 'uploads')
    file_path = os.path.join(upload_path, name)
    print(file_path)
    file_handle = open(file_path, 'r')

    @after_this_request
    def remove_file(response):
        if request.endpoint == 'download':
            os.remove(file_path)
        return response

    return send_file(file_handle, mimetype="text/plain")


if __name__ == '__main__':
    app.run()
