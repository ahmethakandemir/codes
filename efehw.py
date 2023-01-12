import time
import random
startTime = time.time()
list = []
uniqueList = []
uniqueTest = []
def efe():
    counter = 0
    for i in range(1,11):
        uniqueTest.append(i)
    uniqueTest.sort()
    while True:
        x = random.randint(1,10)
        list.append(x)
        
        counter += 1
        if x not in uniqueList:
            uniqueList.append(x)
            uniqueList.sort()
        if uniqueList == uniqueTest:
            return counter
        
            
                
print(efe())
print(f"{time.time() - startTime} secs")
