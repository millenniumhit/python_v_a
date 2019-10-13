import itertools
from pprint import pprint
import socket
f = open('test_file.txt', 'r')
spisok=list()
for line in f:
    if len(line.strip())>0:
        spisok.append(line.strip())
new_spis = [el for el, _ in itertools.groupby(spisok)]
#print(new_spis)
#pprint(new_spis[2])
#print(socket.gethostbyname(new_spis[5])[1])
#pprint(socket.getaddrinfo(new_spis[5], 80)[0])

spisok_ip = [[range(1)], [range(len(new_spis)-1)]]
i = 0
for ip in new_spis:
    spisok_ip[0][i] = socket.gethostbyname_ex(ip)[0]
    spisok_ip[1][i] = socket.gethostbyname_ex(ip)[2]
    i += 1
#spisok_ip_n = list()
#spisok_ip_n = spisok_ip[0], spisok_ip[2]
pprint(spisok_ip)
