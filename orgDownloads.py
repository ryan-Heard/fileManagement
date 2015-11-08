import os

def get_downloads():
    #/A /B C:\Users\%USERNAME%\Downloads
    command = "cd %HOMEPATH%/Downloads && dir /A /B"
    results = os.popen(command).read().strip();

    for line in results.split('\n'):
        if '.exe' in line:
            move_files(line, 'Desktop/Installers')
        elif '.pdf' in line or '.doc' in line or '.rtf' in line:
            move_files(line, 'Documents')
        elif '.jpeg' in line or '.gif' in line or '.img' in line or '.jpg' in line:
            move_files(line,'Pictures')
        elif '.mp4' in line:
            move_files(line,'Videos')
        elif '.tar' in line or '.zip' in line or '.msi' in line or '.iso' in line:
            move_files(line,"Setups")



def move_files(item, target):
    target = target.strip()
    directory = os.popen('cd %HOMEPATH% && cd').read().strip()
    directory += '/'

    if os.path.exists(directory+target):
        pass
    elif os.path.exists(directory+'Desktop/'+target):
        target = 'Desktop/'+target
    elif not os.path.exists(directory+target):
        os.popen('cd %HOMEPATH%/Desktop && md '+target)
        target = 'Desktop/'+target

    command = 'cd %HOMEPATH%/Downloads && move "'+item.strip()+'" %HOMEPATH%/'+target
    results = os.popen(command).read()

get_downloads();
