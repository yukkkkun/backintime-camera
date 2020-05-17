import subprocess
import os
from operator import itemgetter
import rclone


DRIVE = "gremote:temp_share"
RCCONF = ".rclone.conf"


def send_gdrive():

    filelists = []
    for file in os.listdir():
        base, ext = os.path.splitext(file)

        if ext == '.mov':
            filelists.append([file, os.path.getctime(file)])

    filelists.sort(key=itemgetter(1), reverse=True)
    filename = filelists[0][0]

    # print(filename)

    command = 'rclone copy {} gremote:temp_share'.format(filename)
    print(command.split())

    result = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()

    # subprocess.call(command.split())
    print(output)
    print(error)


if __name__ == "__main__":
    send_gdrive()