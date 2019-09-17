
import struct
import datetime
import glob
import csv


class soltropHeader(object):

    def __init__(self,header):

        self._struct = "l109h"

        self._size= struct.calcsize(self._struct)
     #   print(self._size,len(header))
        self._store = struct.unpack(self._struct,header)

    def printStore(self):
        return self._store

    def verion(self):
        return self._store[0]

    def messure(self):
        return self._store[9]

class soltropStore(object):

    def __init__(self,chunk):
        self._data = chunk
       # self._struct = "hhhhhhhhhhhhhhhhhhhhhhhhhh"
      #  print(chunk)
       # print('xxx',struct.unpack_from('H',chunk,offset=0))

        #print(hex(struct.unpack_from('L', chunk, offset=2)[0]))

       # self._date = struct.unpack_from('L', chunk, offset=2)[0]
       # print('fff',self._date)

       # xxx= datetime.datetime.utcfromtimestamp(self._date) #.strftime('%Y-%m-%d %H:%M:%S')
        #print(xxx)
        #    print(item)
        #vvv = xxx.replace(year=xxx.year+40)
        #print(vvv)
        self._struct = "hI24h"
       # self._struct = "hI26i"
        self._size= struct.calcsize(self._struct)
      #  print(self._size,len(chunk))
        self._store = struct.unpack_from(self._struct,chunk,offset=0)
     #   print(self._store)

    def memsize(self):
        print(self._size)
        return self._size

    def printStore(self):
        print(self._store)
        return self._store

    def _getByte(self,type,offset):
     #   print('debug',struct.unpack_from(type ,self._data,offset))
        return(struct.unpack_from(type ,self._data,offset))[0]

    def date(self):
        _data = self._getByte('L',2)
    #    print( _date)
        dateObj = datetime.datetime.utcfromtimestamp(_data)
        return dateObj.replace(year=dateObj.year + 40).strftime('%Y-%m-%d %H:%M:%S')

    def s1(self):
        _value =  self._getByte('h',6)*0.1
        return float("{0:.1f}".format(_value))

    def s2(self):
        _value =  self._getByte('h',8)*0.1
        return float("{0:.1f}".format(_value))

    def s3(self):
        _value =  self._getByte('h',10)*0.1
        return float("{0:.1f}".format(_value))

    def s4(self):
        _value =  self._getByte('h',12)*0.1
        return float("{0:.1f}".format(_value))

    def s5(self):
        _value =  self._getByte('h',14)*0.1
        return float("{0:.1f}".format(_value))

    def s6(self):
        _value =  self._getByte('h',16)*0.1
        return float("{0:.1f}".format(_value))

    def s7(self):
        _value =  self._getByte('h',18)*0.1
        return float("{0:.1f}".format(_value))

    def analogIn1(self):
        _value =  self._getByte('h',20)
        return float("{0:.1f}".format(_value))

    def analogIn2(self):
        _value =  self._getByte('h',22)
        return float("{0:.1f}".format(_value))

    def analogIn3(self):
        _value =  self._getByte('h',24)
        return float("{0:.1f}".format(_value))

    def grundfos(self):
        _value =  self._getByte('h',26)
        return float("{0:.1f}".format(_value))

    def r1(self):
        _value =  self._getByte('h',28)
        return float("{0:.1f}".format(_value))

    def r2(self):
        _value =  self._getByte('h',30)
        return float("{0:.1f}".format(_value))

    def r3(self):
        _value =  self._getByte('h',32)
        return float("{0:.1f}".format(_value))

    def r4(self):
        _value =  self._getByte('h',34)
        return float("{0:.1f}".format(_value))

    def relais(self):
        _value = self._getByte('h', 36)
        return float("{0:.1f}".format(_value))

    def pumpart1(self):
        _value = self._getByte('h', 38)
        return float("{0:.1f}".format(_value))

    def analogOut1(self):
        _value = self._getByte('h', 40)
        return float("{0:.1f}".format(_value))

    def pumpart2(self):
        _value = self._getByte('h', 42)
        return float("{0:.1f}".format(_value))

    def analogOut2(self):
        _value = self._getByte('h', 44)
        return float("{0:.1f}".format(_value))

    def energie(self):
        _value = self._getByte('h', 46)
        return float("{0:.1f}".format(_value))

    def betriebh1(self):
        _value = self._getByte('h', 48)
        return float("{0:.1f}".format(_value))

    def betriebh2(self):
        _value = self._getByte('h', 50)
        return float("{0:.1f}".format(_value))

    def betriebh3(self):
        _value = self._getByte('h', 52)
        return float("{0:.1f}".format(_value))

    def betriebh4(self):
        _value = self._getByte('h', 54)
        return float("{0:.1f}".format(_value))


if __name__ == "__main__":

    import csv

    with open('measurement.csv', mode='w',newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for filename in glob.glob('./LOG/*.DLF'):
            with open(filename, "rb") as f:
                header = f.read(222)
               # print(header)
                header = soltropHeader(header)
              #  print(header.printStore())
               # print(header.verion())
                #print(header.messure())
                s = 0
                for y in range(0,header.messure()):
              #  while True:
               #     s = s+1
                    content = f.read(56)
                    if not content or len(content) < 56:
                        print('file end')
                        break
                #print(content)
                    x = soltropStore(content)
                    #x.memsize()
                   # x.printStore()
                    data_row = [x.date(),x.s1(),x.s2(),x.s3(),x.s4(),x.s5(),x.s6(),x.s7(),x.analogIn1(),x.analogIn2(),x.analogIn3(),x.grundfos(),x.r1(),x.r2(),x.r3(),x.r4(),x.relais(),x.pumpart1(),x.analogOut1(),x.pumpart2(),x.analogOut2(),x.energie(),x.betriebh1(),x.betriebh2(),x.betriebh3(),x.betriebh4(),y]
                  #  print(data_row)
                    csv_writer.writerow(data_row)


        csv_file.close()
