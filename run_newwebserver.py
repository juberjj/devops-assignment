#!/usr/bin/env python3
# Author: Juber Nunes
# Date: 05/03/2019
# Description: Create Instance - Capturing tagname from user- Creating Security Group and Keypair. 

import boto3,sys, base64,time

from secgroup import listsecgroup
from secgroup import creategroup

from keypairs import listkeypairs
from keypairs import createkeypair


boto3.setup_default_session(profile_name='wit')

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')


#### Reading Script to be passed to EC2 instance, reading from file instead for practicality

f = open('userData.txt','r').read()

print()

print('This will create an AWS instance with appropriate Security Group and KeyPair in 3 steps')

print()
tag = input('STEP 1 - Type the Tag name of your instance\n --->  ')


print()
listsecgroup()

print()
print('It will now create a new Security Group, please type a unique name')

print()
sc = input('STEP 2 - Please type the name of your Security Group --- Ports 80 and 22 will allow traffic\n ---> ')

print('Creating SC - ' + sc)
data = creategroup(sc)

print()

#input("Press Enter to show keypairs associated to this account ...\n")

listkeypairs()

kp = input('STEP 3 - Please type the name of your the KeyPair to be created. Must be unique\n ---> ')

#print(kp)
data=createkeypair(kp)



instance = ec2.create_instances(
    ImageId='ami-0fad7378adf284ce0',
    MinCount=1,
    MaxCount=1,
    KeyName=kp,
    SecurityGroups=[sc],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags':[
                {
                    'Key':'Name', 
                    'Value': tag
                },
            ]
        },
    ],
    UserData=f,
    InstanceType='t2.micro')
print()
print('Creating Instance, it will take few seconds')
waiter = client.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance[0].id])
instance[0].reload()
#print (instance[0].id, instance[0].state, instance[0].public_ip_address)
print()
print('Done!')
print()

#print('Copying Check_Webserver script over to the newly created instance')
#time.sleep(12)
#copyfile(kp, instance[0].public_ip_address)

# create a file to store the last ip created
outfile = open('details','w')
keyname = kp+'.pem'
outfile.write('{0} {1}'.format(instance[0].public_ip_address, keyname))

input('Press ENTER to continue')

#run_script(kp, instance[0].public_ip_address)
