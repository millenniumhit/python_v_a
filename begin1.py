import itertools
from pprint import pprint
import socket
#from numpy import ndarray
f = open('test_file.txt', 'r')
spisok=list()
for line in f:
    if len(line.strip())>0:
        spisok.append(line.strip())
new_spis = [el for el, _ in itertools.groupby(spisok)]

spisok_ip = {}
for ip in new_spis:
    try:  
        spisok_ip[socket.gethostbyname_ex(ip)[0]] = (socket.gethostbyname_ex(ip)[2])
    except Exception:
        spisok_ip[ip] = (None)
print(spisok_ip)

