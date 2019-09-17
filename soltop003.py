
import struct
import datetime
import glob
import csv
import json
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError


class influxManager(object):
    def __init__(self,config = {}):


        print('DB config',config)
        self._dbuser = config.get('USER','tgdscm41')
        self._dbpasswd = config.get('PASSWORD','Swisscom10')
        self._dbname = config.get('DBNAME','soltop')
        self._dbhost = config.get('HOST','192.168.20.205')
        self._dbport = config.get('PORT',8086)

        self._log = None

        self._db = None

    def connectdb(self):
        result =  False
        try:
            self._db  = InfluxDBClient(self._dbhost,self._dbport,self._dbuser,self._dbpasswd,self._dbname)
            self._db.create_database(self._dbname)
         #   print('DBTEST',self._db.create_database(self._dbname))
            print('Connect')
            result = True
        except:
            #print ('FAiler')
            self._log.critical('Cannot connect to DB')
            result = False
        return result

    def createdb(self):
        self.connectdb()
       # print("create db",self._dbname)
        self._log.debug('Create DB %s',self._dbname)
        self._db.create_database(self._dbname)

        #        self._db.create_retention_policy('policy','INF', 'INF', default= True)
        return True

    def writedb(self,str_data):
       # print('data',type(str_data),type(json.loads(str_data)))
       # cont= []
       # cont.append(str_data)
        print(self._db.write_points(str_data))
        return True

    def querydb(self, query_str):
        value = self._db.query('SELECT'+ self._dbname + 'from' + query_str)
        return value

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

    db = influxManager()
    db.connectdb()

    filename = './190625.DLF'
    write = 0

    for filename in glob.glob('./LOG/19*.DLF'):

        with open(filename, "rb") as f:
            header = f.read(222)
            # print(header)
            header = soltropHeader(header)
            #  print(header.printStore())
            # print(header.verion())
            # print(header.messure())
            s = 0
            series = []
            for y in range(0, header.messure()):
                #  while True:
                #     s = s+1
                content = f.read(56)
                if not content or len(content) < 56:
                    print('file end')
                    break
                # print(content)
                x = soltropStore(content)


                pointValues = {
                   # "time": x.date(),
                    #              "measurement": row.get('EventName'),
                    "measurement": 'soltop',
                    'tags': {
                        #                'value': row.get('Value'),
                        'type': 'SR04',
                        'location': 'Muenchenbuchsee',
                        'street': 'parkweg',
                        'streetnumber': 49,
                         'serialnumber': '0815'
                    },
                    'time': x.date(),
                    'fields': {
                        'S1': x.s1(),
                        'S2': x.s2(),
                        'S3': x.s3(),
                        'S4': x.s4(),
                        'S5': x.s5(),
                        'S6': x.s6(),
                        'S7': x.s7(),
                        'analogIn1': x.analogIn1(),
                        'analogIn2': x.analogIn2(),
                        'analogIn3': x.analogIn3(),
                        'grundfos': x.grundfos(),
                        'r1':x.r1(),
                        'r2': x.r2(),
                        'r3': x.r3(),
                        'r4': x.r4(),
                        'relais': x.relais(),
                        'pumpart1': x.pumpart1(),
                        'analogOut1':x.analogOut1(),
                        'pumpart2' : x.pumpart2(),
                        'analogOut2' : x.analogOut2(),
                        'energie': x.energie(),
                        'betriebsstd1': x.betriebh1(),
                        'betriebsstd2' : x.betriebh2(),
                        'betriebsstd3' : x.betriebh3(),
                        'betriebsstd4' : x.betriebh4()
                    }
                }
                series.append(pointValues)

           # print(series)
            db.writedb(series)
            write = write + 1
            print(filename,write,len(series))

