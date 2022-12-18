from threading import Condition, Thread


class Thread_example:
    
    def __init__(self): 
        self.q = 0  
        self.c = Condition()

    def evenfun(self):
        while self.q<100:
            self.q = self.q + 1
            if self.q%2 == 0:
                #print("Even -"+str(self.q))
                pass
        
    def oddfun(self):
        while self.q < 100:
            self.q = self.q + 1
            if self.q%2 != 0:
                #print("Odd -"+ str(self.q))
                pass

obj = Thread_example()

t1 = Thread(target=obj.evenfun)
t2 = Thread(target=obj.oddfun)

t1.start()
t2.start()

print(obj.q)