import random

def rock_game():
    print("THE ROCK PAPER GAME")
    print("You V/s Computer")
    print("Press enter to begin")
    enter=input()
    print("1. Point game \n2. Instant game")
    gm=int(input('Enter 1 or 2'))
    
    def rules(m,c,l):
        ans='c'
        if m==c:
            ans='continue'
        elif (m==l[1]) and (c==l[0]):
            ans='m'
        elif (m==l[0]) and c==l[2]:
            ans='m'
        elif (m==l[0]) and c==l[3]:
            ans='m'
        elif (m==l[2]) and c==l[1]:
            ans='m'
        elif (m==l[3]) and c==l[1]:
            ans='m'
        elif (m==l[3]) and c==l[2]:
            ans='m'
        return ans

    l=['rk', 'pa','pn','sc']
    if gm==2:
        
        ans='c'
        while ans=='c':
            user=input(f'Enter {l}')
            ch=random.choice(l)
            print(ch)
            ans=rules(user,ch,l)
    elif gm==1:
        pm,pc=0,0
        pn=int(input('Enter the total point to finish'))
        while pm<pn and pc<pn:
            user=input(f'Enter {l}')
            ch=random.choice(l)
            print(ch)
            ans=rules(user,ch,l)
            if ans=='m':
                pm+=1
            elif ans=='c':
                pc+=1
            print('User=',pm,' , Computer=',pc)
            
            
            
        
        
            

            










            
            
            
            
        
        
        
    
    
rock_game()
