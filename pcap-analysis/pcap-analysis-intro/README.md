# Introduction

This practice session is designed to be a live demonstration with a follow-along style walkthrough of analyzing network packet captures.  

This class assumes that the participants have at least a basic working knowledge of the OSI model, sockets, fundamental transport protocols (i.e. TCP, UDP, ICMP), and basic application protocols (i.e. HTTP, SMTP, FTP).

We will discuss: PCAP file format, UI, process/analysis, techniques, and go over previous challenges.  The intent here is to provide some overview to those who are new, give some hints, and review real challenges without going too far over anyone's head, or not going far enough.

Ultimately, to be successful at packet analysis, you need to: understand what a packet capture is, understand the UI/tool you are working with, understand the protocols you are analyzing (this just come with experience, but know the basics), and be patient.

We will also walkthrough some specific packet capture analysis challenges from recent capture the flag challenges.  These challenges will cover obfuscating data in packet headers and payloads, extracting transferred files, and extracting payloads.

The practice will be discussed with the understanding that participants have completed all of the pre-reading ahead of time and prepared a system with the pre-requisites to follow-along during the live practice session.

We will probably not have enough time to cover everything.  The focus will be to walkthrough the challenges.  Please, review the challenge files before the practice.  And, if there is a particular PCAP you'd like to go over, make it known at the beginning of the practice.

# Tasks to Complete before the Practice Session

1. Download wireshark (and/or any other SW listed)
2. Download the challenge files
3. Review the reference material

# Download:
## Software
Wireshark <https://www.wireshark.org/download.html>  
NetworkMiner <http://www.netresec.com/?page=NetworkMiner>  
Netwitness (signup required) <https://emcinformation.com/283102/REG/.ashx?reg_src=web>  
Caploader <http://www.netresec.com/?page=CapLoader>  

<https://github.com/MCPA/Team-Challenges/blob/master/pcap-analysis/xor-data-challenge/Wireshark%20TCP%20Stream.png>  

## Challenge Files
SANS Boston Puzzle 1
SANS Boston Puzzle 2
Google CTF A Cute Stegosaurus
Google CTF For2
Google CTF In Recorded Conversation
Hack the Arch Level 200
Hack the Arch Level 300
JCC na100 - Across the Wire

## Cheat Sheets
SANS tcpdump & ipv6 tcpdump

# Reference Material to Review before the Practice Session

TCP Handshake <http://packetlife.net/blog/2010/jun/7/understanding-tcp-sequence-acknowledgment-numbers/>  
Protocol Encapsulation <https://en.wikipedia.org/wiki/Encapsulation_(networking)>  
List of Port Numbers <http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml>  
Libpcap File Format <https://wiki.wireshark.org/Development/LibpcapFileFormat>  
USB Capture Setup <https://wiki.wireshark.org/CaptureSetup/USB>  

# What is a Packet-Capture?

A packet capture (PCAP) is a file used to store captured network traffic.  While packets are the data segment at layer 3, pcaps often contain layer 2 frames, or even USB traffic.  

There are many different file formats (pcap, or pcap-ng); generally a packet capture conforms to the libpcacp/winpcap format developed by the berkley guys that do tcpdump.  There are also ncap and snoop, but libpcap is the de facto standard.

# Why is PCAP analysis useful?

Analyzing packet captures is fundamental to understanding traffic flow on a network, performing forensic analysis to understand what has occured on a network post incident, and for extracting artifacts from network traffic.  It is also useful for understanding how an attack, or different tools work, by performing the attack and reviewing the traffic generated by the attack.  It is useful either for offense or defense.

#What should you learn from this practice session?

After the session, participants should be able to:

Understand the difference(s) between pcap, pcap-ng, etc.
Understand the capabilities of packet capture analysis tools.
How to open packet captures.
Analyze packet captures at a high-level (flow?, conversations, endpoints, expert info, etc.).
Analyze transport protocols
Analyze application protocols
Extract contents from packets
Extract/translate packet field information? (tshark, etc)
File carving

# Endnotes
CTF Time Challenges <https://ctftime.org/ctfs>
CTF Time Writeups <https://ctftime.org/writeups>
MCPA Challenges <https://github.com/MCPA/Team-Challenges>
JCC Challenge Writeups <https://github.com/JointCyberTrainingFoundation/Walkthroughs/blob/master/README.md>