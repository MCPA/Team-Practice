Introduction to Buffer Overflows
======

### Description

Just a reminder of this week's walk-thru on 31 July at 2030 PM EST. I will be covering a walk-thru on John's library from our most recent event - mainly because I spent my time working with that and have my own solution after the event.
 
There are three references for the walk-thru
* https://github.com/thebarbershopper/ctf-writeups/tree/master/polictf-2015/johns-library
* http://www.bannsecurity.com/index.php/home/10-ctf-writeups/11-polictf-2015-john-s-library
* http://phrack.org/issues/49/14.html

Please at least read through the first reference - this way you will be better armed to ask questions. The second reference is a more technical description of how the program is vulnerable, how to get a leak, and why the exploit works. The last reference is the go-to on buffer overflows for any programmer wanting to learn about buffer overflows.

In this walk-thru. I will focus mainly on what a buffer overflow is, how to find one, and then leverage it against john's library. I recommend setting up your own system ahead of time so while I do the walk-thru you can follow along inside GDB and on your own VM. Of particular note you will need Linux VM with randomization turn ON. You can do that with the following command: sudo sysctl kernel.randomize_va_space=2. Download the binary @ https://github.com/thebarbershopper/ctf-writeups/blob/master/polictf-2015/johns-library/johns-library

Last, after I'm done with the walk-thru time dependent we can try some live events online. The goal is for this session to last between 1-2 hours depending on interest.
