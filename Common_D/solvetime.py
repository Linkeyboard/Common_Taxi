import time
import datetime

s = '2017-06-16T20:22:02'
a = time.strptime(s,'%Y-%m-%dT%H:%M:%S')
d = datetime.datetime(*a[:5])
