import os
from operator import itemgetter
import time


def delete_olds(CNT):

    filelists = []
    for file in os.listdir():
        base, ext = os.path.splitext(file)

        # print(base, "ext", ext)
        if ext == '.ts':
            filelists.append([file, os.path.getctime(file)])

    filelists.sort(key=itemgetter(1), reverse=True)

    save_filelists = []
    delete_filelists = []

    for i,file in enumerate(filelists):
        if i > CNT + 5 - 1:
            os.remove(file[0])
            # print('{}は削除します'.format(file[0]))

def keep_deliting_olds(CNT):
    while True:
        delete_olds(CNT)
        time.sleep(10)
        
    
if __name__ == "__main__":
    CNT = 10
    delete_olds(CNT)