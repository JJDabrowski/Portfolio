import os, shutil
from flask import render_template

def SeekNMove(path_from, path_to, file_count):
    size = 0
    size_list = []
    file_list = []
    list_of_lists = []

    max_size = 0
    filePath = ''
    large_file = ''
    large_file_path = ''
    large_file_destination = ''

    for folder, subfolders, files in os.walk(path_from):

        for file in files:
            size = os.stat(os.path.join( folder, file )).st_size
            size_list.append(size)
            filePath = os.path.join( folder, file )
            file_list = [file, filePath, size]
            list_of_lists.append(file_list)

    sorted_sl = sorted(size_list)

    try:
        for j in range (file_count):
            max_size = sorted_sl[-1]
            for i in list_of_lists:
                if max_size in i:
                    large_file_path = i[1]
                    large_file = i[0]
                    large_file_destination = os.path.join( path_to, large_file )
                    shutil.move( large_file_path, large_file_destination )
                    list_of_lists.remove(i)
                    sorted_sl.remove(max_size)
    except IndexError as error:
        return render_template('congrats.html'), 200