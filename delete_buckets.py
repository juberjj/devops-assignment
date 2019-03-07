#!/usr/bin/env python3
# Author: Juber Nunes
# Date: 05/03/2019
# Description: Delete Bucket and Contents in one go. 

import sys, boto3

boto3.setup_default_session(profile_name='wit')

s3 = boto3.resource('s3')


### function listing all buckets before deletion
def listbuckets():
	for bucket in s3.buckets.all():
		print (bucket.name)
		print ("---")
		try:
			for item in bucket.objects.all():
				print ("\t%s" % item.key)
		except Exception as error:
			print(error)

listbuckets()

print()
bucket_name =(input('Type the name of the bucket for deletion\n ---> '))

## this will delete the content inside the bucket first and then delete the bucket itself, all in one go for this effort
try:
	bucket.objects.all().delete()
	response = bucket.delete()
	print (response)
except Exception as error:
	print (error)
