import os
from flask import Flask
from pottery.resources.product_catalog import potteryapp
from pottery.resources.user_account_catalog import useraccountapp

# object creation
app = Flask(__name__)
app.register_blueprint(potteryapp)
app.register_blueprint(useraccountapp)


@app.before_request
def before_request():
    print('In the init before')

import pottery.views
import pottery.resources.product_catalog
import pottery.resources.user_account_catalog
import pottery.models.products
import pottery.models.accounts
from pymodm import connect
import logging

# Db connectin
# If you are running this inside docker and want to connect to mongo on the host machine then DNS is 'host.docker.internal'
# If you are using docker compose use the image name of the mongo with the port 'mongo:27017'
connect("mongodb://localhost:27017/pottery")
# connect("mongodb://mongo:27017/pottery")
# connect(f'mongodb://{os.environ["MONGO_HOST"]}:27017/pottery')
name = "pottery"

# temporary products
# create list of product models.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# file_handler = logging.FileHandler('pottery/logs/product_catalog.log')
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
