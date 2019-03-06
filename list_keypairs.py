#!/usr/bin/env python3

import boto3

# set profile to WIT as the default goes to personal one
boto3.setup_default_session(profile_name='wit')


def listkeypairs():

	ec2 = boto3.client('ec2')

	keypair = ec2.describe_key_pairs()['KeyPairs']

	#keys = {key['KeyName']: key for key in keypair}

	keys = [key['KeyName'] for key in keypair]

	print('\n')
	print('You Have '+ str(len(keys)) + ' KeyPairs Associated to this Account' )
	print('\n')

	for item in keys:
		print('-- '+ item)

	print('\n')

#listkeypairs()