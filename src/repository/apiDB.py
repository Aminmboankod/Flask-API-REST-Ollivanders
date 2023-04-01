
import requests
import json
import os

KEY = os.environ['KEY']
FIND = os.environ['FIND']
UPDATEONE = os.environ['UPDATEONE']
DELETE = os.environ['DELETE']
INSERT = os.environ['INSERT']


def get_headers():
    """
        Este método contiene el encabezado para las peticiones
        Return: El encabezado para ser añadido en las peticiones 
    """
    return {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': KEY,
    }

def inventory():
    """
        Este método hace una petición POST a la base de datos sin filtro
        Return: Toda la información que contiene la base de datos en formato JSON dentro de una lista
    """

    url = FIND
    payload = json.dumps({
        "collection": "inventory",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {},
        "projection": {"_id": 0}
    })

    response = requests.request("POST", url, headers=get_headers(), data=payload)
    response = json.loads(response.text)
    items = response.get('documents')
    return items



'''
    Métodos para el crud a la base de datos
'''

def item_db(item_name):
    """
        Este método hace una petición POST a la base de datos buscando por nombre
        Return: Las ocurrencias que coincidan con algún documento de la 
        la base de datos en formato JSON detro de una lista
    """
        
    url = FIND
    payload = json.dumps({
        "collection": "inventory",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {"name": item_name},
    })

    try:
        response = requests.post( url, headers=get_headers(), data=payload)

    except requests.exceptions.HTTPError:

        if response.status == 400:
            print("The query isn't correct")

        if response.status == 401:
            print("Unauthorized user tries to connect!")
        
        if response.status == 404:
            print("HTTP not found!")

        if response.status == 500:
            print("Internal server error")
    finally:
        response = json.loads(response.text)
        item = response.get('documents')
    return item

def update_db(item):
    """
        Este método hace una petición POST a la base de datos para actualizar el item.
    """

    url = UPDATEONE
    payload = json.dumps({
        "collection": "inventory",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {"name": item["name"]},
        "update": {"$set": {"sell_in": item["sell_in"],
                            "quality": item["quality"]
                            }
                    }
    })

    try:
        response = requests.request("POST", url, headers=get_headers(), data=payload)
        
    
        response.raise_for_status()
        print(f"PUT request to {url} with payload {payload} was successful with response {response.text}")
    except requests.exceptions.HTTPError as e:
        print(f"PUT request to {url} with payload {payload} failed with error {e}")
    except Exception as e:
        print(f"PUT request to {url} with payload {payload} failed with error {e}")

def delete():


    url = DELETE
    payload = json.dumps({
        "collection": "inventory",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {}
    })

    requests.request("POST", url, headers=get_headers(), data=payload)

def delete_one(item):
    url = DELETE
    payload = json.dumps({
        "collection": "inventory",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {
                "name": item["name"],
                "sell_in": item["sell_in"],
                "quality": item["quality"]
        }
    })

    requests.request("POST", url, headers=get_headers(), data=payload)

def insert(item):

    url = INSERT
    payload = json.dumps({
        "collection": "inventory",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "document": {
                "name": item["name"],
                "sell_in": item["sell_in"],
                "quality": item["quality"]
        
        }


    })

    requests.request("POST", url, headers=get_headers(), data=payload)


