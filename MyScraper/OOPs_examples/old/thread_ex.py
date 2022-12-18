"""
Creating thread 
using function OR extend Thread class(threading module) OR both
f.start()

t.run()
t.start()
"""

from threading import Condition, Lock, Thread, current_thread
from time import sleep

class ThreadExample:
    def __init__(self, num):
        self.num = num
        print("available ="+ str(num))
        self.l = Condition()
        self.booked = 0
    
    def display_anything(self, user, tkt):
        
        self.l.acquire()
        
        print('{0} requested {1} tickets'.format(user, tkt))
        self.num = self.num -  tkt
        sleep(1)
        if(self.num< 0):
            print("\ntkts exhausted for {0} as available tkts are {1} and requested {2}".format(user, self.num, tkt))
            self.num = self.num + tkt
        else:
            print('{0} booked by {1}'.format(tkt, user))
            self.booked = self.booked + tkt
        self.l.notify()
        self.l.release()

    def display_tickets(self):  
        self.l.acquire()
        self.l.wait(timeout=1)  
        self.l.release()
        print("\nTotal remaining =" + str(self.num))
        print("\ntotal booked =" + str(self.booked))
        
        

print(current_thread().getName())  
obj = ThreadExample(5)
t1 = Thread(target=obj.display_anything, args=('dev',3))
t2 = Thread(target=obj.display_anything, args=('ved',3))
t3 = Thread(target=obj.display_anything, args=('edi',1))
t1.start()
t2.start()
t3.start()

obj.display_tickets()
