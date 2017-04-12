import dropbox

flow = dropbox.client.DropboxOAuth2FlowNoRedirect('e5mnwfj82mx9rgi', 'gmngrwdnaa1cb2x')

access_token = raw_input("Enter the authorization code here: ").strip()

client = dropbox.client.DropboxClient(access_token)
f = open('sample.txt', 'rb')
response = client.put_file('/magnum-opus.txt', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.txt', 'wb')
out.write(f.read())
out.close()
print metadata
