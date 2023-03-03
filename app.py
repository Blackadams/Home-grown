import requests
import time

def home_grown():
    url = 'https://powerup.home-grown.co.za/api/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
    data = {'grant_type': 'password', 'username': '', 'password': ''}
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.ok:
        return response.json()
    else:
        raise ValueError('Failed to get access token')

def unpack_token(token):
    access_token = token['access_token']
    token_type = token['token_type']
    expires_in = token['expires_in']
    user_name = token['userName']
    issued = token['.issued']
    expires = token['.expires']
    
    return access_token, token_type, expires_in, user_name, issued, expires


counter = 0

def generate_msgid():
    global counter
    
    # Get the current date and time in the specified format
    dt_string = time.strftime("%Y%m%d%H%M%S")
    
    # Increment the counter and rollover if it exceeds 999999
    counter = (counter + 1) % 1000000
    
    # Pad the counter with leading zeros to make it 6 digits long
    counter_str = str(counter).zfill(6)
    
    # Concatenate the date/time string and counter string to form the MsgID
    msgid = dt_string + counter_str
    
    return msgid













