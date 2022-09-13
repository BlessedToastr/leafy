# Leafy - A Web Enumeration Tool - Not Finished

Leafy is a Web Enumeration Tool that checks websites for possible LFI vulnerabilities

# Quick Start

### Get the Script

```jsx
wget -q https://raw.githubusercontent.com/BlessedToastr/leafy/main/leafy.py
```

### To Run the Script

```bash
$ python3 leafy.py -h
usage: leafy.py [-h] -m MODE [-i IP] [-p PORT] [-a PATH] [-P PARAM] [-l LIST]

options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  What mode to run leafy on
  -i IP, --ip IP        The IP address of the website you are targeting
  -p PORT, --port PORT  The port the website is running on
  -a PATH, --path PATH  Full path
  -P PARAM, --parameter PARAM
                        The parameter to use
  -l LIST, --list LIST  The full path to the wordlist
```
### To run in LFI mode
```bash
$ python3 leafy.py -m lfi -i <IP> -p <PORT> -a <PATH> -P <PARAMETER> -l <WORDLIST>
```
### To run in dir busting mode
```bash
$ python3 leafy.py -m dir -i <IP> -p <PORT> -a <PATH> -l <WORDLIST>
```

### A list can be pulled with

```bash
wget -q https://raw.githubusercontent.com/BlessedToastr/leafy/main/list
```

# About

Leafy is a script designed to test websites for LFI vulnerabilities. It draws from a list of potential LFI syntaxes and tests those on the domain provided. In the future, Leafy will be fleshed out to a script that does further Web Enumeration.

# Advisory

This script is designed to be for educational use only. Only use this script on networks and machines you have permission to use on. Any misuse of this script will no be the responsibility of the author or other collaborators of this project. 

Created by BlessedToastr
