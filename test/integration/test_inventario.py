from app import app
from flask import jsonify

import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.mark.home
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bienvenido a mi API" in response.data

@pytest.mark.get_items
def test_get_items(client):
    response = client.get('/inventario')
    assert response.status_code == 200
    assert isinstance(response.json, dict)