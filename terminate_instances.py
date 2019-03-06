#!/usr/bin/env python3

import boto3

boto3.setup_default_session(profile_name='wit')

ec2 = boto3.client('ec2')

qtd = len(ec2.describe_instances()['Reservations'])

instances = []
for x in range(qtd):

	response=ec2.describe_instances()['Reservations'][x]['Instances'][0]['InstanceId']
	tag=ec2.describe_instances()['Reservations'][x]['Instances'][0]['Tags'][0]['Value']
	state=ec2.describe_instances()['Reservations'][x]['Instances'][0]['State']['Name']
	print(str(x) + ' -- ' + response + ' -- ' + tag + ' -- ' + state)
	instances.append(response)
	print()

delete=input("What instance you wish to terminate ? ")

#print("'%s'" % instances[int(delete)])
#terminate = ec2.terminate_instances(InstanceIds=["'%s'" % instances[int(delete)]])
terminate = ec2.terminate_instances(InstanceIds=[instances[int(delete)]])


print()
input('Press ENTER to continue')

