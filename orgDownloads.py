import os

def get_downloads():
    #/A /B C:\Users\%USERNAME%\Downloads
    command = "cd  %HOMEPATH%/Downloads && dir /A /B"
    results = os.popen(command).read().strip();

    for line in results.split('\n'):
        if '.exe' in line:
            move_files(line, 'Desktop/Installers')
        elif '.pdf' in line or '.doc' in line:
            move_files(line, 'Documents')
        elif '.jpeg' in line or '.gif' in line or '.img' in line:
            move_files(line,'Pictures')




def move_files(item, target):
    command = "cd %HOMEPATH%/Downloads && move "+item+" %HOMEPATH%/"+target
    results = os.popen(command).read()

get_downloads();
