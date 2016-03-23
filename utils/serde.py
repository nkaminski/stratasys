#!/usr/bin/env python
import sys, os
import binascii

def dataPack(bindata):
    st = binascii.hexlify(bindata)
    st2 = ""
    for i, c in enumerate(st):
        st2 += c
        if(i % 2 == 1):
            st2 += ' '
    print(str(len(st2)) + ' bytes packed')
    return st2

def dataUnpack(st):
    st = st.replace(' ','').strip()
    bd = binascii.unhexlify(st)
    print(str(len(st)) + ' non-whitespace characters decoded')
    return bd

if __name__ == "__main__":
    if(sys.argv[1] == 'unpack'):
        print("Unpacking material EEPROM data")
        with open(sys.argv[2],"r") as fp:
            st = fp.read()
            wp = open(sys.argv[3],'wb')
            outData = dataUnpack(st)
            wp.write(outData)
            wp.close()
    elif(sys.argv[1] == 'pack'):
        print("Packing material EEPROM data")
        with open(sys.argv[2],"rb") as fp:
            bd = fp.read()
            outData = dataPack(bd)
            wp = open(sys.argv[3],'w')
            wp.write(outData)
            wp.close()
    else:
        print("Usage: " + os.path.basename(__file__) + " <pack|unpack> <input file> <output file>")
