import sys,socket,time,argparse
# ./caesar.py ./transposition.py
import caesar,transposition
#./pygenere.py
from pygenere import *
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def read(s):
    s.setblocking(0)
    recv_buf = ''
    data = []
    timeout = 1
              
    begin=time.time()
    while 1:
        if data and time.time()-begin > timeout:
            break
        elif time.time()-begin > timeout*2:
            break
        try:
            recv_buf = s.recv(1024)
            if recv_buf:
                data.append(recv_buf)
                begin = time.time()
            else:
                time.sleep(0.25)
        except:
            pass
    return ''.join(data)  

def connect(host,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(host)
        sock.connect((ip, int(port)))
        return sock
        
    except socket.error, msg:
        print str('Error trying to connect.')

def main():
    verbose = []

    try:
        parser = argparse.ArgumentParser()

        # Host and Port arguments required to connect to remote host
        parser.add_argument(
                '-H', '--host',type=str, help='IP Address', required = True)
        parser.add_argument(
                '-p', '--port',type=int, help='TCP Port', required = True)
        parser.add_argument(
                '-v', '--verbose',help='Enable verbose mode', 
                action="store_true", required = False)

        args = parser.parse_args()
    except argparse.ArgumentError as err:
        print str(err)
        sys.exit(2)

    sock = connect(args.host, args.port)

    # Stage 1
    data = read(sock)
    verbose.append(data)
    if args.verbose:
        print verbose[0]
    cipher = data.split(':')[1].strip()
    plaintext = caesar.brute_force(cipher,1,26,["the"])
    answer = plaintext.split(' ')[6]
    print("{0}::Stage 1 Cipher: {1}{2}".format(color.RED, color.END,cipher))
    print("{0}::Stage 2 Plaintext: {1}{2}".format(color.RED,color.END, plaintext))
    print("{0}::Stage 2 Answer: {1}{2}".format(color.GREEN,color.END,answer))
    sock.sendall(answer + '\n')

    # Stage 2
    data = read(sock)
    verbose.append(data)
    if args.verbose:
        print("\n %s" % verbose[1])
    cipher = data.split(':')[1].strip()
    plaintext = transposition.decipher(cipher)
    answer = plaintext.split('"')[1::2][0]
    print("{0}::Stage 2 Cipher: {1}{2}".format(color.RED, color.END,cipher))
    print("{0}::Stage 2 Plaintext: {1}{2}".format(color.RED,color.END, plaintext))
    print("{0}::Stage 2 Answer: {1}{2}".format(color.GREEN,color.END,answer))
    sock.sendall(answer + '\n')

    #Stage 3
    data = read(sock)
    #print "Data received: %s" % data
    if( (data != "") and ("study" not in data)): 
        cipher = data.split(':')[1]
        key = VigCrack(cipher).crack_codeword()
        #print "Key: %s" % key
        plaintext = Vigenere(cipher).decipher(key)
        plaintext =  plaintext.replace(" ","")
        #print "Plaintext: %s" % plaintext
        if plaintext.find("HERE"):
            answer = plaintext.split("HERE")[1].split("OK")[0]
            print("{0}::Stage 3 Cipher: {1}{2}".format(color.RED, color.END,cipher))
            print("{0}::Stage 3 Plaintext: {1}{2}".format(color.RED,color.END, plaintext))
            print("{0}::Stage 3 Answer: {1}{2}".format(color.GREEN,color.END,answer))
            sock.sendall(answer + "\n")
            print read(sock)
        else:
            print("{0}Plaintext was not properly decrypted.{1}".format(color.RED,color.END))
    else:
        print("{0}No data received for Stage 3.{1}".format(color.RED,color.END))



if __name__ == "__main__":
    main()
