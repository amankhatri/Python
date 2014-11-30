__author__ = 'kaman'
import threading
#since this class is threaded multiple objects from this class can exist at same time
class BuckysMessanger(threading.Thread):
    def run(self):
        for _ in range(10): # i wanna look 10 times and I don't really care about the variable
           print(threading.current_thread().getName())

x = BuckysMessanger(name="Send out messages")
y = BuckysMessanger(name="Receive Messages")
#when ever we want to start the thread we have to call start a thread and whenever we do start it looks for a run method
x.start()
y.start()