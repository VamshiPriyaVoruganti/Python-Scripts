import requests


authorizationCode = ''
clientId= 'fugj7otvhooz3jz815zf4s06tca4kuvk'
clientSecret='8oIeB95fdXSheEvmE0tUKUr2IAr8YdrI'
oauth2URL = 'https://app.box.com/api/oauth2/token'
'''

r=requests.get(https://account.box.com/api/oauth2/authorize?response_type=code&client_id=clientId&state='security_token%3DKnhMJatFipTAnM0nHlZA')

print r.url
'''
getTokens = requests.post(oauth2URL,data={'grant_type' : 'authorization_code','code' : authorizationCode, 'client_id' :clientId, 'client_secret' :clientSecret})
# If the above gives a 4XX or 5XX error
getTokens.raise_for_status()
# Get the JSON from the above
newTokens = getTokens.json()
# Get the new access token, valid for 60 minutes
accessToken = newTokens['access_token']
print accessToken

