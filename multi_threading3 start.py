#-*- coding: utf-8 -*-
#Thread 裡面 wrapper 了 start_new_thread()
from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, name, sleeptime):
        Thread.__init__(self)
        self.sleeptime = sleeptime
        self.setName(str(sleeptime))

    def run(self):
        while(True):
            print 'Threading_{0}\n'.format(self.getName())
            time.sleep(self.sleeptime)

if __name__ == "__main__":
    for i in range(1,5):
        #當呼叫 start() 時，會自動去呼叫 run()
        MyThread('Threading', i).start()

#P.S 只能夠 override __init()__ 和 run() ，不能夠 override start()
