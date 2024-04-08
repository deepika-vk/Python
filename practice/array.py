from array import *
vals=array('i',[5,6,7,98,8])
vals.reverse()
print(vals)
print(vals.buffer_info())

vals.reverse()

newarray=array(vals.typecode,(a*a for a in vals))
for i in newarray:
    print(i)