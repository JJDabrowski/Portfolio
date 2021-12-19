#spróbować try dla for files oraz dla seeknmove

import os, shutil, logging
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        return render_template('home.html'), 200

@app.route('/about', methods=['POST'])
def about():
    if request.method == 'POST':
        return render_template('about.html'), 200

@app.route('/congratulations', methods=['POST'])
def RBF():
    if request.method == 'POST':
        path_from = request.form.get('fromPath')
        path_to = request.form.get('toPath')
        numberDeleted = request.form.get('nd')
        
        if path_from and path_to:
            path1 = os.path.abspath(path_from)
            path2 = os.path.abspath(path_to)
            path3 = path2 + '/ToBeRemoved'
            noDel = int(numberDeleted)

            #Variables definitions
            size = 0
            sizeList = []
            fileList = []
            fileListoList = []
            fullList = 0

            maxSize = 0
            filePath = ''
            bigFile = ''
            bigFilePath = ''
            bigFilePathRem = ''

            #SeekNMoveFunction
            def SeekNMove():
                for folder, subfolders, files in os.walk(path1):
      
                    for file in files:
                        size = os.stat(os.path.join( folder, file )).st_size
                        sizeList.append(size)
                        filePath = os.path.join( folder, file )
                        fileList = [file, filePath, size]
                        fileListoList.append(fileList)
            
                sizeListSort = sorted(sizeList)

                try:
                    for j in range (noDel):
                        maxSize = sizeListSort[-1]
                        for i in fileListoList:
                            if maxSize in i:
                                bigFilePath = i[1]
                                bigFile = i[0]
                                bigFilePathRem = os.path.join( path3, bigFile )
                                shutil.move( bigFilePath, bigFilePathRem )
                                fileListoList.remove(i)
                                sizeListSort.remove(maxSize)
                except IndexError as error:
                    return render_template('congrats.html'), 200

    try:
        os.mkdir(path3)
    except OSError as error: 
        SeekNMove()
        return render_template('congrats.html'), 200

    SeekNMove()
    return render_template('congrats.html'), 200 


if __name__ == "__main__":
    app.run(debug=True)
