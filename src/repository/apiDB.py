
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from dotenv import dotenv_values
import requests
import json
import os

'''
    Uso el método dotenv_values para cargar las variables de entorno del archivo .env
'''

config = dotenv_values()
KEY = config['KEY']
URI = config['URI']

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




def inventario():
    """
        Este método hace una petición POST a la base de datos sin filtro
        Return: Toda la información que contiene la base de datos en formato JSON dentro de una lista
    """

    url = URI
    payload = json.dumps({
        "collection": "items",
        "database": "Ollivanders-shop",
        "dataSource": "OllivandersCluster",
        "filter": {},
    })

    response = requests.request("POST", url, headers=get_headers(), data=payload)
    return response








def item(item_name):
    """
        Este método hace una petición POST a la base de datos buscando por
        Return: Las ocurrencias que coincidan con algún documento de la 
        la base de datos en formato JSON detro de una lista
    """
        
    url = URI
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

