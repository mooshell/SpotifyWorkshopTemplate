# File used to connect with the API
from requests import post, get
import json
from urllib.parse import urlencode

import base64
from dotenv import load_dotenv
import os
import datetime 

# Accessing Information from your .env file
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

class SpotifyAPI(object):

    # Our Access Token Need to Make Requests to the Spotify Web API
    access_token = None
    # The time when our Access Token Will Expire
    access_token_expires = None
    # A boolean value indicating whether our access token is Expired or Not
    access_token_expired = True
    # Our Client ID
    client_id = None
    # Our Client Secret
    client_secret = None
    # The Endpoint to Request a Token
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_creds(self):

        """
            Returns a base64 encoded string
        """

        client_id = self.client_id
        client_secret = self.client_secret
        # Ensuring client_id and client_secrets have values
        if client_secret == None or client_id == None:
            raise Exception("You must set client_id and client secret")
        # Auth String BEFORE encoding
        auth_string = client_id + ":" + client_secret
        # This is currently a string, but to encode the string using base64, we need to convert it into BYTES
        # Convert the String Into Bytes
        auth_bytes = auth_string.encode()
        # Encode String in Base64
        encoded_auth = base64.b64encode(auth_bytes)

        return encoded_auth.decode()

    ############################
    #   SET UP TOKEN HEADERS   #
    ############################

    def get_token_header(self):

        """
            Returns the headers necessary to request an access token
        """
        
        client_creds_b64 = self.get_client_creds()

        return {
            # INSERT: TOKEN HEADERS    
        }
    
    ############################
    #     SET UP TOKEN DATA    #
    ############################

    def get_token_data(self):

        """
            Returns the data necessary to request an access token
        """

        return {
            # INSERT: TOKEN DATA  
        }

    ############################
    # RETRIEVE AN ACCESS TOKEN #
    ############################

    def perform_auth(self):

        """
            Returns True if an access token is successfully obtained
        """

        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_header()

        # INSERT: Performing the Request
        response = None

        # INSERT: Check if Request is Valid
        valid_request = None

        if not valid_request:
            raise Exception("Could not authenticate Client")

        # INSERT: Pulling Necessary Data from the Response
        now = datetime.datetime.now()
        data = response.json()
        # INSERT: Access Token
        access_token = None
        self.access_token = access_token
        # INSERT: Expires In
        expires_in = None
        # INSERT: The time when the token will expire
        expires = None
        self.access_token_expires = expires
        self.access_token_expired = False
        
        return True

    def get_access_token(self):

        """
            Retrieves the current access token; refreshes the token if it is expired
        """

        auth_done = self.perform_auth()
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token()
        return token

    ###############################
    #   SET UP RESOURCE HEADERS   #
    ###############################

    def get_resource_header(self):

        """
            Retrieve the headers necessary to make an authenticated API call
        """

        access_token = self.get_access_token()

        headers = {
            #INSERT: RESOURCE HEADERS
        }

        return headers

    #######################################################
    # Performing a Search Query Given A Track & An Artist #
    #######################################################

    def search(self, query=None, search_type='track'):
        """
            Returns the JSON response of an request made to the Search endpoint
        """

        if query == None:
            raise Exception("A query is required")
        
        if isinstance(query, dict):
            #turns a dictionary into a list
            query_list = [ k + ":" + v for k,v in query.items()]
            query = " ".join(query_list)

        query_params = urlencode({"q": query, "type": search_type.lower(), "limit": "1"})

        headers = self.get_resource_header()

        # INSERT: The Endpoint we wish to Query
        endpoint = None
        lookup_url = endpoint + "?" + query_params

        # INSERT: The GET Request
        response = None
        
        if response.status_code not in range(200,299):
            return {}
        
        return response.json()
    
    ######################################
    # PERFORMING AN AUDIO ANALYSIS QUERY #
    ######################################

    def get_audio_analysis(self, _id):
        """
            Returns the JSON response of an request made to the Audio Analysis
        """

        if _id == None:
            raise Exception("An id is required")

        headers = self.get_resource_header()
        
        # INSERT: The Endpoint we wish to Query
        endpoint = None
        lookup_url = endpoint + str(_id)

        # INSERT: The GET Request
        response = None

        if response.status_code not in range(200,299):
            return {}
        
        return response.json()
