from flask import Blueprint, jsonify, request
from app.database.database_connector import db
from app.database.models import LaundryStore, Address, Hours, WashAndFoldPrice, Reviews, DryCleaningPrice


main_bp = Blueprint('main', __name__)

#GET Request - Search Laundry Store by Name
@main_bp.route('/getLaundryStore', methods=['GET'])
def getLaundryStore(): 
   try:
        data = request.get_json()
        if not data or 'name' not in data:
             return jsonify({"error": "A 'name' field is required in the JSON body"}), 400
        name = data['name']
        stores = LaundryStore.query.filter((LaundryStore.name.ilike(f"%{name}%"))).all()
        if not stores:
             return jsonify({"message": "No stores found matching name"}), 404
        stores_info = []

        for store in stores:
          reviews = store.reviews
          if reviews:
               avg_rating = sum(review.rating for review in reviews) / len(reviews)
          else:
               avg_rating = None
          
          store_info = {
               "name": store.name,
               "id": store.id,
               "phone number": store.phone_number,
               "address": {
                    "address_1": store.address.address_1,
                    "address_2": store.address.address_2,
                    "city": store.address.city,
                    "state": store.address.state,
                    "zip_code": store.address.zip_code
                    } if store.address else None,
               "hours": {
                    "mon": store.hours.mon,
                    "tue": store.hours.tue,
                    "wed": store.hours.wed,
                    "thur": store.hours.thur,
                    "fri": store.hours.fri,
                    "sat": store.hours.sat,
                    "sun": store.hours.sun
               } if store.hours else None,
               "avg_rating": avg_rating
          }
          stores_info.append(store_info)


        return jsonify({"stores": stores_info}), 200
   except Exception as e:
        return jsonify({"error": "Invalid JSON input"}), 400
#    return jsonify({"name": name})

#GET Request - Search Laundry Store by ID
@main_bp.route('/getLaundryStoreID', methods=['GET'])
def getLaundryStoreID():
     try:
          data = request.get_json()
          if not data or 'id' not in data:
               return jsonify({"error": "An 'id' field is required in the JSON body"}), 400
          ids = data['id']
          stores = LaundryStore.query.filter(LaundryStore.id.in_(ids)).all()
          
          if not stores:
               return jsonify({"error": "No stores found matching input"}), 404
          
          stores_info = []
          for store in stores:
               reviews = store.reviews
               if reviews:
                    avg_rating = sum(review.rating for review in reviews) / len(reviews)
               else:
                    avg_rating = None
               
               store_info = {
                    "name": store.name,
                    "id": store.id,
                    "phone number": store.phone_number,
                    "address": {
                         "address_1": store.address.address_1,
                         "address_2": store.address.address_2,
                         "city": store.address.city,
                         "state": store.address.state,
                         "zip_code": store.address.zip_code
                         } if store.address else None,
                    "hours": {
                         "mon": store.hours.mon,
                         "tue": store.hours.tue,
                         "wed": store.hours.wed,
                         "thur": store.hours.thur,
                         "fri": store.hours.fri,
                         "sat": store.hours.sat,
                         "sun": store.hours.sun
                    } if store.hours else None,
                    "avg_rating": avg_rating
               }
               stores_info.append(store_info)
          return jsonify({"stores": stores_info}), 200
     
     except Exception as e:
        return jsonify({"error": "Invalid JSON input"}), 400

#Get pricing for a specific laundry store
@main_bp.route('/read_laundry_store_price/<int:store_id>', methods=['GET'])
def read_laundry_store_price(store_id):
     #Placeholder
     # return jsonify({"message": "List of laundry store pricing"}), 200
     #Query laundry store, wash_and_fold price, and dry_cleaning_price
     store = LaundryStore.query.get_or_404(store_id)
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
     return jsonify(pricing_info), 200

#GET Request Placeholder
@main_bp.route('/read_laundry_store/<int:store_id>', methods=['GET'])
def read_laundry_store(store_id):
    #placeholder
    return jsonify({"message": "Laundry store"}), 200

#POST Request Placeholder
@main_bp.route('/create_laundry_store', methods=['POST'])
def create_laundry_store():
     #Placeholder response for POST request
     data = request.json
     return jsonify({"message": "Placeholder: Laundry store creatred", "data": data}), 201

#PUT Request Placeholder
@main_bp.route('/update_laundry_store/<int:store_id>', methods=['PUT'])
def update_laundry_store(store_id):
     #Placeholder response for PUT request
     data = request.json
     return jsonify({"message": f"Placeholder: Laundry store with ID {store_id} updated", "updated_data": data}), 200

#PATCH Request Placeholder
@main_bp.route('/partial_update_laundry_store/<int:store_id>', methods=['PATCH'])
def partial_update_laundry_store(store_id):
     data = request.json
     return jsonify({'message': f"Placeholder: Partially updated laundry store with ID {store_id}", "patched_data": data}), 200

#DELETE Request Placeholder
@main_bp.route('/delete_laundry_store/<int:store_id>', methods=['DELETE'])
def delete_laundry_store(store_id):
     #Placeholder response for DELETE request
     return jsonify({'message': f"Placeholder: Laundry store with ID {store_id} deleted"}), 204