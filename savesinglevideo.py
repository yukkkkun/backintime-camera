import subprocess
import threading
import time

def start_saving_onesecvideo():
    command = 'ffmpeg -f alsa -thread_queue_size 1024 -i hw:0,0 -f v4l2 -thread_queue_size 256 -s 640x480 -framerate 24 -i /dev/video0 -b:v 8000k -c:v h264_omx -bufsize 500k -r 30 -vsync cfr -g 24 -c:a aac -b:a 256k -ar 44100 -bufsize 256k -flags +cgop+loop+global_header   -bsf:v h264_mp4toannexb -f hls -hls_list_size 120 -hls_time 1 -hls_flags delete_segments stream.m3u8'
    # you can take the ID of the process that you are executing and kill it based on PID, as example : 

    proc = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('test1')
    output,error = proc.communicate()
    print(output)
    print(error)


def shut_saving_onesecvideo():
    command = 'sudo killall ffmpeg'
    subprocess.call(command.split())



if __name__ == "__main__":

    save_threading=threading.Thread(target=start_saving_onesecvideo)      
    save_threading.setDaemon(True)
    save_threading.start()

    time.sleep(30)

    shut_saving_onesecvideo()