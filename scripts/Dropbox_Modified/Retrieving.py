import dropbox

flow = dropbox.client.DropboxOAuth2FlowNoRedirect('e5mnwfj82mx9rgi', 'gmngrwdnaa1cb2x')

access_token = raw_input("Enter the authorization code here: ").strip()

client = dropbox.client.DropboxClient(access_token)

folder_metadata = client.metadata('/')

f, metadata = client.get_file_and_metadata('/sample2.txt')
out = open('download.txt', 'wb')
out.write(f.read())
out.close()
print "done"
