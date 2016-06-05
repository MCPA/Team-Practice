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
2. Download the vulnerable binary and create a flag to be read on your local VM.
3. Install a disassembler, such as [IDA free 5.0](https://clickhere.com), [Hopper](https://clickhere.com), [Binary Ninja](https://binary.ninja), or use [radare2](https://clickhere.com) which is included with Kali Linux.

## Pre-Reading Material

* Read the primer on Smashing the Stack.
* Read the primer on Return-Oriented-Programming.
* Read about modern protections used to protect binaries from exploitation.

## Agenda

1. Introduction
2. Background Noise
    * x64 Registers and Calling Conventions
    * x64 Instructions & Intel Syntax
3. What is ROP?
    * Trampolines
    * Return-2-Libc
    * Gadgets
    * ROP Chaining
4. Minimum Requirements
5. Walkthrough & Live Demo
6. Questions
7. References

## Summary

What is Return-Oriented-Programming?   
Why is it useful?   
What do I hope someone will learn from attending this practice session?

## Useful Links

The recorded practice session can be found [[here]()]  
Practice material can be found [[here]()]  
Pre-reading material can be found [[here]()]

-----

## Endnotes
