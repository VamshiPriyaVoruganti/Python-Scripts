from dropbox import client, rest, session

def reading_uploading():

	f = open('sample.txt', 'rb')

	response = client.put_file('/upload.txt', f)

	print 'uploaded: ', response


def retrieving():

	folder_metadata = client.metadata('/')

	f, metadata = client.get_file_and_metadata('/sample2.txt')
	out = open('download.txt', 'wb')
	out.write(f.read())
	out.close()
	print "done"


sess = session.DropboxSession('e5mnwfj82mx9rgi', 'gmngrwdnaa1cb2x','dropbox')

request_token = sess.obtain_request_token()

url = sess.build_authorize_url(request_token)
	 

print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
raw_input()
	 

access_token = sess.obtain_access_token(request_token)
	 

client = client.DropboxClient(sess)

reading_uploading()

retrieving()



