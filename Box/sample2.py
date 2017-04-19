from boxsdk import OAuth2

oauth = OAuth2(
    client_id='	fugj7otvhooz3jz815zf4s06tca4kuvk',
    client_secret='8oIeB95fdXSheEvmE0tUKUr2IAr8YdrI',
    store_tokens=your_store_tokens_callback_method,
)

auth_url, csrf_token = oauth.get_authorization_url('http://localhost:8080')

def store_tokens(access_token, refresh_token):
    # store the tokens at secure storage (e.g. Keychain)
    pass

# Make sure that the csrf token you get from the `state` parameter
# in the final redirect URI is the same token you get from the
# get_authorization_url method.


assert 'THE_CSRF_TOKEN_YOU_GOT' == csrf_token
access_token, refresh_token = oauth.authenticate('YOUR_AUTH_CODE')

from boxsdk import Client

client = Client(oauth)

me = client.user(user_id='me').get()
print 'user_login: ' + me['login']

