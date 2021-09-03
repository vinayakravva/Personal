num=int(input("ENter number:"))

def sum(num):
    if(num>0):
        add=num+sum(num-1)
    else:
        return 0
    return add
print(sum(num))
        



