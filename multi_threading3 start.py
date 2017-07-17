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
        MyThread('Threading', i).start()
