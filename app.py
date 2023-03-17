from flask import Flask
from src.repository.apiDB import connection_database


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/inventario HTTP/1.1')
def inventario():
    return connection_database



if __name__=="__main__":
    app.run(port=5000)