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
