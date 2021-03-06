#-*- coding: utf-8 -*-
import thread
import time

def Thread_with_lock(name, sleeptime, lock, *args):
    while(True):
        #將第7、11行註解拿掉，將會同步
        #lock.acquire() #鎖上這個線程，在完成之前不讓其他線程對變數做干擾
        print('Enter_{0}\n'.format(name))
        time.sleep(sleeptime)
        print('Leave_{0}\n'.format(name))
        #lock.release() #解鎖這個線程，開始其他線程

if __name__ == "__main__":
    lock = thread.allocate_lock() # allocate_lock() from _thread (Low-level threading API)
    thread.start_new_thread(Thread_with_lock, ("Lock1", 2, lock))
    thread.start_new_thread(Thread_with_lock, ("Lock2", 2, lock))

    while (True):
        pass
