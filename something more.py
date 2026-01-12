import random
import time
a= input("Press enter to begin")
t='True'
i=0
while t=='True' :
    q =(random.randrange(0, 101))
    s=random.choice(['*','+','-'])
    m=(random.randrange(0, 101))
    print (q,s,m)
    if s=='*' :
        w=q * m
    if s=='+':
         w=q+m
    if s=='-' :
        w=q-m
    g=int(input())
    p=time.time()
    i=i+1
    r=time.time()
    if g==w :
        t='True'
    if (r-p)>= 3 :
        t='False'
        print("Time out")
    if g!=w :
        t='False'

print(w)

print ('Your score is', i-1)
print("Close the window and press F5 in the coding window and try again")

    
    



