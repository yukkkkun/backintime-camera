import subprocess
import threading
import datetime
import os


now = datetime.datetime.now()
filename = 'video' + '{0:%Y%m%d%H%M}'.format(now) + '.mov'

PATH = str(os.path.abspath(__file__)[:-len(os.path.basename(__file__))])
OUTPUT = PATH + filename


def outputvideo():
    command = 'ffmpeg -safe 0 -f concat -i {}mylist.txt -acodec copy -vcodec copy {}'.format(PATH, OUTPUT)
    print(command)
    proc = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('test1')
    output,error = proc.communicate()
    print(output)
    print(error)

# ffmpeg -f concat -safe 0 -i C:\C\input.txt -c copy C:\C\output.mp4


if __name__ == "__main__":


    outputvideo()
    print(OUTPUT)