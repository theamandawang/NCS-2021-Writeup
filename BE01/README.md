# BE01
#### 100pts
## Briefing: Download the file and find a way to get the flag.

# My Solution

I have a Windows machine, and booting the VM for linux is usually a hassle, so I first took a look at [chicken.pdf](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/BE01/chicken.pdf) using Notepad.

The first couple of lines are as follows:
> %PDF-1.4
> %âãÏÓ
> 1 0 obj
> <<
> /Filter /FlateDecode
> /Length 550559
> \>\>
> stream
> PK
>      °}ZQ r@azf zf    egg.zipPK
>      ¨}ZQš¦]?Þe Þe    chicken.zipPK
>      œ}ZQý4Ï:Je Je    egg.zipPK
>      •}ZQ}»å®d ®d    chicken.zipPK 

Looking at this, it seems like there are hidden files within [chicken.pdf](https://github.com/theamandawang/NCS-2021-Writeup/blob/main/BE01/chicken.pdf). The perfect tool for this is [binwalk](https://tools.kali.org/forensics/binwalk#:~:text=Binwalk%20is%20a%20tool%20for,for%20the%20Unix%20file%20utility.) on Linux. 

I used
```
binwalk -Me chicken.pdf
```
After finding the hidden files, I traversed the directory and found the file *egg.pdf*

Opening it, you will see the flag.

>Flag:
>wh1ch_came_f1rst?
