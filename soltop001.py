#http://code.activestate.com/recipes/577610-decoding-binary-files/?in=user-4175703
import binascii
import hexdump
import struct

with open("./190625.DLF", "rb") as f:
    header = f.read(222)
    print(header)
    print(binascii.hexlify(header))
   # str=""
   # for ch in header:
    #    str += hex(ord(ch))+" "
    #print (str)
    print(hexdump.dump(header, size=2, sep=' '))
    #content = f.read(112)
    #print(hexdump.dump(content, size=2, sep=' '))

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print(struct.unpack('h',value)[0])

    typeSize = struct.calcsize('I')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Date',struct.unpack('I',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('S1',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('S2',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('S3',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('S4',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('S5',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('S6',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('S7',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Analog1',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Analog2',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Analog3',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Grundfos',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('R1',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('R2',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('R3',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('R4',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Relais',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Pumpenart 1',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Analog out1',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Pumpenart 2',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Analog out2',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Energieertrag',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Betriebsstunden 1',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Betriebsstunden 2',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Betriebsstunden 3',struct.unpack('h',value)[0])

    typeSize = struct.calcsize('h')
    print('typeSize',typeSize)
    value = f.read(typeSize)
    print('value',value)
    print('value1',binascii.hexlify(value))
    if typeSize!=len(value):
        print('error')
    print('Betriebsstunden 4',struct.unpack('h',value)[0])


   #print('unknonw',content.read('uint8'))
    #bdata = []
   # print('unkonwn',bdata.append(struct.unpack('b',content[4])))

   # hex_content= header.encode('hex')
    #print('cc',hex_content)
   # print(" ".join(hex(ord(n)) for n in header))
   #while byte != b"":
    #    # Do stuff with byte.
     #   byte = f.read(208)
      #  print(byte)

f.close()