import requests
import json
import os

KEY = os.environ["APIKEY"]

'''
    Snippet with an existing database 
'''

def connection_database():

    url = "https://eu-west-2.aws.data.mongodb-api.com/app/data-qcybd/endpoint/data/v1/action/find"

    payload = json.dumps({
        "collection": "items",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter":{}
        
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': KEY, 
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    return response


