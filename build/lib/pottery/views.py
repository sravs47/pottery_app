from flask import Blueprint
from pottery import app
potteryapp = Blueprint('potteryapp',__name__)

@potteryapp.route('/')
def index():
    return 'Hello world'
