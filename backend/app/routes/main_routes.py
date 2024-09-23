from flask import Blueprint, jsonify, request
from ..database.database import db
from ..database.models import LaundryStore, Address, Hours, WashAndFoldPrice, Reviews, DryCleaningPrice


main_bp = Blueprint('main', __name__)


#API 1: Get laundry stores within a radius of the user's location
@main_bp.route('/read_laundry_store_price', methods=['GET'])
def read_laundry_store_prices(store_id):
    pass

#API 2: Get pricing for a specific laundry store

@main_bp.route('/read_laundry_store_price', methods=['GET'])
def read_laundry_store_price(store_id):
     #Query laundry store, wash_and_fold price, and dry_cleaning_price
     store = LaundryStore.query.get_or404(id)
     wash_and_fold = store.wash_and_fold_price
     dry_cleaning = store.dry_cleaning_price

     #Prepare info to return in JSON format
     pricing_info = {
          "store_name": store.name,
          "wash_and_fold_price": {
               "min_price": wash_and_fold.min_price, 
               "min_pounds": wash_and_fold.min_pounds, 
               "price_per_pound": wash_and_fold.price_per_pound
               },
          "dry_cleaning_price": {
               "dress": dry_cleaning.dress,
               "sweater": dry_cleaning.sweater,
               "skirt": dry_cleaning.skirt,
               "shorts": dry_cleaning.shorts,
               "outer_jacket": dry_cleaning.outer_jacket,
               "coat": dry_cleaning.coat,
               "jump_suit": dry_cleaning.jump_suit,
               "launder_shirt": dry_cleaning.launder_shirt,
               "dry_clean_shirt": dry_cleaning.dry_clean_shirt,
               "blouse": dry_cleaning.blouse,
               "pants": dry_cleaning.pants,
               "suit_jacket": dry_cleaning.suit_jacket,
               "two_piece_suit": dry_cleaning.two_piece_suit,
               "robe": dry_cleaning.robe,
               "scarf": dry_cleaning.scarf,
               "tie": dry_cleaning.tie,
               "tuxedo": dry_cleaning.tuxedo,
               "three_piece_suit": dry_cleaning.three_piece_suit
          }
     }

     #Return pricing info as JSON
     return jsonify(pricing_info)


#API 3: Get list of laundry stores sorted by price

@main_bp.route('/sort_laundry_stores_on_price', methods=['GET'])
def sort_laundry_stores_on_price():
     pass
