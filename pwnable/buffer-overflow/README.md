Introduction to Buffer Overflows
======

### Description

This practice session was covered during a HoT session on 31 July at 2030 PM EST. It covered a walk-thru on John's library from iCTF - mainly because I spent my time working with that and have my own solution after the event. It also demonstrated overflowing buffers with a pre-made binary included in this package.

### Pre-reading Material
There are three references for the walk-thru that will help you understand
* https://github.com/thebarbershopper/ctf-writeups/tree/master/polictf-2015/johns-library
* http://www.bannsecurity.com/index.php/home/10-ctf-writeups/11-polictf-2015-john-s-library
* http://phrack.org/issues/49/14.html

Please at least read through the first reference - this way you will be better armed to ask questions. The second reference is a more technical description of how the program is vulnerable, how to get a leak, and why the exploit works. The last reference is the go-to on buffer overflows for any programmer wanting to learn about buffer overflows.

### Summary

This session focused mainly on what a buffer overflow is, how to find one, and then leverage it against a binary. I recommend setting up your own system ahead of time so while I do the walk-thru you can follow along inside GDB and on your own VM. Of particular note you will need Linux VM with randomization turned ON. You can do that with the following command: ``` sudo sysctl kernel.randomize_va_space=2 ```. [Download the binary](https://github.com/thebarbershopper/ctf-writeups/blob/master/polictf-2015/johns-library/johns-library). I've made a couple modifications to the programming material and was missing time to prepare for john's library. I'll cover the progress I made on it and then switch over to exploiting a different challenge to give the demo. Either way it should be helpful to watch and see the methodology.

Last - there are compiling options for the intermediate challenge co-located with this readme. The practice session is based on the easiest challenge compilation option.

### Links

The recorded practice session can be found [here](http://www.youtube.com/watch?v=SpVKnG5hwng)  
Practice material can be found [here](https://github.com/MCPA/Team-Challenges/tree/master/pwnable/buffer-overflow)
