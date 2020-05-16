import os
from operator import itemgetter

PATH = str(os.path.abspath(__file__)[:-len(os.path.basename(__file__))])

def make_text_newvideos(CNT):

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
        if i > CNT - 1:
            delete_filelists.append('file ' + PATH + file[0])
            # os.remove(file[0])
        else:
            save_filelists.append('file ' + PATH + file[0])

    # save usefiles as a text file
    f = open('mylist.txt', 'w')
    for x in save_filelists:
        f.write(str(x) + "\n")
    f.close()


if __name__ == "__main__":

    CNT = 10
    make_text_newvideos(CNT)