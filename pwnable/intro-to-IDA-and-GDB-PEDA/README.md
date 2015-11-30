Introduction to IDA 5.0 and GDB Python Exploit Development Assistance (PEDA)
======

### Description

This team practice was held on December 12th (2030 via Google Hangouts - I'll email and post the link about 10 minutes prior). Ben Smith is going to be leading this practice. It will focus on providing an introduction to using IDA v5.0, IDA Pro Freeware, and GDB-PEDA, an interactive GDB Python Exploit Environment. If you didn't sit in our last practice on 21 November 2015, you may want to go back and review the [video](https://youtu.be/PkLkOAqmNkI?t=17m50s). The practice will make more sense if you have a basic knowledge of the stack and assembly terminology. There are also a few tasks to complete before the practice, because this session will be very hands-on:

### Tasks to complete before watching the practice:
Ensure you have done the following PRIOR to practice.  We will not wait for you to begin.
```
Have linux running in a VM on a windows box, I'm running the most recent Kali VM image, Kali 1.1.0 VM64
update and upgrade your image.
Ensure you are able to run 32bit ELFs if you are on a 64bit linux
newer linux: sudo apt-get install lib32z1 lib32ncurses5 lib32bz2-1.0
older linux: sudo apt-get install ia32-libs
download and install ida-pro 5.0 (this is what I'll be using) on your windows box
download and install gdb-peda on your linux image (you are succesful if when you run gdb the prompt now says gdb-peda)
```

You are mission complete if you can open your ELF file (re_100_final) in IDA-PRO and if you can attach it to GDB and when you type "run" it asks you to enter in the "secret flag"

All the class material can be found [here](https://goo.gl/8lu5V7).
