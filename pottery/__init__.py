from flask import Flask
# object creation
app = Flask(__name__)

import pottery.views
import pottery.resources.product_catalog
import pottery.models.products
from pymodm import connect

# Db connectin
connect("mongodb://localhost:27017/pottery")


import logging

# temporary products
# create list of product models.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('pottery/logs/product_catalog.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


if __name__ == '__main__':
    app.run(debug=True)