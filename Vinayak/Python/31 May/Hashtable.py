hashtable = [[] for _ in range(10)]

def insert(hastable,key,value):
    hash_value = hashing(key)
    hastable[hash_value].append(value)

def hashing(key):
    return key % len(hashtable)

def display(hashtable):
    for i in range(len(hashtable)):
        print(i , end = "")
        for j in hashtable[i]:
            print("------> " , end ="") 
            print(j , end = "")
        print()

insert(hashtable,123,223)
insert(hashtable,424,324)
insert(hashtable,525,625)
insert(hashtable,627,525)
insert(hashtable,25,28)
insert(hashtable,720,829)
insert(hashtable,25,25)
display(hashtable) 