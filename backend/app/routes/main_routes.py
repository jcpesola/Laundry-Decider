from flask import Blueprint, jsonify, request


main_bp = Blueprint('main', __name__)


#API 1: Get laundry stores within a radius of the user's location
@main_bp.route('/read_laundry_store_price', methods=['GET'])
def read_laundry_store_prices(store_id):
    pass

#API 2: Get pricing for a specific laundry store

@main_bp.route('/read_laundry_store_price', methods=['GET'])
def read_laundry_store_price(store_id):
     pass

#API 3: Get list of laundry stores sorted by price

@main_bp.route('/sort_laundry_stores_on_price', methods=['GET'])
def sort_laundry_stores_on_price():
     pass
