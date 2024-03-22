from flask import Flask, request, jsonify
import os
import time
import logging
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
cors = CORS(app)

def dbCall():
    time.sleep(3)
    values = ["a", "b", "c", "d", "c"]
    for value in values:
     print("print: ", value)
     app.logger.info("logger: %s", value)
     #app.logger.debug("logger: %s", value)

    productsdb = [
        { 'id': 0, 'title': 'Apples', 'price': 1.20 },
        { 'id': 1, 'title': 'Bananas', 'price': 1.45 },
        { 'id': 2, 'title': 'Grapes', 'price': 5.12 },
        { 'id': 3, 'title': 'Blackberries', 'price': 2.52 }
    ]
    return productsdb

@app.route('/', methods=['GET'])
def home():
    products = dbCall()
    return jsonify(products)

if __name__ == '__main__':
    port= os.environ.get('PORT')
    app.run(host='0.0.0.0', debug=True, port=port)
