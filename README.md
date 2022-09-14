# LEAFY - A Web Enumeration Tool

![leafy](/images/leaf.png?raw=true "Leaf")
# What is Leafy?

Leafy is a Web Enumeration Tool that checks websites for possible LFI vulnerabilities

# Quick Start

### Get the Script

```bash
wget -q https://raw.githubusercontent.com/BlessedToastr/leafy/main/leafy.py
```

### To Run the Script

```bash
$ python3 leafy.py -h
 _                __       
| |    ___  __ _ / _|_   _ 
| |   / _ \/ _` | |_| | | |
| |__|  __/ (_| |  _| |_| |
|_____\___|\__,_|_|  \__, |
                     |___/ 

usage: leafy.py [-h] -m MODE [-i IP] [-p PORT] [-a PATH] [-P PARAM] [-P2 PARAM] [-l LIST]

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
$ python3 leafy.py -m lfi -i <IP> -p <PORT> -a <PATH> -P <PARAMETER> -P2 <END PARAMETER>-l <WORDLIST>
```

### To run in dir busting mode
```bash
$ python3 leafy.py -m dir -i <IP> -p <PORT> -a <PATH> -e <EXTENSION> -l <WORDLIST>
```
---
### A list for lfi can be pulled with

```bash
wget -q https://raw.githubusercontent.com/BlessedToastr/leafy/main/list
```

# Examples
### LFI
```bash
python3 leafy.py -m lfi -i 172.16.0.8 -p 80 -a index.php -P ?page= -P2 '&ext=' -l /full/path/to/list
```

### Dir Busting
```bash
python3 leafy.py -m dir -i 172.16.0.8 -p 80 -a '' -e '' -l /full/path/to/list
```

```bash
python3 leafy.py -m dir -i 172.16.0.8 -p 80 -a '/admin' -e '.php' -l /full/path/to/list
```


# About

Leafy is a script designed to test websites for LFI vulnerabilities. It draws from a list of potential LFI syntaxes and tests those on the domain provided. In the future, Leafy will be fleshed out to a script that does further Web Enumeration.

# Advisory

This script is designed to be for educational use only. Only use this script on networks and machines you have permission to use on. Any misuse of this script will no be the responsibility of the author or other collaborators of this project. 

Created by BlessedToastr
