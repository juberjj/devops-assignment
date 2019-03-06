#!/usr/bin/env python3
import sys, boto3

boto3.setup_default_session(profile_name='wit')

s3 = boto3.resource('s3')

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

#print(bucket_name)
# #for bucket_name in sys.argv[1:]:
#     bucket = s3.Bucket(bucket_name)

try:
	bucket.objects.all().delete()
	response = bucket.delete()
	print (response)
except Exception as error:
	print (error)
