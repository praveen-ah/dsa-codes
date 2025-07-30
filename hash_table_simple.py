hashTable = [[] for _ in range(10)]
def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1
    while not checkPrime(n):
        n += 2
    return n

# print(getPrime(25))

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    found = False
    for i, kv in enumerate(hashTable[index]):
        if kv[0] == key:
            hashTable[index][i] = (key, data)
            found = True
            break
    if not found:
        hashTable[index].append((key, data))

def removeData(key):
    index = hashFunction(key)
    for i, kv in enumerate(hashTable[index]):
        if kv[0] == key:
            del hashTable[index][i]
            break

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")
insertData(213, "orange")

print(hashTable)

removeData(123)

print(hashTable)

