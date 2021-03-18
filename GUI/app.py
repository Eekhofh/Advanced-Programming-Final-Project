from flask import Flask, render_template, request, send_from_directory, redirect, url_for, after_this_request, send_file
import os
from test_script import *


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
files_uploaded = 0

@app.route('/')
def index_page():
    # TODO: Create two upload buttons. One for script and other for SRT.
    # TODO: Change the upload buttons to the files themselves, files can be replaced if needed! User error?

    # Checks if the uploads folder exists, if not create an uploads folder.
    upload_folder = APP_ROOT + '/uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    print(files_uploaded)
    return render_template('index.html', file_exist_srt=os.path.isfile(os.path.join(upload_folder, 'subs.srt')),
                           file_exist_out=os.path.isfile(os.path.join(upload_folder, 'out_test.txt')),
                           file_exist_script=os.path.isfile(os.path.join(upload_folder, 'script.txt')),
                           total_upload=files_uploaded)


@app.route('/upload_srt', methods=['GET', 'POST'])
def upload_srt():
    global files_uploaded

    upload_folder = os.path.join(APP_ROOT, 'uploads')

    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        dest = f'{upload_folder}/{filename}'
        new_file = f'{upload_folder}/subs.srt'
        f.save(dest)
        os.rename(dest, new_file)
        files_uploaded += 1
        return redirect('/')


@app.route('/upload_script', methods=['GET', 'POST'])
def upload_script():
    global files_uploaded
    upload_folder = os.path.join(APP_ROOT, 'uploads')

    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        dest = f'{upload_folder}/{filename}'
        new_file = f'{upload_folder}/script.txt'
        f.save(dest)
        os.rename(dest, new_file)
        files_uploaded += 1
        return redirect('/')


@app.route('/process')
def process():
    # TODO: Make it process script and subs files. Return JSON file.
    upload_folder = os.path.join(APP_ROOT, 'uploads')
    file_in = os.path.join(upload_folder, 'script.txt')
    file_out = os.path.join(upload_folder, 'out_test.txt')
    add_test(file_in, file_out)
    files_upload = 0
    return redirect(url_for('index_page'))


@app.route('/downloads', methods=['GET', 'POST'])
def download():
    # TODO: Make it download the appropriate output file
    upload_folder = os.path.join(APP_ROOT, 'uploads')
    file_path = os.path.join(upload_folder, 'out_test.txt')

    @after_this_request
    def remove_files(response):
        os.remove(file_path)
        return response

    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run()
