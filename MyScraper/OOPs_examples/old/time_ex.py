# import time
from datetime import *

# epochseconds = time.time()
# print(epochseconds)

# t = time.ctime(epochseconds)
# print(t)

#dt = datetime.datetime.today()


det = date(2021, 1, 12)
tim = time(21, 30, 00)

dettim= datetime.combine(det, tim)
print (dettim)

assert dettim != None