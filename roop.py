import time
import threading

import savesinglevideo
import deleteoldvideo
import maketexts
CNT = 30

#save one second video
save_threading=threading.Thread(target=savesinglevideo.start_saving_onesecvideo)      
save_threading.setDaemon(True)
save_threading.start()


# if __name__ == "__main__":

#     time.sleep(30)
#     deleteoldvideo.delete_olds(CNT)
    


