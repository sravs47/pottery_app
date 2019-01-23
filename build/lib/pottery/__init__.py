from flask import Flask,Blueprint
from pottery.resources.product_catalog import potteryapp
# object creation
app = Flask(__name__)
app.register_blueprint(potteryapp)


import pottery.views
import pottery.resources.product_catalog
import pottery.models.products
from pymodm import connect
import logging

# Db connectin
# If you are running this inside docker and want to connect to mongo on the host machine then DNS is 'host.docker.internal'
connect("mongodb://localhost:27017/pottery")

name ="pottery"

# temporary products
# create list of product models.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# file_handler = logging.FileHandler('pottery/logs/product_catalog.log')
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)