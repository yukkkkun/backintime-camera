import os
from operator import itemgetter

PATH = str(os.path.abspath(__file__)[:-len(os.path.basename(__file__))])

def make_text_newvideos(CNT):

    print('makng texts')

    filelists = []
    for file in os.listdir(PATH[:-1]):
        # print(file)
        base, ext = os.path.splitext(file)

        # print(base, "ext", ext)
        if ext == '.ts':
            filelists.append([file, os.path.getctime(PATH + file)])

    filelists.sort(key=itemgetter(1), reverse=True)

    save_filelists = []
    delete_filelists = []

    # print(filelists)

    for i,file in enumerate(filelists):
        if i < CNT:
            save_filelists.append('file ' + PATH + file[0])

            # os.remove(file[0])
        else:
            delete_filelists.append('file ' + PATH + file[0])
    # save usefiles as a text file

    save_filelists.sort(reverse=False)
    f = open(PATH + 'mylist.txt', 'w')
    for x in save_filelists:
        f.write(str(x) + "\n")
    f.close()


if __name__ == "__main__":

    CNT = 10
    make_text_newvideos(CNT)
    print(PATH)