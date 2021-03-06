#!/usr/bin/env python3
# Author: Juber Nunes
# Date: 05/03/2019
# Description: Create bucket and Copy image. 

import sys, boto3, subprocess

boto3.setup_default_session(profile_name='wit')

s3 = boto3.client("s3")

bckt= s3.list_buckets()['Buckets']

### function to list buckets prior creation avoiding duplication

def listbucket():
	for bucket in bckt:
		print (bucket['Name'])
		print ("---")
		try:
			for item in bucket.objects.all():
				print ("\t%s" % item.key)
		except Exception as error:
			print(error)
listbucket() ## calling itelf for initiation

print()

## save the name entered by user to a variable
bucket = input('Please enter an unique name for Bucket\n ---> ')


## default creation of bucket
response = s3.create_bucket(
	Bucket = bucket,
	CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'},
	) 

print()

## grabs the image name from user before copying it over
object_name = input('Name of the image to be copied over\n ---> ')
object_name = open(object_name, 'rb')

## sending object over
response = s3.put_object(
	ACL='public-read',
	Bucket=bucket,
	Body=object_name,
	Key='image.jpg' ##  hardcoded name 
	)

print()
print('Done! Bucket created and image copied')
print()

## reads
f = open('details','r')
for line in f:
	fields = line.split(' ')
	ipaddr=fields[0]
	keyname=fields[1]

## Buildding and pushing the HTML tags to be sent after bucket being created and image uploaded
cmd = 'ssh -o StrictHostKeyChecking=no -i ' + keyname + ' ec2-user@' + ipaddr + ' '"'"'echo "<hr>S3 Image : <br>" | sudo tee -a /var/www/html/index.html'"'"''
bckt_addr = '\"<img src= https://s3-eu-west-1.amazonaws.com/' + bucket + '/image.jpg>\"' 
cmd2= 'ssh -o StrictHostKeyChecking=no -i ' + keyname + ' ec2-user@' + ipaddr + ' '"'"' echo ' +   bckt_addr + ' | sudo tee -a /var/www/html/index.html'"'"'' 

subprocess.run(str(cmd), check=True, shell=True)
subprocess.run(str(cmd2), check=True, shell=True)

input('Press ENTER to continue')


### https://s3-eu-west-1.amazonaws.com/bucketname/image