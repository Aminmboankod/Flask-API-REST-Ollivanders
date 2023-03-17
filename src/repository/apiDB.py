import requests
import json
import os





# Get Headers devuelve el diccionario 
# con el encabezado para las solicitudes

def get_headers():
    return {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': "eNChn3gB6rRCKR9fzSRJYsVnePizUSRxvgReuXOcrEl4lhUe5j3XkSkLEKcmXwMW",
    }


def read_items():
    url = "https://eu-west-2.aws.data.mongodb-api.com/app/data-qcybd/endpoint/data/v1/action/find"
    payload = json.dumps({
        "collection": "items",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {},
    })

    response = requests.request("POST", url, headers=get_headers(), data=payload)
    return response
