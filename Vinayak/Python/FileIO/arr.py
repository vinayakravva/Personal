
import array as arr
numarr=arr.array('i',[10,5,67,88,98,34])
f1=open('arr.txt','w')
for i in numarr:
    f1.write(str(i))
    
f1.close()

f2=open('arr.txt','r')
l=f2.read().split()
print(l)
for i in l:
    print(i)
