import os
import shutil
from os import path


def get_downloads():
    #/A /B C:\Users\%USERNAME%\Downloads
    #command = "cd %HOMEPATH%/Downloads && dir /A /B"
    #results = os.popen(command).read().strip();
    os.chdir(path.expanduser('~')+"\Downloads")
    results = os.listdir()

    img_types = ['jpeg','gif','img','jpg','png']
    readable_types = ['pdf','doc','rtf','docx']
    compressed_file_types = ['tar','zip','.msi','iso']
    sound_types = ['mp4']
    installer_types = ['exe']

    for line in results:

        ext = line.split('.')
        ext = ext[1]

        if ext in installer_types:
            move_files(line, 'Desktop/Installers')
        elif ext in readable_types:
            move_files(line, 'Documents')
        elif ext in img_types:
            move_files(line,'Pictures')
        elif ext in sound_types:
            move_files(line,'Videos')
        elif ext in compressed_file_types:
            move_files(line,"Setups")

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

    #shutil.move(path.realpath(item), path.expanduser('~')+'\\'+target)
    #print("Moved: {} to {}".format(item,target))
    command = 'cd %HOMEPATH%/Downloads && move "'+item.strip()+'" %HOMEPATH%/'+target
    results = os.popen(command).read()
    print(results)

get_downloads();
