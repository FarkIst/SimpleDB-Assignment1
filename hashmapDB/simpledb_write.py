import sys
import hashMap
import random
import string

_hashMap = hashMap.getHash()

file = open("database", "wb")


def toBytes(string):
    return bytes(string + '\n', 'utf-8')

def add(key, value):
    bytesData = toBytes(key + ',' + value)
    file.write(bytesData)
    _hashMap[key] = _hashMap[sorted(_hashMap.keys())[-1]] + sys.getsizeof(bytesData)

def generateData():
    chars = string.ascii_letters + string.digits
    return ''.join(random.sample(chars, 10))

list_len = 10
randomstr = {el: generateData() for el in range(list_len)}
randomstr

i = 0

for i in range(len(randomstr)):
    k = str(i)
    v = str(randomstr[i])
    add(k, v)
file.close()