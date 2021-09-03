
hashtable = [[]for  _ in range(int(input("Enter no.of. Table : ")))]

def insert(hashtable,key,value):
    hash_value = hashing(key)
    hashtable[hash_value].append(value)

def hashing(key):
    return key % len(hashtable)

def display(hastable):
    for i in range(len(hashtable)):
        print(i,end = " ")
        for j in (hastable[i]):
            print("-----> ",end = " ")
            print(j,end=" ")
        print()





while(True):
    print("""
    1 -- Insert the data 
    2 -- display
    3 -- Exit
    """)
    print()
    ch=int(input("Enter the choice : "))

    if ch == 1:
        value = int(input("Enter the numbers to insert : "))
        key = value
        insert(hashtable,key,value)

    if ch == 2:
        display((hashtable))

    if ch == 3:
        exit() 