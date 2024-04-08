# x=int(input("enter first no"))

# y=int(input("enter 2nd no"))
# z=x+y
# print(z)
# print('Deepika')
# print(7)

# ch=input('enter the char')[1]
# print(ch)
# import sys
# x=int(sys.argv[0])
# y=int(sys.argv[1])
# z=x+y
# print(z)

# x=8
# r=x%2
# if(r==0):
#     print("Even")
# if(r==1):
#     print("odd")    

# x=int(input("enter the number"))
# if(x>0):
#     print("positive")
# elif(x<0):
#     print("Negative")
# else:
#     print("its zero")            


# for i in range(5):
#     if(i==3):
#         continue;
#     print("Deepika",i)
    
# patterns

i=1
while(i<=5):
    for j in range(i):
        print("*",end="")
    print('\n')
    i+=1    

# for each

nums=[12,15,18,21,26]
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")