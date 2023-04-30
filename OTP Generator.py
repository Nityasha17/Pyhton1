import random

ans=random.random()
print(ans)
n=int(input('enter no. of digits'))
ans=str(ans)
ans=ans[2:n+2]
print('OTP is =',ans)
