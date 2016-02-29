# CTF Practice - 20 February 2016

## Introduction
----
Systemshock was a challenge from the CodeGate General CTF in 2015. It consists of a binary called shock with ```setuid``` permissions. This short write-up is based on a write-up completed by [smokeleeteveryday](https://github.com/smokeleeteveryday/CTF_WRITEUPS/tree/master/2015/CODEGATE/pwnable/systemshock). The session was recorded and posted on [youtube](https://youtu.be/xBcNWbiVEzk). A second recording will be posted demonstrating the exploit since it was not demonstrated during the live on-air hangout.

## Setup

In order to practice with this challenge you will need the binary from [here](shock). The binary is stripped, and as such, I highly recommend using a more robust disassembler than [objdump](https://sourceware.org/binutils/docs/binutils/objdump.html), such as [hopper](www.hopperapp.com) or [IDA Free](https://www.hex-rays.com/products/ida/support/download_freeware.shtml) and configuring [GDB PEDA](https://raw.githubusercontent.com/tentpegbob/bearded-cyril/master/tool-repo.sh). Finally, create a small text file (```echo 'I"m not the flag you are looking for\!' > flag```) which you want to be able to open after exploiting the shock binary.

## Solving the Challenge

A breakdown of the steps necessary to finish the shock challenge from CodeGate CTF 2015:
* Bypass the security features of the binary (stack canary and non-executable stack)
* Make use of a ```strcat``` vulnerability [\[1\]](#endnote1)
* Determine the distance between the buffer and the stack
    * Understand where and why the program crashes
    * Take advantage of ```system``` which is already resident inside the vulnerable program

### A detailed solution write-up is provided by [smokeleeteveryday](https://github.com/smokeleeteveryday/CTF_WRITEUPS/tree/master/2015/CODEGATE/pwnable/systemshock).


----
## Endnotes
<a name="endnote1">[1]</a>: ```strcat``` appends a copy of a source string into a destination string. It is dependent on the programmer to ensure that the destination array is large enough to contain the concatenated resulting string. The return value is the destination string.
