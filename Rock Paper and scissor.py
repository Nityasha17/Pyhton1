import random
l=['1','2','3']
a=['','ROCK','PAPER','SCISSOR']
print('WELCOME TO ROCK PAPER SCISSOR GAME\n')
print('1-->ROCK\n2-->PAPER\n3-->SCISSOR')
while(True):
    ans=random.choice(l)
    x=a[int(ans)]
    i=input('\nENTER UR CHOICE ')
    print('\n')

    if i==ans:
        print('DRAW')
        print('U AND COMPUTER THINK SIMILAR')
    elif (i=='2' and ans=='1') or (i=='1' and ans=='3') or (i=='3' and ans=='2'):
        k=a[int(i)]
        print('u chose ',k)
        print('computer chose ',x)
        print("U WON")
        print()
    elif (ans=='2' and i=='1') or (ans=='1' and i=='3') or (ans=='3' and i=='2'):
        k=a[int(i)]
        print('computer chose ',x)
        print('u chose ',k)
        print("COMPUTER WON")
        print()
    else:
        print('INVALID INPUT')

    print('would u like to play again? ')
    s=input('if yes type y/Y) ')
    if s=='Y' or s=='y':
        continue
    else:
        break
