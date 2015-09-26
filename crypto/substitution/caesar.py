import string,argparse

def rot(msg,shift):
    """ helper function for the encrypt and decrypt functions """

    # create a character translation table
    trans = dict(zip(string.lowercase, string.lowercase[shift:] + string.lowercase[:shift]))
    trans.update(zip(string.uppercase, string.uppercase[shift:] + string.uppercase[:shift]))

    # apply the translation table to the msg string
    return ''.join(trans.get(ch, ch) for ch in msg)

def encipher(plaintext,shift):
    """ return an enciphered string given a key and plaintext """
    return rot(plaintext,shift)

def decipher(cipher,shift):
    """ return an deciphered string given a key and ciphertext """
    return rot(cipher,-shift)

def brute_force(ciphertext,shift_from,shift_to,wordlist):
    """ brute force a caesar cipher text given a range of rotation values
    in integer format and a list of words in string format
    Return a plaintext string if it contains any words in the wordlist"""
    plaintext = ''
    answer = ''
    for i in range(shift_from,shift_to):
        plaintext = decipher(ciphertext,int(i))
        if  any(word.lower() in plaintext.lower() for word in wordlist):
            answer = plaintext
    return answer

def main():
    try:
        parser = argparse.ArgumentParser()

        # Host and Port arguments required to connect to remote host
        parser.add_argument(
                '-m', '--message',type=str, help='Ciphertext/Plaintext message', required = True)
        parser.add_argument(
                '-s', '--shift',type=int, help='Numerical value to shift', required = False)
        parser.add_argument(
                '-f', '--force',help='Brute Force', action="store_true", required = False)

        mode = parser.add_mutually_exclusive_group()
        mode.add_argument("-d", "--decipher", action="store_true")
        mode.add_argument("-e", "--encipher", action="store_true")

        args = parser.parse_args()

        if(args.force):
            print brute_force(args.message,1,26,["the","you","we","he","she"])
        elif(args.encipher):
            print encipher(args.message,args.shift)
        elif(args.decipher):
            print decipher(args.message,args.shift)

    except argparse.ArgumentError as err:
        print str(err)
        sys.exit(2)

if __name__ == "__main__":
    main()
