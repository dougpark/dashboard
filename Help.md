## Python Virtual Environment
* Create:   python -m venv .venv
* Activate: source .venv/bin/activate

## Linux find a process by name
* ps aux | grep -i server.py




## How to find the pid for a running process 
* https://unix.stackexchange.com/a/237911
* ps ax | awk '! /awk/ && /myprocessname/ { print $1}'

