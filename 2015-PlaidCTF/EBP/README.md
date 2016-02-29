# CTF Practice - 6 February 2016

## Introduction

Kendall is a 300 point pwnable challenge from the 2015 Boston Key Party. The challenge involves exploiting a router, taking advantage of the Superfish vulnerability[\[1\]](#endnote1), and intercepting browsing information.

## Setup


Download the [binary](kendall.tar_.gz?raw=true) and the Superfish root cert [here](superfish.pem?raw=true). When running the binary, make sure you create the required files for the binary to function. So, in the same directory ```touch dhcp.log``` and ```touch password.txt```.

## Solving the Challenge Steps

A breakdown of the steps necessary to finish from [Michael Weissbacher](http://mweissbacher.com/blog/2015/03/01/boston-key-party-2015-kendall-challenge-superfish/):

* Pwn the binary
    * Bypass authentication
    * Overwrite DNS entries with DNS controlled by team
    * Trigger DHCP renew
* Intercept Browsing
    * Set up DNS server that responds with team’s IP
    * Listen to the requests and make them succeed
    * Interpret the HTTP request
    * Set up SSL interception with Superfish CA

### A detailed solution write-up is provided by [Balalaika Cr3w](https://ctfcrew.org/writeup/97).

----
## Endnotes
<a name="endnote1">[1]</a>: In February 2015, Lenovo was caught selling computers with preinstalled "malware" called <strong>Superfish</strong>. Superfish broke the trust chain between the user's computer and the destination by signing all certificates with its own root certificate - thus pretending to be the destination website. Find out more about it [here](http://stephen-brennan.com/2015/02/20/superfish-explained/) from <em>Stephen Brennan</em>. The how to retrieve the root certificate process is described and some other useful links are located at the bottom of the writeup [here](http://blog.erratasec.com/2015/02/extracting-superfish-certificate.html#.VrAfvDYrJBw).
