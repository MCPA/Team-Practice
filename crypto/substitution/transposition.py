#!/bin/python

def decipher(msg):
    for j in range(2, len(msg)):

        dec_msg = ['0'] * len(msg)
        idec_msg, shift = 0, 0

        for i in range(len(msg)):
            dec_msg[idec_msg] = msg[i]
            idec_msg += j

            if idec_msg > len(msg) - 1:
                shift += 1
                idec_msg = shift
        dec_msg = "".join(dec_msg)

        if "you" not in dec_msg: continue
        return dec_msg

#cipher = open('string.txt','r').readline().rstrip()
#print decipher(cipher)
