import thread
import time

def MyFirstThread(name, sleeptime, *args):
    while(True):
        print('{0}_{1}\n'.format(name, sleeptime))
        time.sleep(sleeptime)

if __name__ == "__main__":
    for i in range(1, 6):
        thread.start_new_thread(MyFirstThread, ("Thread", i))
    while(True):
        print('MainThread {0}\n'.format(thread.get_ident()))
        time.sleep(1)
