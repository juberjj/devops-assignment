#!/usr/bin/env python3
import boto3, os

# setup default credentials
boto3.setup_default_session(profile_name='wit')

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

