#API 1: Get laundry stores within a radius of the user's location
@app.route('/read_laundry_store_price/<int:store_id>', methods=['GET'])
def read_laundry_store_prices(store_id):
    pass

#API 2: Get pricing for a specific laundry store
def read_laundry_store_price(store_id):
     pass

#API 3: Get list of laundry stores sorted by price



if __name__ == "__main__":
     app.run(debug=True, host='local_host', port=8080)