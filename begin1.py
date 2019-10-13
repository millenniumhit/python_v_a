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
pprint(socket.gethostbyname_ex(new_spis[5]))
#pprint(new_spis[2])
#print(socket.gethostbyname(new_spis[5])[1])
#pprint(socket.getaddrinfo(new_spis[5], 80)[0])

