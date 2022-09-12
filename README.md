# Leafy - A Web Enumeration Tool - Not Finished

Leafy is a Web Enumeration Tool that checks websites for possible LFI vulnerabilities

# Quick Start

### Get the Script

```jsx
wget -q https://raw.githubusercontent.com/BlessedToastr/leafy/main/leafy.py
```

### To Run the Script

```bash
python3 leafy.py -i <IP> -p <port> -a <path> -P <parameter> -l <list>
```

- IP is the IP address you are targeting
- Port is the port the webserver is listening on
- Path is the file path to the vulnerable php script
- Parameter is the php parameter to user
  - ex: ?page=, ?dir=, ?file=, etc.
- List is the file of potential payloads

### A list can be pulled with

```bash
wget -q https://raw.githubusercontent.com/BlessedToastr/leafy/main/list
```

# About

Leafy is a script designed to test websites for LFI vulnerabilities. It draws from a list of potential LFI syntaxes and tests those on the domain provided. In the future, Leafy will be fleshed out to a script that does further Web Enumeration.

# Advisory

This script is designed to be for educational use only. Only use this script on networks and machines you have permission to use on. Any misuse of this script will no be the responsibility of the author or other collaborators of this project. 

Created by BlessedToastr
