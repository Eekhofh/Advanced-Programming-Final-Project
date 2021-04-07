from flask import Flask, render_template, request, send_from_directory, redirect, url_for, after_this_request, \
    send_file, flash
import os
from test_script import *
from final_project import *
import calculate_matches

app = Flask(__name__)

# Set the root of the file
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
print(APP_ROOT)
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
app.config.update()
file_option = None
sub_script_match = None


@app.route('/')
def index_page():

    # Checks if the uploads folder exists, if not create an uploads folder.
    upload_folder = APP_ROOT + '/uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    return render_template('index.html', file_exist_srt=os.path.isfile(os.path.join(upload_folder, 'subs.srt')),
                           file_exist_out=os.path.isfile('json_output.json'),
                           file_exist_script=os.path.isfile(os.path.join(upload_folder, 'script.txt')),
                           script_match=sub_script_match)


def allowed_file(filename, extension):
    # This function checks if the file extension is allowed or not. It gets a filename as input and a list
    # of allowed extensions.
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == extension


@app.route('/upload_srt', methods=['GET', 'POST'])
def upload_srt():
    # This function is the upload button for .srt files.

    upload_folder = os.path.join(APP_ROOT, 'uploads')

    # Checks if a POST request is being done, if it is then get the file and check the extension.
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        if allowed_file(filename, 'srt'):
            # If the extension is allowed, then save the file on the machine and rename it to subs.srt.
            # This is so that the file is known as the subtitles file for the whole program.

            dest = f'{upload_folder}/{filename}'
            new_file = f'{upload_folder}/subs.srt'
            f.save(dest)
            os.rename(dest, new_file)
        else:
            flash('File extension not allowed! Only .srt is allowed.')
        return redirect('/')


@app.route('/upload_script', methods=['GET', 'POST'])
def upload_script():
    # This function is the upload button for .srt files.

    upload_folder = os.path.join(APP_ROOT, 'uploads')

    # Checks if a POST request is being done, if it is then get the file and check the extension.
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        if allowed_file(filename, 'txt'):
            # If the extension is allowed, then save the file on the machine and rename it to subs.srt.
            # This is so that the file is known as the subtitles file for the whole program.

            dest = f'{upload_folder}/{filename}'
            new_file = f'{upload_folder}/script.txt'
            f.save(dest)
            os.rename(dest, new_file)
        else:
            flash('File extension not allowed! Only .txt is allowed.')
        return redirect('/')


@app.route('/process', methods=['POST'])
def process():
    global file_option, sub_script_match
    # When the user presses the Process button, the file path will be get and given to the process script.
    # This script will combine the two files and return one file.
    file_path_subs = os.path.join(APP_ROOT, 'uploads', 'subs.srt')
    file_path_script = os.path.join(APP_ROOT, 'uploads', 'script.txt')

    file_option = request.form['file_option']
    run_process()

    os.remove(file_path_script)
    os.remove(file_path_subs)

    sub_script_match = calculate_matches.calculate_matches('json_output.json')
    return redirect(url_for('index_page'))


@app.route('/downloads', methods=['GET', 'POST'])
def download():
    # When the combined file is available, the user can press the download button to download this specific file.
    file_path_csv = os.path.join(APP_ROOT, 'csv_output.csv')
    file_path_json = os.path.join(APP_ROOT, 'json_output.json')
    dialogue_file = os.path.join(APP_ROOT, 'dialogue_aligned.txt')

    @after_this_request
    def remove_files(response):
        # After the file has been downloaded, it will be removed locally.
        os.remove(file_path_csv)
        os.remove(file_path_json)
        os.remove(dialogue_file)
        return response

    if file_option == 'csv':
        return send_file(file_path_csv, as_attachment=True)
    else:
        return send_file(file_path_json, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
