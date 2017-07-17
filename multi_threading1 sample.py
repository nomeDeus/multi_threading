#-*- coding: utf-8 -*-
import thread
import time

def MyFirstThread(name, sleeptime, *args):
    while(True):
        print('{0}_{1}\n'.format(name, sleeptime))
        time.sleep(sleeptime)

if __name__ == "__main__":
    for i in range(1, 6):
        #第一個參數就是 thread function，第二個參數是我們要傳進去的資料(tuples)
        thread.start_new_thread(MyFirstThread, ("Thread", i))
    while(True):
        print('MainThread {0}\n'.format(thread.get_ident()))
        time.sleep(1)
