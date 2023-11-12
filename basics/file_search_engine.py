import os
fileType='.mp4'

anyfile=os.listdir('Salman')
for file in anyfile:
    if file.endswith(fileType):
        print(file)


