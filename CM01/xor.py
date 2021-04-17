import numpy as np

f = open('cm 01 frame.txt', 'r')
f2 = open('cm01 code qr.txt', 'r')
f3 = open('xored.txt', 'w+')

i = 0
for x in f:
    for y in x:
        i += 1
    print(i)
    break
##file length = 301 by 301 square


array = np.zeros((301, 301))


code = np.zeros((301,301))
count = 0
count2 = 0
for line in f2:
    count2 = 0
    for x in line:
        if(x == '0'):
            code[count][count2] = 0
        else:
            code[count][count2]  = 1
        count2 += 1
    count += 1
print(code) 

frame = np.zeros((301,301))
count = 0
count2 = 0
for line in f:
    count2 = 0
    for x in line:
        if(x == '0'):
            frame[count][count2] = 0
        else:
            frame[count][count2]  = 1
        count2 += 1
    count += 1
print(frame) 

for x in range(301):
    for y in range(301):
        if code[x][y] != frame[x][y]:
            array[x][y] = 1

for x in range(301):
    f3.write(str(array[x]) + '\n')
