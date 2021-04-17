# CM01
  #### 250pts
## Briefing: Download the file and find a way to get the flag.

# My Solution
![frame.png](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/CM01/frame.png)

Scanning the QR code frame.png with my phone camera, I got the message:
> Hey, I've put the flag into the other file using the same trick we always use. You know what to do. :)

Now, looking at the other "QR code" they give us, code.png, we can scan it and it does nothing.


![code.png](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/CM01/code.png)


Something interesting about QR codes is that you can perceive the black and white pixels as 0s or 1s. Essentially QR codes are "binary" images.

Based on this observation, I deduced that XOR was the most likely way to decrypt the QR code code.png.

I used https://www.dcode.fr/binary-image to help me convert the QR codes to binary text files.

These text files are [cm 01 frame.txt](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/CM01/cm%2001%20frame.txt) and [cm 01 code qr.txt](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/CM01/cm01%20code%20qr.txt)

Now that we have these QR codes represented in text form, we can XOR each pixel.

I ended up using the numpy library to work with matrices so the new XORed text file would be easier to create.``
import numpy as np
```python
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
```

After creating a new file with [xored.txt](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/CM01/xored.txt), we can put that back into [Dcode.fr](https://www.dcode.fr/binary-image) to create a QR code out of the binary data.

Finally, we end up with the [xored QR code](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/CM01/xored.png)

Scan it:
![xored code](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/CM01/xored.png)

And we get:
> FLAG: A_Code_For_A_Code
