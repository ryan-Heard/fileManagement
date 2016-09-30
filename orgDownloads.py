import os
import shutil
from os import path


def get_downloads():
    os.chdir(path.expanduser('~')+"\Downloads")
    results = os.listdir()

    img_types = ['jpeg', 'gif', 'img', 'jpg', ' png']
    readable_types = ['pdf', 'doc', 'rtf',
                      'docx', 'xls', 'csv',
                      'json', '.log']
    compressed_file_types = ['tar', 'zip', '.msi', 'iso']
    sound_types = ['mp4']
    installer_types = ['exe']

    for line in results:
        os.chdir(path.expanduser('~')+"\Downloads")
        location = path.realpath(line)
        ext = line.split('.')

        if len(ext) > 1:
            ext = ext[1]

        if ext in installer_types:
            move_files(location, 'Desktop/Installers')
        elif ext in readable_types:
            move_files(location, 'Documents')
        elif ext in img_types:
            move_files(location, 'Pictures')
        elif ext in sound_types:
            move_files(location, 'Videos')
        elif ext in compressed_file_types:
            move_files(location, 'Setups')


def move_files(item, target):
    target = target.strip()
    os.chdir(path.expanduser('~'))

    if os.path.exists(target):
        pass
    elif os.path.exists('Desktop/'+target):
        target = 'Desktop/'+target
    elif not os.path.exists(target):
        os.chdir('Desktop')
        os.mkdir(target)

    shutil.move(item, path.expanduser('~')+'\\'+target)
    print("Moved: {} to {}".format(item, target))


get_downloads()
