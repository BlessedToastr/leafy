import argparse
from ast import arg
import urllib.request
from urllib.error import HTTPError


# Initial Banner
leafy_banner = '''
 _                __       
| |    ___  __ _ / _|_   _ 
| |   / _ \/ _` | |_| | | |
| |__|  __/ (_| |  _| |_| |
|_____\___|\__,_|_|  \__, |
                     |___/ 
'''

lfi_banner = '''
 _     _____ ___            ____ _   _ _____ ____ _  __
| |   |  ___|_ _|          / ___| | | | ____/ ___| |/ /
| |   | |_   | |   _____  | |   | |_| |  _|| |   | ' / 
| |___|  _|  | |  |_____| | |___|  _  | |__| |___| . \ 
|_____|_|   |___|          \____|_| |_|_____\____|_|\_\
'''

dir_banner = '''
 ____ ___ ____    ____  _   _ ____ _____ _____ ____  
|  _ \_ _|  _ \  | __ )| | | / ___|_   _| ____|  _ \ 
| | | | || |_) | |  _ \| | | \___ \ | | |  _| | |_) |
| |_| | ||  _ <  | |_) | |_| |___) || | | |___|  _ < 
|____/___|_| \_\ |____/ \___/|____/ |_| |_____|_| \_\
'''
print(leafy_banner)

count = 0

# Arg checker
def check_arg(arg):
    try:
        arg
    except:
        print('Missing needed argument')
        exit

# Exploit Function for apache log poisoning
def exploit_apache(url):
    print('yes')

# Dir busting function
def getRespCode(url):
    try:
        resp = urllib.request.urlopen(url)
        # print(resp.getcode())
        if resp.getcode() == 200 or resp.getcode() == 204 or resp.getcode() == 301 or resp.getcode() == 302 or resp.getcode() == 307 or resp.getcode() == 401 or resp.getcode() == 403:
            print(url)
    except HTTPError as e:
        return e.code()

# Init parser
parser = argparse.ArgumentParser()

# Add Args
parser.add_argument("-m", "--mode", help="What mode to run leafy on", metavar="MODE", dest="mode", type=str, required=True) # Required
parser.add_argument("-i", "--ip", help="The IP address of the website you are targeting", metavar="IP", dest="ip", type=str) # LFI, DIR
parser.add_argument("-p", "--port", help="The port the website is running on", metavar="PORT", dest="port", type=str) # LFI, DIR
parser.add_argument("-a", "--path", help="Full path", metavar="PATH", dest="path", type=str) # LFI, DIR
parser.add_argument("-e", "--extension", help="extension to brute force", metavar="TYPE", dest="ext", type=str) # DIR
parser.add_argument("-P", "--parameter", help="The parameter to use", metavar="PARAM", dest="param", type=str) # LFI
parser.add_argument("-P2", "--parameter2", help="In case you need a second parameter after lfi line", metavar="PARAM2", dest="param2", type=str)
parser.add_argument("-l", "--list", help="The full path to the wordlist", metavar="LIST", dest="list", type=str) # LFI, DIR

# Get the args
args = parser.parse_args()

# -----------------------------------------------------------------------------------------------------------

# Exploit Mode
if args.mode == "exploit":
    check_arg(args.ip)
    try:
        args.ip
    except:
        print('L')
        exit

# LFI MODE
if args.mode == "lfi":
    if args.ip is not None and args.list is not None:

        # If port is not given, default to 80
        if args.port is not None:
            port = args.port
        else:
            port = "80"

        # If path is not given, default to none
        if args.path is not None:
            path = args.path
        else:
            path = ""
        
        # If parameter is not given, default to ?file=
        if args.param is not None:
            param = args.param
        else:
            param = "?file="

        # If second parameter is not given, default to none
        if args.param2 is not None:
            param2 = args.param2
        else:
            param2 = ""

        # Define the website
        website = "http://" + args.ip + ":" + port + "/" + path + param

        # Open list and read all the lines
        file = open(args.list, 'r')
        lines = file.readlines()
        with open(args.list, 'r') as fp:
            length = len(fp.readlines())

        # Banner
        print(leafy_banner)

        # Read and loop through every line in file
        for line in lines:
            payload = website + line + param2
            payload = payload.replace("\n", "")
            resp = urllib.request.urlopen(payload)
            if b'root' in resp.read():
                print(payload)
                count += 1
            else:
                continue
    else:
        print("You need to specify which IP to target and a wordlist")
        exit

# -----------------------------------------------------------------------------------------------------------

# DIR BUST MODE
if args.mode == "dir":
    
    # Test for required args
    # Test for IP
    try:
        args.ip
    except:
        print('You need to indicate an IP to target')
        exit
    
    # Test for port
    try:
        args.port
    except:
        print("you need to indicate a port to target")
        exit

    # Test for path
    try:
        args.path
    except:
        print("you need to indicate a path to target")
        exit
    
    # Test for extension
    try:
        args.ext
    except:
        print("you need to indicate an extension")
        exit

    # Test for list
    try:
        args.list
    except:
        print("you need to indicate a list")
        exit
    

    # Define the website
    website = "http://" + args.ip + ":" + args.port + "/" + args.path + "/"

    # Open list and read all the lines
    file = open(args.list, 'r')
    lines = file.readlines()
    with open(args.list, 'r') as fp:
        length = len(fp.readlines())

    # Banner
    print(dir_banner)

    # Directory busting
    for line in lines:
        payload = website + line + str(args.ext)
        try:
            getRespCode(payload)
        except:
            continue

# -----------------------------------------------------------------------------------------------------------

# Print when script is done
print("Potential Paths Found: " + str(count))
print("done")
