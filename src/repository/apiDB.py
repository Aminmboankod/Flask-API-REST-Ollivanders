
#from dotenv import load_dotenv
import requests
import json
import os

'''
    Uso el método dotenv_values para cargar las variables de entorno del archivo .env
'''

#load_dotenv()
KEY = os.environ['KEY']
FIND = os.environ['FIND']
UPDATEONE = os.environ['UPDATEONE']

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


######################## C R U D #########################

def inventory():
    """
        Este método hace una petición POST a la base de datos sin filtro
        Return: Toda la información que contiene la base de datos en formato JSON dentro de una lista
    """

    url = FIND
    payload = json.dumps({
        "collection": "items",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {},
    })

    response = requests.request("POST", url, headers=get_headers(), data=payload)
    return response


def item_db(item_name):
    """
        Este método hace una petición POST a la base de datos buscando por nombre
        Return: Las ocurrencias que coincidan con algún documento de la 
        la base de datos en formato JSON detro de una lista
    """
        
    url = FIND
    payload = json.dumps({
        "collection": "items",
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

    item_name = item["name"]
    sell_in = item["sell_in"]
    quality = item["quality"]

    """
        Este método hace una petición PUT a la base de datos para actualizar el item.
    """
    url = UPDATEONE
    payload = json.dumps({
        "collection": "items",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {"name": item_name},
        "update": {"$set": {"sell_in": sell_in, 
                            "quality": quality}}
    })

    response = requests.request("PUT", url, headers=get_headers(), data=payload)

    return response

