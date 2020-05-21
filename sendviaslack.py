import os
import sys

sys.path.append('/home/pi/.local/lib/python3.7/site-packages')

from operator import itemgetter
from slacker import Slacker


PATH = str(os.path.abspath(__file__)[:-len(os.path.basename(__file__))])


def send():
    # APIトークンを指定
    token = 'xoxb-848438480896-1141381587457-8hPhpeuI48ScfkXAvTuaLM4X'
    # アップロードするチャンネルを指定
    channel = 'backintime-camera'
    # 絶対パスを指定
    filelists = []
    for file in os.listdir(PATH[:-1]):
        base, ext = os.path.splitext(file)

        if ext == '.mov':
            filelists.append([file, os.path.getctime(PATH + file)])

    filelists.sort(key=itemgetter(1), reverse=True)
    filename = filelists[0][0]

    print(filename)
    file = PATH + filename
 
    slacker = Slacker(token)
    slacker.files.upload(file_=file, channels=channel)
 
if __name__ == "__main__":
    send()