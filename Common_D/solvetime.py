import time
import datetime

s = '2017-06-16T20:22:12'
a = time.strptime(s,'%Y-%m-%dT%H:%M:%S')
d = datetime.datetime(*a[:5])
