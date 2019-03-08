import json
from time import time
import requests
import jwt


# Open Saved Client Data
with open('XXX.json') as f:
    client_data = json.load(f)

# Set Client info
client_id = client_data['client_id']
private_key = client_data['private_key']

# Set default parameters
auth_url = 'https://oidc.imeetcentral.com/oauth2/token'
grant_type = 'urn:ietf:params:oauth:grant-type:jwt-bearer'

payload = {"iss":client_id,"aud":'oidc.imeetcentral.com',
           "exp":(time() + 600000),
           "iat":time(),
           "scp":'cd.user'}

auth_token = jwt.encode(payload, private_key, algorithm ='RS256')

form_params = {
    'grant_type' : grant_type,
    'assertion' : auth_token
    }


# data to be sent to api
data = {}

# sending post request and saving response as response object
r = requests.post(url = auth_url, data = data)
