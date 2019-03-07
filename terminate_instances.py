#!/usr/bin/env python3
# Author: Juber Nunes
# Date: 05/03/2019
# Description: Terminate EC2 instances - Listing them to user first 


import boto3

boto3.setup_default_session(profile_name='wit')

ec2 = boto3.client('ec2')

qtd = len(ec2.describe_instances()['Reservations'])

instances = [] ## building an empty array with info from instances so user can use pass the position on the array for termination rather that EC2 ID

for x in range(qtd):

	response=ec2.describe_instances()['Reservations'][x]['Instances'][0]['InstanceId']
	tag=ec2.describe_instances()['Reservations'][x]['Instances'][0]['Tags'][0]['Value']
	state=ec2.describe_instances()['Reservations'][x]['Instances'][0]['State']['Name']
	print(str(x) + ' -- ' + response + ' -- ' + tag + ' -- ' + state)
	instances.append(response)
	print()

delete=input("What instance you wish to terminate ? ")

#print("'%s'" % instances[int(delete)])
terminate = ec2.terminate_instances(InstanceIds=[instances[int(delete)]])


print()
input('Press ENTER to continue')

