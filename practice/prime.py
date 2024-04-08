import math
x=int(input("enter the number"))
for i in range(2,int(math.sqrt(x))):
    if(x%i==0):
        print("Not prime")
        break
else:
    print("Prime")    

# effient way is    sqrt(n);