import requests
import json







def get_headers():
    """
        Este método contiene el encabezado para las peticiones
        Return: El encabezado para ser añadido en las peticiones 
    """
    return {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': "eNChn3gB6rRCKR9fzSRJYsVnePizUSRxvgReuXOcrEl4lhUe5j3XkSkLEKcmXwMW",
    }


def read_items():
    """
        Este método hace una petición POST a la base de datos sin filtro
        Return: Toda la información que contiene la base de datos en formato JSON
    """

    url = "https://eu-west-2.aws.data.mongodb-api.com/app/data-qcybd/endpoint/data/v1/action/find"
    payload = json.dumps({
        "collection": "items",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {},
    })

    response = requests.request("POST", url, headers=get_headers(), data=payload)
    return response


def read_item(item_name):
    url = "https://eu-west-2.aws.data.mongodb-api.com/app/data-qcybd/endpoint/data/v1/action/find"
    payload = json.dumps({
        "collection": "items",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {"name": item_name},
    })
    response = requests.request("POST", url, headers=get_headers(), data=payload)

    response = json.loads(response.text)
    item = response.get('documents')
    return item