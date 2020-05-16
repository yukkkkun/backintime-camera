

import savesinglevideo
import deleteoldvideo
import outputvideo



if __name__ == "__main__":

    #save one second video
    save_threading=threading.Thread(target=savesinglevideo.start_saving_onesecvideo)      
    save_threading.setDaemon(True)
    save_threading.start()


    while True:
        deleteoldvideo.
