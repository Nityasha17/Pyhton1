import random
print('WELCOME TO GUESS THE NUMBER GAME')
print()


print('1=EASY\n2=MEDIUM\n3=ADVANCE')

level=int(input('enter the level'))

if level==1:
    start=int(input('enter start number '))
    end=int(input('enter last number '))
    c=end-start-2
    ans=random.randint(start,end)

elif level==2:
    start=int(input('enter start number '))
    end=int(input('enter last number '))
    c=int(input('enter no. of chance '))
    ans=random.randint(start,end)

elif level==3:
    start=1
    end=100
    c=10
    ans=random.randint(start,end)

print('\n\n\n')

b=0
while((c-b)>0):
    if(c-b)!=c:
        print('Remaining choices:',c-b)
    i=int(input('ENTER UR CHOICE-->'))
    if i==ans:
        print("u win\n")

        print('best score=',c*100)
        print('ur score is=',(c-b)*100)
        break
    elif i>ans:
        print('grater\n')
    elif i<ans:
        print('lesser\n')
    else:
        print('invalid input\n')
    b+=1
else:
    print('BETTER LUCK NEXT TIME')
    print('THE NUMBER GUESSED BY ME WAS ',ans)
