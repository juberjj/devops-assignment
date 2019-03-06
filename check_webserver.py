#!/usr/bin/env python


# This script has been adapted for python 2.7 which is installed by default when creating an instance
import subprocess

def checkhttpd():

	try:
		cmd = 'ps -A | grep httpd'
		subprocess.check_call(cmd, shell=True) # the same as subprocess.run check=True, it checks the  
 		print('Webserver is running')
	except subprocess.CalledProcessError:
		print('Webserver is NOT running... Attempting to start it now')
		subprocess.check_call('systemctl start httpd', shell=True)

def main():

	checkhttpd()

# standard boilerplate to call main function

if __name__ == '__main__':
	main()
