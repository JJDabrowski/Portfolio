import os
from flask import Flask, request, render_template, url_for, redirect
from utils import SeekNMove

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/congratulations', methods=['POST'])
def RBF():
    try:
        if request.method == 'POST':
            path_from = request.form.get('from-path')
            path_to = request.form.get('to-path')
            number_deleted = request.form.get('file-count')

            if path_from and path_to:
                path1 = os.path.abspath(path_from)
                path2 = os.path.abspath(path_to)
                path3 = path2 + '/ToBeRemoved'
                file_count = int(number_deleted)

        try:
            os.mkdir(path3)
        except OSError as error:
            print(error)
            SeekNMove(path1, path3, file_count)
            return render_template('congrats.html'), 200

        SeekNMove(path1, path3, file_count)
        return render_template('congrats.html'), 200

    except UnboundLocalError as error:
        print(error)
        return redirect(url_for('index'), code=302)