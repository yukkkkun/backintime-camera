import time
import threading

import outputvideo
import maketexts

CNT = 30

def take_shoot():
    maketexts.make_text_newvideos(CNT)
    outputvideo.outputvideo()

if __name__ == "__main__":
    take_shoot()

    