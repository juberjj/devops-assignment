#!/usr/bin/env python3
# Author: Juber Nunes
# Date: 05/03/2019
# Description: Create and List Security Group. 



import boto3, sys, os, stat

# module python-dotenv installed for reading environment variables through a .env file (pip install python-dotenv)
# importing file 
from dotenv import load_dotenv

# Load file from the path.
load_dotenv()

boto3.setup_default_session(profile_name=os.getenv('profile'))

# function taking one parameter which is the name to be created
def creategroup(name):
# set profile through .env file as the default goes to personal one

	ec2 = boto3.resource('ec2')
	# Create sec group - VPC is being passed through environment variable set on .env
	sec_group = ec2.create_security_group(
		GroupName=name, Description='allow web', VpcId=os.getenv('VpcId'))
	sec_group.authorize_ingress(
		IpPermissions=[
		{
		'IpRanges':[{'CidrIp':'0.0.0.0/0'}],
		'IpProtocol':'tcp',
		'FromPort':80,
		'ToPort':80,
		},
		{
		'IpRanges':[{'CidrIp':'0.0.0.0/0'}],
		'IpProtocol':'tcp',
		'FromPort':22,
		'ToPort':22
		}

		]
		)
	# function returns the security group id created for subsequent requests
	return sec_group.id


## instance['Reservations'][0]['Instances'][0]['PublicIpAddress']

def listsecgroup():

	# load ec2 client
	ec2 = boto3.client('ec2')

	# load all sceurity groups details to variable
	sec_group = ec2.describe_security_groups()['SecurityGroups']

	# filter the results by key "GroupName and Description"
	secs = [sec['GroupName'] for sec in sec_group]
	desc = [sec['Description'] for sec in sec_group]

	print('\n')
	print('You Have '+ str(len(secs)) + ' Security Groups Associated to this Account' )
	print('\n')

	for item, des in zip(secs, desc):
		print('Group Name  --- ' + item)
		print('Description --- ' + des)


		print('\n')
	return(item)

#listsecgroup()
