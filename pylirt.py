import paramiko
with open('cred_list.txt') as f:
	lines = f.readlines()
	for line in lines:
		IP_address=line.split("|")[0]
		user=line.split("|")[1]
		passw=line.split("|")[2].split("\n")[0]
		print(IP_address,"-",user,"-",passw)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(IP_address, username=user, password=passw)
		try:
			stdin, stdout, stderr =  ssh.exec_command("""cat /etc/passwd""")
			print("/etc/passwd:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""cat /etc/group""")
			print("/etc/group:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""cat /etc/sudoers""")
			print("/etc/sudoers:\n",stdout.read().decode())
		except:
			pass
		try:
                	stdin, stdout, stderr =  ssh.exec_command("""lastlog""")
                	print("Latest login:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""cat /var/log/auth.log""")
			print("auth.log:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""uptime""")
			print("System uptime:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""cat /proc/meminfo""")
			print("Detailed of RAM:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""ps aux""")
			print("Process:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""cat /etc/resolv.conf""")
			print("DNS Configuration:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""cat /etc/hosts""")
			print("/etc/hosts:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""iptables -L -v -n""")
			print("iptables rules:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""find / -type f -size +512k -exec ls -lh {}/;""")
			print("Size +512 file:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""find / -mtime -1 -ls""")
			print("To find all files modified in the last 24 hours use:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""ip a""")
			print("Network interface:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""netstat -nap""")
			print("All listening ports in the network:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""arp -a""")
			print("ARP cache:\n",stdout.read().decode())
		except:
			pass
		try:
			stdin, stdout, stderr =  ssh.exec_command("""echo $PATH""")
			print("Path:\n",stdout.read().decode())
		except:
			pass
		ssh.close()
		print("=============\n")
