import dropbox

f = open('sample.txt', 'rb')

flow = dropbox.client.DropboxOAuth2FlowNoRedirect('e5mnwfj82mx9rgi', 'gmngrwdnaa1cb2x')

access_token = raw_input("Enter the authorization code here: ").strip()

client = dropbox.client.DropboxClient(access_token)

response = client.put_file('/sample.txt', f)

print 'uploaded: ', response

