import boto
import boto.s3
import sys,os
from boto.s3.key import Key

def upload_file():
 bucket = conn.create_bucket(bucket_name,location=boto.s3.connection.Location.DEFAULT)

 testfile = "replace this with an actual filename"
 print 'Uploading %s to Amazon S3 bucket %s' % (testfile, bucket_name)
 k = Key(bucket)
 k.key = 'my test file'
 k.set_contents_from_filename('temp.txt')


def download_file():

 bucket = conn.get_bucket(bucket_name)
 bucket_list = bucket.list()
 for l in bucket_list:
  keyString = str(l.key)
  if not os.path.exists(keyString):
    l.get_contents_to_filename(keyString)


AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)

upload_file()
download_file()




