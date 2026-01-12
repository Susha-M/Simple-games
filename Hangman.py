import random
print('HANGMAN')
print('Instuctions to play the game')
print('Guess the word')
print('You have 8 chances if wrong')
print("Let's start the game")
wd=['soldier', 'drainage','flower','complicated','computer','university','bookcase','python','jaguar']
wr=random.choice(wd)
ls=len(wr)*['_']
jn=' '.join(ls)
le=0
dp=[]
print(jn)
while le<len(wr) :
    l1=input('guess a letter')
    
    if l1 in wr :
        if wr.count(l1)==1:
            rel=wr.find(l1)
            ls[rel]=l1
            jn=' '.join(ls)
        if  wr.count(l1)>=2:
            if l1 not in dp:
                rel=wr.find(l1)
                ls[rel]=l1
                jn=' '.join(ls)
                dp.append(l1)
            elif l1 in dp:
                rel=wr.rfind(l1)
                ls[rel]=l1
                jn=' '.join(ls)
                
            
        print(jn)
        
        print()
        
        
    elif l1 not in wr:
        if le==0:
            print('    _     ')
            print('     |    ')
            print('Your guess:',jn)
        elif le==1:
            print('    _     ')
            print('     |    ')
            print('     O     ')
            print('Your guess:',jn)
        elif le==2:
            print('    _     ')
            print('     |    ')
            print('     O     ')
            print('     |     ')
            print('Your guess:',jn)
        elif le==3:
            print('    _     ')
            print('     |    ')
            print('     O     ')
            print('     |\     ')
            print('Your guess:',jn)
        elif le==4:
            print('    _     ')
            print('     |    ')
            print('     O     ')
            print('    /|\     ')
            print('Your guess:',jn)
        elif le==5:
           print('    _     ')
           print('     |    ')
           print('     O ')
           print('    /|\     ')
           print('     |    ')
           print('Your guess:',jn)
        elif le==6:
           print('    _     ')
           print('     |    ')
           print('     O     ')
           print('    /|\     ')
           print('     |    ')
           print('    /      ')
           print('Your guess:',jn)
        elif le==7:
           print('    _     ')
           print('     |    ')
           print('     O     ')
           print('    /|\     ')
           print('     |    ')
           print('    / \    ')
           print('Your guess:',jn)
        elif le==8:
           print('Your guess:',jn)
           print('You Lost')
           break
        le+=1
    if ls==list(wr) :
        print('You Won')
        break
    print()

print('The word is', wr)




    
  
    
    

