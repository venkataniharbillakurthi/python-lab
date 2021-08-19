import random
r=random.randint(1,10)
while True:
    guess=int(input('Enter the number:'))
    if r==guess:
        print('congrat!your guess correct:')
        break
    else:
        print('sorry!try again')
    
    
 Enter the number:7
sorry!try again
