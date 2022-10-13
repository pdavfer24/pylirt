# Pylirt - Python Linux Incident Response Toolkit

Tested Kali 2022.1

## Description

With this application, it is aimed to accelerate the incident response processes by collecting information in linux operating systems.

## Features

Information is collected in the following contents.

/etc/passwd

cat /etc/group

cat /etc/sudoers

lastlog

cat /var/log/auth.log

uptime/proc/meminfo

ps aux

/etc/resolv.conf

/etc/hosts

iptables -L -v -n

find / -type f -size +512k -exec ls -lh {}/;

find / -mtime -1 -ls

ip a

netstat -nap

arp -a

echo $PATH


## Installation

git clone https://github.com/anil-yelken/pylirt

cd pylirt

sudo pip3 install paramiko

## Usage

The following information should be specified in the cred_list.txt file:

IP|Username|Password

<img src="https://github.com/anil-yelken/pylirt/blob/main/creds_list.jpg">

sudo python3 plirt.py

<img src="https://github.com/anil-yelken/pylirt/blob/main/pylirt.jpg">

## Contact

https://twitter.com/anilyelken06

https://medium.com/@anilyelken
