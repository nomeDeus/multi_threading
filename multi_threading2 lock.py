import thread
import time

def Thread_with_lock(name, sleeptime, lock, *args):
    while(True):
        #lock.acquire()
        print('Enter_{0}\n'.format(name))
        time.sleep(sleeptime)
        print('Leave_{0}\n'.format(name))
        #lock.leave()

if __name__ == "__main__":
    lock = thread.allocate_lock() # allocate_lock() from _thread (Low-level threading API)
    thread.start_new_thread(Thread_with_lock, ("Lock1", 2, lock))
    thread.start_new_thread(Thread_with_lock, ("Lock2", 2, lock))

    while (True):
        pass
