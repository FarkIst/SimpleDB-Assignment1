import sys
import os.path

def getHash():
        if os.stat("database").st_size==0:
                return {}

        file = open("database", "rb")

        data = file.read()

        data = data.decode('utf-8').split('\n')
        data.pop()

        hash = {}
        byte_offset = 0

        for pair in data:
                key = pair.split(',', 1)[0]
                hash[key] = byte_offset
                byte_offset = byte_offset + len(pair) + 1
                
        
        file.close()
        return hash
