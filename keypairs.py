#!/usr/bin/env python3
# Author: Juber Nunes
# Date: 05/03/2019
# Description: Create and List Keypairs 


import boto3, sys, os, stat

# set profile to WIT as the default goes to personal one
boto3.setup_default_session(profile_name='wit')

def createkeypair(key):
	ec2 = boto3.client('ec2')

	keypair = ec2.describe_key_pairs()['KeyPairs']
	test=[item for item in keypair if item.get('KeyName')==key]

	if test!=[]:
		print()
		print('Key already exists, please try with a different name')

	# create a file to store the key locally
	outfile = open(key + '.pem','w')

	# call the boto ec2 function to create a key pair
	key_pair = ec2.create_key_pair(KeyName=key)

	# capture the key and store it in a file
	KeyPairOut = str(key_pair.get('KeyMaterial'))
	outfile.write(KeyPairOut)

	os.chmod(key + '.pem', stat.S_IRUSR)


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

