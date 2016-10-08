import os
import shutil
from os import path
import json

files_types = {}

with open('pointer.json') as pointer:
    files_types = json.load(pointer)


def get_downloads():
    os.chdir(path.expanduser('~')+"\Downloads")
    results = os.listdir()

    for line in results:
        ext = line.split('.')

        try:
            switch_board(ext, line)
        except Exception as ex:
            print(ex)
            ext[0] += ' (COPY)'
            switch_board(ext, line)


def move_files(item, target):
    target = target.strip()
    os.chdir(path.expanduser('~'))

    if os.path.exists(target):
        if not os.path.exists('Downloads/Copies/'):
            os.mkdir('Downloads/Copies')

        if not os.path.exists('Downloads/Copies/'+target):
                os.mkdir('Downloads/Copies/'+target)

        target = 'Downloads/Copies/'+target

    elif os.path.exists('Desktop/'+target):
        target = 'Desktop/'+target

    elif not os.path.exists(target):
        os.chdir('Documents')

    shutil.move(item, path.expanduser('~')+'\\'+target)
    print("Moved: {} to {}".format(item, target))


def switch_board(ext, line):
    os.chdir(path.expanduser('~')+"\Downloads")
    location = path.realpath(line)

    img_types = ['jpeg', 'gif', 'img', 'jpg', ' png']
    readable_types = ['pdf', 'doc', 'rtf',
                      'docx', 'xls', 'csv',
                      'json', '.log']
    compressed_file_types = ['tar', 'zip', '.msi', 'iso']
    sound_types = ['mp4']
    installer_types = ['exe']

    if len(ext) > 1:
        ext = ext[1]

    if ext in files_types['installer_types']:
        move_files(location, 'Installers')
    elif ext in files_types['readable_types']:
        move_files(location, 'Documents')
    elif ext in files_types['img_types']:
        move_files(location, 'Pictures')
    elif ext in files_types['sound_types']:
        move_files(location, 'Videos')
    elif ext in files_types['compressed_file_types']:
        move_files(location, 'Setups')


get_downloads()
