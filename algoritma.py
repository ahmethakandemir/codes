from re import A
import time
'''
import random
trials=0
a=[8,25,24]
x=0
while x not in a:
    x=random.randint(1,100)
    trials=trials+1
print("trials: ",trials,'guessed number is: ',x) 
'''
'''
customers = {"a","b","c","d"}

def cus_ser(a, b="User not exist"):
    if b not in customers:
        print(b, "age is: ", a)
    else:
        print("age is: ", a, "ID is: ", b)
cus_ser(15)
'''
'''
print("objects,sep='',end="'\n',file=sys.stdout, flush=False)
'''
'''
def ac(b = int(input("sayı giriniz: "))):
    a = b
    for i in range(b):  
        if a == 1:  
            print("aferim")
            x=False
        else:
       
            print("devaaaam")
            a-=1
    return a
        
ac()
'''
'''
g = str(input("Input is : "))
def guess():
    m = "input"
    for i in range(5):
        if g[i] == m[i]:
            print(i + 1 , ". letter in the correct place")
        elif g[i] in m:
            print(i + 1, ". letter is correct but in different place")
        else:
            print(i + 1,". letter is not correct")
            
guess()

''''''
g = str(input("input is : "))
def guessWord():
    m = "input"
    if g == m:
        print("word is correct")
        return
    
    a = False
    for k in range(5):
        for i in range(5):
            if g[i] == m[k]:
                a = True
    for i in range(5):
        if g[i] == m[i]:
            print("at least one letter is in correct place")
            break
    for i in range(5):
        if a and g[i] != m[i]:
            print("at least one letter is correct but in different place")
            return
    for i in range(5):
        if not a:
            print("no letter is in the word")
            return

guessWord()

''''''
g = str(input("input is : "))
def guessWord():
    m = "input"
    if g == m:
        print("word is correct")
        return
    for i in range(5):
        if g[i] == m[i]:
            print("at least one letter is in correct place")
            break
    for i in range(5):
        if g[i] in m and g[i] != m[i]:
            print("at least one letter is correct but in different place")
            return
    for i in range(5):
        if g[i] == m[i]:
            return    
    for i in range(5):
        if g[i] not in m:
            print("no letter is in the word")
            return

guessWord()
'''
'''
g = str(input("input is : "))
def guessWord():
    m = "input"
    if g == m:
        print("word is correct")
        return
    a = False
    for k in range(5):
        for i in range(5):
            if g[i] == m[k]:
                a = True
    for i in range(5):
        if g[i] == m[i]:
            print("at least one letter is in correct place")
            break
    for i in range(5):
        if a and (g[i] != m[i]):
            print("at least one letter is correct but in different place")
            return
    for i in range(5):
        if not a:
            print("no letter is in the word")
            return

guessWord()
'''
'''''''''
g = str(input("input is : "))
def guessWord():
    m = "input"
    if g == m:
        print("word is correct")
        return
    a = False
    for k in range(5):
        for i in range(5):
            if g[i] == m[k]:
                a = True
    for i in range(5):
        if g[i] == m[i]:
            print("at least one letter is in correct place")
            break
    for i in range(5):
        for k in range(5):
            if g[i] == m[k]:
                if g[i] != m[i]:
                    print("at least one letter is correct but in different place")
                    return
    for i in range(5):
        if g[i] == m[i]:
            return    
    for i in range(5):
        if not a:
            print("no letter is in the word")
            return

guessWord()
'''''''''