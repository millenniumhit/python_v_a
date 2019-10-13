import itertools
from pprint import pprint
import socket
from numpy import ndarray
f = open('test_file.txt', 'r')
spisok=list()
for line in f:
    if len(line.strip())>0:
        spisok.append(line.strip())
new_spis = [el for el, _ in itertools.groupby(spisok)]

spisok_ip = list()
i = 0
for ip in new_spis:
    if i < 10: #чтобы не падало на крокозябрах
        for ip4 in socket.gethostbyname_ex(ip)[2]:
            spisok_ip.append([socket.gethostbyname_ex(ip)[0], socket.gethostbyname_ex(ip4)[0]])
            i += 1 #и это тоже убрать
pprint(spisok_ip)
