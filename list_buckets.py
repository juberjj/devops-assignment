#!/usr/bin/env python3
import boto3


boto3.setup_default_session(profile_name='wit')

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print (bucket.name)
    print ("---")
    try:
    	for item in bucket.objects.all():
    		print ("\t%s" % item.key)
    except Exception as error:
    	print(error)