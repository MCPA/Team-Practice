# Return-Oriented-Programming (ROP)

## Introduction
This practice session is intended to be a live demonstration coupled with a follow-along style walkthrough of ROP building and exploitation. But the practice session will include a light refresher on x64 assembly programming and an introduction to provide a background into what Return-Oriented-Programming actually is. This class assumes that the participants have at least a working knowledge of the C and x86/x64 assembly programming languages. Attendees need to have a basic understanding of the stack and terminology such as: registers, stack frames, and the heap. The practice will be discussed with the understanding that participants have completed all of the pre-reading ahead of time and prepared a Virtual Machine (VM) with the pre-requisites to follow-along during the live practice session.

## Tasks to Complete Before the Practice

1. Download the most recent version of Kali Linux:
  * Install GDB Peda
  * Install pwnlib
  * Install ltrace
  * Install strace
  * Install socat
  * Install capstone & [ROPgadget](https://github.com/JonathanSalwan/ROPgadget)
2. Download the vulnerable [binary](Simple_Calc) and create a flag to be read on your local VM.
3. Install a disassembler, such as [IDA free 5.0](https://www.hex-rays.com/products/ida/support/download.shtml), [Hopper](www.hopperapp.com), [Binary Ninja](https://binary.ninja), or use [radare2](https://github.com/radare/radare2) which is included with Kali Linux.
4. Install a debugger of your choice or use [GDB-PEDA](https://github.com/longld/peda)

## Pre-Reading Material

* Browse the primer on [Smashing the Stack by AlephOne](References/AlephOne-SmashingtheStack.pdf)
* Read the entire primer on Return-Oriented-Programming on [wikipedia](https://en.wikipedia.org/wiki/Return-oriented_programming).
* Look over our intro to x86 [slides](https://github.com/MCPA/Team-Challenges/raw/master/pwnable/intro-to-x86/intro-to-x86.ppt.pdf) or [video](https://youtu.be/PkLkOAqmNkI?t=19m40s)
* Look over slides 7-12 from a class made by Saumil Shah [[here](http://www.slideshare.net/saumilshah/dive-into-rop-a-quick-introduction-to-return-oriented-programming)]

## Agenda

1. Introduction
2. Background Noise
    * x64 Registers and Calling Conventions
    * x64 Instructions & Intel Syntax
    * Modern protections for preventing misuse
3. What is ROP?
    * Trampolines
    * Return-2-Libc
    * Gadgets
    * ROP Chaining
4. Watch ROP Work
5. Walkthrough & Live Demo
6. Questions
7. References

## Summary

##### What is Return-Oriented-Programming and why is it useful?    
Return-Oriented-Programming (ROP) is a type of exploitation techniques which bypasses many protection features afforded by both the OS and compilation techniques. ROP has three fairly common uses and techniques by which is gains it's name from: 1) ROP Chaining; 2) Return to Libc (Ret-2-libc); and 3) Trampolines. It does this by using executable pieces of code that are already present in the vulnerable program. Through this technique it is possible to not only redirect control of the program but execute arbitrary operations on the targeted host machine.

##### What should you learn from this practice session?
This practice sessions is geared towards teaching what is involved with building a ROP chain through not only providing a demonstration, but also lecture material for future referencing. It assumes that the attendee(s) at least have a basic understanding of assembly programming and stacks/stack frames. Following the practice session attendees should understand why ROP is possible and be able to build a ROP chain using instructions present in the program.

## Useful Links

The recorded practice session can be found [[here](https://youtu.be/3o4nO3WZn6o)]  
Practice material can be found [[here](https://github.com/MCPA/Team-Challenges/tree/master/pwnable/return-oriented-programming)]
Pre-reading material can be found [[here](https://github.com/MCPA/Team-Challenges/tree/master/pwnable/return-oriented-programming/References)]

-----

## Endnotes
