from threading import Timer

def saysomething(msg):
    print (msg)

tick = 3
hey = Timer(tick, saysomething, ['hey, hello'])
hey.start()
