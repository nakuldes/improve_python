
import random
from time import sleep
from threading import Thread
import queue

def producer(q):
    while True:
        print("ready to produce.")
        q.put(random.randint(1,50))
        print("\nproduced")
        sleep(3)

def consumer(q):
    while True:
        print("Ready to consume")
        print("\nConsuming "+str(q.get()))
        sleep(3)

q = queue.Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))

t1.start()
t2.start()