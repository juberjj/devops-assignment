#!/usr/bin/env python
# Author: Juber Nunes
# Date: 05/03/2019
# Description: Check if HTTPD is running if not attempt to start it in one go. 

# This script has been adapted for python 2.7 which is installed by default when creating an instance
import subprocess

def checkhttpd():

	try:
		cmd = 'ps -A | grep httpd'
		subprocess.check_call(cmd, shell=True) # the same as subprocess.run check=True, it checks the  
 		print('Webserver is running')
	except subprocess.CalledProcessError:
		print('Webserver is NOT running... Attempting to start it now') 
		subprocess.check_call('systemctl start httpd', shell=True) ## if detected that is not running send the command to start it

def main():

	checkhttpd()

# standard boilerplate to call main function

if __name__ == '__main__':
	main()
