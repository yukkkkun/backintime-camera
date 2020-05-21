import outputvideo
import maketexts
import sendviaslack


CNT = 30

def take_shoot():
    
    maketexts.make_text_newvideos(CNT)
    outputvideo.outputvideo()
    sendviaslack.send()
if __name__ == "__main__":
    take_shoot()