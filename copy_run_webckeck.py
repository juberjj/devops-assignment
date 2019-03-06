#!/usr/bin/env python3

import boto3, subprocess


boto3.setup_default_session(profile_name='wit')

#def copyfile(keyname, ipaddr):
def copyfile():

	ec2 = boto3.client('ec2')

	f = open('details','r')#.read()#.decode('utf8')
	for line in f:
		fields = line.split(' ')
		ipaddr=fields[0]
		keyname=fields[1]
	#keyname= keyname + '.pem'
	print(keyname)


	#keyname=keyname +'.pem'
	try:
		cmd = 'scp -o StrictHostKeyChecking=no -i ' + keyname + ' check_webserver.py ec2-user@' + ipaddr + ':.'
		cmd2 = 'ssh -o StrictHostKeyChecking=no -i ' + keyname + ' ec2-user@' + ipaddr + ' ./check_webserver.py'
		print(cmd)
		subprocess.run(str(cmd), check=True, shell=True)
		print('Check Webserver copied')
		subprocess.run(str(cmd2), check=True, shell=True)

	except subprocess.CalledProcessError:
		print('Check Webserver not copied')


def run_script(keyname, ipaddr):

	keyname=keyname +'.pem'
	try:
		cmd = 'ssh -o StrictHostKeyChecking=no -i ' + keyname + ' ec2-user@' + ipaddr + './check_webserver.py'
		print(cmd)
		subprocess.run(str(cmd), check=True, shell=True)
		print('Check Webserver copied')
	except subprocess.CalledProcessError:
		print('Check Webserver not copied')	

copyfile()
print()
input('Press ENTER to continue')