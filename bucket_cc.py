#!/usr/bin/env python3

import sys, boto3, subprocess

boto3.setup_default_session(profile_name='wit')

s3 = boto3.client("s3")

bckt= s3.list_buckets()['Buckets']

def listbucket():
	for bucket in bckt:
		print (bucket['Name'])
		print ("---")
		try:
			for item in bucket.objects.all():
				print ("\t%s" % item.key)
		except Exception as error:
			print(error)
listbucket()

print()

bucket = input('Please enter an unique name for Bucket\n ---> ')


response = s3.create_bucket(
	Bucket = bucket,
	CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'},
	) 


print()

object_name = input('Name of the image to be copied over\n ---> ')

object_name = open(object_name, 'rb')

response = s3.put_object(
	ACL='public-read',
	Bucket=bucket,
	Body=object_name,
	Key='image.jpg'

	)

print()
print('Done! Bucket created and image copied')
print()

f = open('details','r')#.read()#.decode('utf8')
for line in f:
	fields = line.split(' ')
	ipaddr=fields[0]
	keyname=fields[1]

cmd = 'ssh -o StrictHostKeyChecking=no -i ' + keyname + ' ec2-user@' + ipaddr + ' '"'"'echo "<hr>S3 Image : <br>" | sudo tee -a /var/www/html/index.html'"'"''
bckt_addr = '\"<img src= https://s3-eu-west-1.amazonaws.com/' + bucket + '/image.jpg>\"' 
cmd2= 'ssh -o StrictHostKeyChecking=no -i ' + keyname + ' ec2-user@' + ipaddr + ' '"'"' echo ' +   bckt_addr + ' | sudo tee -a /var/www/html/index.html'"'"'' 
#print(cmd2)
subprocess.run(str(cmd), check=True, shell=True)
subprocess.run(str(cmd2), check=True, shell=True)

input('Press ENTER to continue')

#print(response)

### https://s3-eu-west-1.amazonaws.com/bucl