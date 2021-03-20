from flask import Flask, render_template, request, send_from_directory, redirect, url_for, after_this_request, \
    send_file, flash
import os
from test_script import *


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
ALLOWED_EXTENSION = {'txt', 'srt'}
app.config.update()
files_uploaded = 0


@app.route('/')
def index_page():

    # Checks if the uploads folder exists, if not create an uploads folder.
    upload_folder = APP_ROOT + '/uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    return render_template('index.html', file_exist_srt=os.path.isfile(os.path.join(upload_folder, 'subs.srt')),
                           file_exist_out=os.path.isfile(os.path.join(upload_folder, 'out_test.json')),
                           file_exist_script=os.path.isfile(os.path.join(upload_folder, 'script.txt')),
                           total_upload=files_uploaded)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION


@app.route('/upload_srt', methods=['GET', 'POST'])
def upload_srt():
    global files_uploaded

    upload_folder = os.path.join(APP_ROOT, 'uploads')

    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        if allowed_file(filename):
            dest = f'{upload_folder}/{filename}'
            new_file = f'{upload_folder}/subs.srt'
            f.save(dest)
            os.rename(dest, new_file)
            files_uploaded += 1
        else:
            flash('File extension not allowed!')
        return redirect('/')


@app.route('/upload_script', methods=['GET', 'POST'])
def upload_script():
    global files_uploaded

    upload_folder = os.path.join(APP_ROOT, 'uploads')

    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        if allowed_file(filename):
            dest = f'{upload_folder}/{filename}'
            new_file = f'{upload_folder}/script.txt'
            f.save(dest)
            os.rename(dest, new_file)
            files_uploaded += 1
        else:
            flash('File extension not allowed!')
        return redirect('/')


@app.route('/process')
def process():
    global files_uploaded
    # TODO: Make it process script and subs files. Return JSON file.
    upload_folder = os.path.join(APP_ROOT, 'uploads')
    srt_in = os.path.join(upload_folder, 'subs.srt')
    script_in = os.path.join(upload_folder, 'script.txt')
    file_out = os.path.join(upload_folder, 'out_test.json')
    add_test(script_in, srt_in, file_out)
    files_uploaded = 0
    return redirect(url_for('index_page'))


@app.route('/downloads', methods=['GET', 'POST'])
def download():
    # TODO: Make it download the appropriate output file
    upload_folder = os.path.join(APP_ROOT, 'uploads')
    file_path = os.path.join(upload_folder, 'out_test.json')

    @after_this_request
    def remove_files(response):
        os.remove(file_path)
        return response

    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run()
