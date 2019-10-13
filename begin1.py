import itertools
f = open('test_file.txt', 'r')
spisok=list()
for line in f:
    spisok.append(line)
new_spis = [el for el, _ in itertools.groupby(spisok)]
print(new_spis)
