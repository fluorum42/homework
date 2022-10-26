#Написать программу, которая выводит саму себя задом наперед

import sys
file_name = sys.argv[0]
f = open(file_name, 'r')
for line in f:
    print(line[::-1], end = '')
f.close()