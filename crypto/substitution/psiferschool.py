#!/usr/bin/env python
#socat TCP4-LISTEN:12345,reuseaddr,fork EXEC:"python -u ./psiferschool.py"
#Or, if preferrable, run "python -u ./psifeschool.py" from xinetd. The unbuffered option is important.
from __future__ import print_function
import os
import random
import re
import signal
import time
import sys


def receive_alarm(signum, stack):
    print('Time\'s up. Try again later.')
    sys.exit(-1)

signal.signal(signal.SIGALRM, receive_alarm)
TIMEOUT = 10
STAGE = 1
flag = "flag{IGraduatedPsiferSchoolAndAllIGotWasThisLousyFlag}"
signal.alarm(TIMEOUT)
starttime = time.time()

def main():
    global STAGE
    global flag

    print('''
    Welcome to psifer school v0.002

Your exam begins now. You have %s seconds, work fast.
    ''' % TIMEOUT)


#CEASAR CIPHER
    answer = random.choice(['easypeesy','easyasabc','supersimple','notveryhard','hopeyouautomate','answerhere'])
    plaintext = "the answer to this stage is %s" % answer
    print(plaintext,file=sys.stderr)
    print(answer,file=sys.stderr)
    ciphertext = ''
    slide = random.randint(1,24)
    for c in plaintext:
        if c.isalpha():
            if ord(c)+slide <= ord('z'):
                ciphertext += chr(ord(c)+slide)
            else:
                ciphertext += chr(ord(c)+slide-26)
        else:
            ciphertext += c

    print("Here is your first psifer text, a famous ancient roman would be proud if you solve it.\n\npsifer text: %s" % ciphertext)

    try:
        attempt = raw_input()
    except:
        print("Connection dead, quitting.",file=sys.stderr)

    if attempt.upper()==answer.upper():
        timenow = time.time()
        print("Congratulations, you have solved stage %d. You have %s seconds left." % (STAGE, int(TIMEOUT - (timenow - starttime))))
        STAGE +=1 
    else:
        print("Looks like you need to study more.")
        sys.exit(-1)

#TRANSPOSITION CIPHER
    answer = random.choice(['winning for the win','this is where the answer goes','easiest answer','not not wrong','more answers here','tired of making up bogus answers'])
    plaintext = "I hope you don't have a problem with this challenge. It should be fairly straight forward if you have done lots of basic crypto. The magic phrase for your efforts is \"%s\". For your efforts, you will get another challenge!." % answer
    print(plaintext,file=sys.stderr)
    print(answer,file=sys.stderr)
    width = random.randint(2,len(plaintext)/4)
    ciphertext = [''] * width
    for column in range(width):
        pointer = column
        while pointer < len(plaintext):
            ciphertext[column] += plaintext[pointer]
            pointer += width

    ciphertext=''.join(ciphertext)

    print("Now it's time for something slightly more difficult. Hint, everybody knows it's not length that matters.\n\npsifer text: %s" % ciphertext)

    try:
        attempt = raw_input()
    except:
        print("Connection dead, quitting.",file=sys.stderr)

    if attempt.upper()==answer.upper():
        timenow = time.time()
        print("Congratulations, you have solved stage %d. You have %s seconds left." % (STAGE, int(TIMEOUT - (timenow - starttime))))
        STAGE +=1 
    else:
        print("Looks like you need to study more.")
        sys.exit(-1)

#VIGENERE CIPHER
    answer = random.choice(['stagekey','applepie','magicwand','normalwords','blahlah','nothingtricky'])
    plaintext = "This time we will give you more plaintext to work with. You will probably find that having extra content that is ascii makes this one more solvable. It would be solvable without that but we will make sure to give lots of text just to make sure that we can handle it. I wonder how much will be required. Lets put the magic phrase for the next level in the middle right here %s. Ok, now more text to make sure that it is solvable. I should probably just put in some nursery rhyme or something. Mary had a little lamb, little lamb, little lamb. Mary had a little lamb whose fleeze was white as snow. I don't want to make this harder than it needs to be, if you've solved a lot of simple crypto challenges, you probably already have the code and will breeze right through it. If it helps, most of the plaintext is static at each of the levels, I'm not a masochist. The funny thing is that depending on which random key you get, that poem might be exactly the right offset to successfully mount an attack. We'll see. Little bit more, little bit more, there!" % answer
    print(plaintext,file=sys.stderr)
    print(answer,file=sys.stderr)
    keyword = random.choice(['dictionary','words','areeasy','tobrute','force']).upper()
    ciphertext = ''
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keywordIndex = 0
    for char in plaintext:
        if char.isalpha():
            num = upper.find(char.upper())
            num += upper.find(keyword[keywordIndex])
            num %= 26
            #print("char: %c, num: %d" % (char,num))
            ciphertext += upper[num]
            keywordIndex +=1
            keywordIndex %= len(keyword)
    ciphertext = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]

    print("Last one.\n\npsifer text: %s" % ' '.join(ciphertext))

    try:
        attempt = raw_input()
    except:
        print("Connection dead, quitting.",file=sys.stderr)

    if attempt.upper()==answer.upper():
        timenow = time.time()
        print("Congratulations, you have solved stage %d. The flag is: %s." % (STAGE,flag))
        print("Solved",file=sys.stderr)
        STAGE +=1 
    else:
        print("Looks like you need to study more.")
        sys.exit(-1)

if __name__ == "__main__":
    main()
