# Intro to Reversing with radare2

## Introduction
This session is intended to go over types of reverse engineering and to introduce basic methods for both static analysis and dynamic analysis.  In conjunction, we will take a look at the radare2 disassembler/debugger and software suite as a viable alternative to the proprietary and expensive IDAPro.  
## Tasks to Complete Before the Practice

1. Download and install [radare2:](radare.org/r/down.html) 

## Pre-Reading Material

* Look over our intro to x86 [slides](https://github.com/MCPA/Team-Challenges/raw/master/pwnable/intro-to-x86/intro-to-x86.ppt.pdf) or [video](https://youtu.be/PkLkOAqmNkI?t=19m40s)

## Agenda

1. Introduction
2. Why reverse?
    * Not just for crackme's and breaking stuff
    * Exploring undocumented API's
    * Hooking, extend functionality or change behavior, or debugging issues in closed source software
    * Static vs dynamic analysis 
3. Diving into r2
    * Quick glance: suite utilities
    * CMD line mode
      -The "abc's"
      -Basic patch cycle: a, p, w
    * Visual mode
    * Debugging with r2
4. Demos/practice 
5. Further capabilities: ESIL, GUIs, desired capabilites 
6. Questions
7. References

## Summary

##### What is radare2? Why should we use it?  
radare2 is a portable and customizable reversing framework - it can run on very many platforms, including phones, supports a ridiculous number of target architectures, and can be extended with multiple language bindings.  See the comparison table linked below to compare with IDA and Hopper. Oh, and it's free (as in beer and freedom). 
##### What should you learn from this practice session?
This practice session is intended to introduce reverse engineering in general, a step back from our specific context of security; talk about for what it can be applied, and why it's such an awesome practice to pursue. We will go over static and dynamic (debugging) techniques to understanding both labeled and stripped binaries.   

## Useful Links

[free reversing ebook](beginners.re/RE4B-EN.pdf)

[radare2 intro ebook](https://radare.gitbooks.io/radare2book/content/)

[handy cheatsheet](https://github.com/pwntester/cheatsheets/blob/master/radare2.md)

[migration from gdb/ida](https://github.com/radare/radare2/wiki/Migration-from-ida-or-gdb)

[YouTube video from this practice](https://youtu.be/KCuZ9Ig_boY)

-----

## Endnotes
