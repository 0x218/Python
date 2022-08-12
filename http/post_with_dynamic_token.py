# This program - 
#   1. Sends a post request to access dynamic token
#   2. Use the dynamic (bearer) token to post data 
#   Note: my backend server expects a bearer token for auth and a base64 encoded data for processing.
#   3. Print the reponse received from the post request 
#   Note: upon successful authentication, my backend server returns another base64 encoded data)


from os import system
import requests
import json

base64EncodedInput = 'SUkqALItAAD / O6ImgZU7sDwzM6wq//pimOOKQkThU07WGF7TT7wqmHWGAAAFABULgAAGwEFAAEAAA3wwe/iHYnE7W7HFIRexUUZhFYpEDAAEAAAACAAAAAAAAAAIAA='


# construct header and payload with clientid, client_secret.
def get_headers_for_token_request():
    token_url = 'https://api-internal.pod.myplaygrounddomain.net/apip/auth/v2/token'
    token_header = {'Accept': 'application/json','Content-Type': 'application/json',}
    token_payload = {'client_id': 'oo1nclud3ooyourooclientidoohereoo','client_secret': 'oo1nclud3ooyouroocl13ntooS3cr3toohereoo','grant_type': 'client_credentials',}
    return token_url, token_header, token_payload


# construct header and payload with input data for post request
def get_headers_for_post(token):
    post_url = "https://api-internal.pod.myplaygrounddomain.net/v1/p2e/api/invocations"
    post_headers = {'Accept': 'application/json','Content-type': 'application/json','Authorization': 'Bearer ' + token,}
    post_payload ={'name' : 'what-ever-applicable', 'role' : 'creator', 'public_key' : ''+ base64EncodedInput,}##pay
    return post_url, post_headers, post_payload


# a post method - returns a response (token_url is designed to return a bearer token in my environment)
def get_token(token_Url, token_header, token_payload):
    token_response = requests.post(token_Url, headers=token_header, json=token_payload)
    return token_response

# another post method - returns a resonse (post_url is designed to return an encoded data)
def post_and_get_response(post_Url, post_headers, post_payload ):
    response = requests.post(post_Url, headers=post_headers, json=post_payload)
    return response



if __name__ == "__main__":
    system('cls')

    token_url, token_header, token_payload = get_headers_for_token_request()
    resp_token = get_token(token_url, token_header, token_payload).json()
    #print (resp_token)
    token = resp_token["access_token"]##ignore all content except the access_token
    #print (token)

    post_Url, post_headers, post_payload = get_headers_for_post(token)
    resp = post_and_get_response(post_Url, post_headers, post_payload).json()
    print (resp)
