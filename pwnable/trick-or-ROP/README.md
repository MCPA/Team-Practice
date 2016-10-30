# Trick-or-ROP (Beating dmail)

## Introduction
This practice session is intended to be a live demonstration coupled with a follow-along style walkthrough of ROP building and exploitation. A basic understanding of x86/x64 assembly programming helps to understand material that is not specifically discussed such as: understanding of the stack and terminology such as: registers, stack frames, and the heap. The practice will be discussed with the understanding that participants have completed all of the pre-reading ahead of time and prepared a Virtual Machine (VM) with the pre-requisites to follow-along during the live practice session.

## Tasks to Complete Before the Practice

1. Download the most recent version of Kali Linux:
  * Install GDB Peda
  * Install pwnlib
  * Install ltrace
  * Install strace
  * Install capstone & [ROPgadget](https://github.com/JonathanSalwan/ROPgadget)
2. Download the vulnerable [binary](dmail) and create a flag to be read on your local VM.
3. Install a disassembler, such as [IDA free 5.0](https://www.hex-rays.com/products/ida/support/download.shtml), [Hopper](www.hopperapp.com), [Binary Ninja](https://binary.ninja), or use [radare2](https://github.com/radare/radare2) which is included with Kali Linux.
4. Install a debugger of your choice or use [GDB-PEDA](https://github.com/longld/peda)

## Pre-Reading Material

* Look over our intro to x86 [slides](https://github.com/MCPA/Team-Challenges/raw/master/pwnable/intro-to-x86/intro-to-x86.ppt.pdf) or [video](https://youtu.be/PkLkOAqmNkI?t=19m40s)
* Look over our intro to ROP [[here](https://github.com/MCPA/Team-Practice/raw/master/pwnable/return-oriented-programming/intro-to-ROP.pdf)]

## Agenda

1. Introduction
2. Starting Points
    * Basic information (file, strings, flawfinder, checksec)
    * What are the observable output and input parameters?
    * What are some potential vulnerabilities to begin checking?
3. Dynamic Analysis
    * Use gdb and python to our advantage
    * Automate some of the tasks
    * Update as we go along
4. Chaining Vulnerabilities
    * What information leaks do we have?
    * Tricking Malloc
    * Some light ROP
5. Profit!
6. Questions
7. References

## Summary

##### What is Return-Oriented-Programming and why is it useful?
Return-Oriented-Programming (ROP) is a type of exploitation techniques which bypasses many protection features afforded by both the OS and compilation techniques. ROP has three fairly common uses and techniques by which is gains it's name from: 1) ROP Chaining; 2) Return to Libc (Ret-2-libc); and 3) Trampolines. It does this by using executable pieces of code that are already present in the vulnerable program. Through this technique it is possible to not only redirect control of the program but execute arbitrary operations on the targeted host machine.

##### What should you learn from this practice session?
This practice sessions is geared towards reviewing a past pwnable type of Jeopardy challenge during a BlazeCTF 2016. Although our team members were unable to beat dmail at the time, we did reach some of the same conclusions that other teams that did beat the challenge found. As a result, participants should learn new techniques and methods in which to find and exploit CTF challenges for the future.

## Useful Links

The recorded practice session can be found [[here](https://youtu.be/wIPJ4U4K0nU)]  
Practice material can be found [[here](https://github.com/MCPA/Team-Challenges/tree/master/pwnable/trick-or-rop)]  
Radare2 Intro Video [[here](https://youtu.be/KCuZ9Ig_boY)]  
Solution Writeup [[here](https://0xabe.io/ctf/exploit/2016/04/24/BlazeCTF-dmail.html)]  
Another Solution [[here](http://www.hamidx9.ir/solutions/2016/blazectf/dmail/sol.py)]  

-----

## Endnotes
[Understanding glibc malloc](https://sploitfun.wordpress.com/2015/02/10/understanding-glibc-malloc/)  
[Finding the Magic Gadget Shell](https://0xabe.io/howto/exploit/2016/03/30/Radare2-of-the-Lost-Magic-Gadget.html)  
