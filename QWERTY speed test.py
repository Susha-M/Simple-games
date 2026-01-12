print("This is a game just for testing your speed")
print("Rules are as follows")
print("An alphabet appears, click the alphabet quickly and press enter")
print("If you be late, time runs out, Remember!")
import random
import time
list=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
a= input ("Press enter to begin")
q =  random.choice(list)
print (q)
m=input() #input a number
if m==q:
    t='True'
else:
    t='False'

i=1
while t=='True' :
    k=random.choice(list)
    w=time.time()
    i=i+1
    print (k)
    m=input() #input a number
    r=time.time()
    
    if m==k :
        t='True'
    if (r-w)>= 1.8 :
        t='False'
        print("Time out")
    if m!=k :
        t='False'

print ('Your score is', i)
print("Close the window and press F5 in the coding window and try again")
    
    
    


