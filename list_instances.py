#!/usr/bin/env python3

import boto3

boto3.setup_default_session(profile_name='wit')

ec2 = boto3.client('ec2')

describe = ec2.describe_instances()['Reservations'] 
qtd = len(ec2.describe_instances()['Reservations'])

instances = []

if qtd < 0:
	print('No instances ' + qtd)
for x in range(qtd):
	
	instanceid=describe[x]['Instances'][0]['InstanceId']
	tag=describe[x]['Instances'][0]['Tags'][0]['Value']
	state=describe[x]['Instances'][0]['State']['Name']
	keyname=describe[x]['Instances'][0]['KeyName']


	## check state if running grab public ip else just print instance details
	if state  == 'running':
		pub_ip=describe[x]['Instances'][0]['PublicIpAddress']
		print()
		print(str(x) + ' -- ' + instanceid + ' -- ' + tag + ' -- ' + state + ' -- ' + 'Keyname --' + keyname + '  Public Ip -- ' + pub_ip)
		print()
	else:
		print()
		print(str(x) + ' -- ' + instanceid + ' -- ' + tag + ' -- ' + state + ' -- ' + 'Keyname --' + keyname)
		instances.append(instanceid)
		print()



input('Press ENTER to continue')

