
import csv
from dataclasses import dataclass
import operator
from typing import List

@dataclass
class LaundryItem:
    name: str
    quantity: int
    unit_type: str #lbs or number of items

@dataclass
class LaundryStore:
    name: str
    prices: dict[str, dict[str, float]]

    def to_dict(self):
       return {
        "Store Name": self.name,
        "Wash-n-Fold - Min Price": self.prices.get("Wash-n-Fold", {}).get("Wash-n-Fold - Min Price", "N/A"),
        "Wash-n-Fold - Min Lbs": self.prices.get("Wash-n-Fold", {}).get("Wash-n-Fold - Min Lbs", "N/A"),
        "Wash-n-Fold - Price Per Lb": self.prices.get("Wash-n-Fold", {}).get("Wash-n-Fold - Price Per Lb", "N/A"),
        "Wash-n-Press - Shirt": self.prices.get("Wash-n-Press", {}).get("Wash-n-Press - Shirt", "N/A"),
        "Dry Cleaning - Shirt": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Shirt", "N/A"),
        "Dry Cleaning - Pants": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Pants", "N/A"),
        "Dry Cleaning - Dress": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Dress", "N/A"),
        "Dry Cleaning - Suit": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Suit", "N/A"),
        "Dry Cleaning - Blouse": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Blouse", "N/A"),
        "Dry Cleaning - Coat": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Coat", "N/A"),
        "Dry Cleaning - Skirt": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Skirt", "N/A"),
        "Dry Cleaning - Sweater": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Sweater", "N/A"),
        "Dry Cleaning - Jacket": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Jacket", "N/A"),
        "Dry Cleaning - Blanket": self.prices.get("Dry Cleaning", {}).get("Dry Cleaning - Blanket", "N/A")
       }

STORES: List[LaundryStore] = []

def application_setup():
    file = "laundry_STORES_UES.csv"
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for row in csvreader:
            name = row[0]
            prices = {
                "Wash-n-Fold": {
                    "Wash-n-Fold - Min Price": float(row[1]) if row[1] else 0.0,
                    "Wash-n-Fold - Min Lbs": float(row[2]) if row[2] else 0.0,
                    "Wash-n-Fold - Price Per Lb": float(row[3]) if row[3] else 0.0
                },
                "Wash-n-Press": {
                    "Wash-n-Press - Shirt": float(row[4]) if row[4] else 0.0
                },
                "Dry Cleaning": {
                    "Dry Cleaning - Shirt": float(row[5]) if row[5] else 0.0,
                    "Dry Cleaning - Pants": float(row[6]) if row[6] else 0.0,
                    "Dry Cleaning - Dress": float(row[7]) if row[7] else 0.0,
                    "Dry Cleaning - Suit": float(row[8]) if row[8] else 0.0,
                    "Dry Cleaning - Blouse": float(row[9]) if row[9] else 0.0,
                    "Dry Cleaning - Coat": float(row[10]) if row[10] else 0.0,
                    "Dry Cleaning - Skirt": float(row[11]) if row[11] else 0.0,
                    "Dry Cleaning - Sweater": float(row[12]) if row[12] else 0.0,
                    "Dry Cleaning - Jacket": float(row[13]) if row[13] else 0.0,
                    "Dry Cleaning - Blanket": float(row[14]) if row[14] else 0.0
                }
            }
            store = LaundryStore(name, prices)
            STORES.append(store)

def get_valid_choice(end):
        while True:
            choice = input("\nPlease select a number: \n")
            if choice in map(str, range(1, end)):
                return choice
            else:
                print("Invalid option. Please enter a valid number.")

def get_valid_float(prompt):
    while True:
        try:
            value = input(prompt[:len(prompt)-2] + " Press 'Enter/Return' if not available / applicable" + prompt[len(prompt)-2: ])
            if value == "":
                value = None
            else:
                value = float(value)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number or None.")

def get_valid_string(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print("Store name cannot be empty. Please enter a valid name.")

def calculate_price():
    items = []

    def wash_n_fold(pounds, prices):
        min_lbs = prices["Wash-n-Fold - Min Lbs"]
        price_per_lb = prices[ "Wash-n-Fold - Price Per Lb"]
        min_price = prices["Wash-n-Fold - Min Price"]
        if not min_lbs and not min_price:
            cost = price_per_lb * pounds
        elif float(pounds) > min_lbs:
            excess_pounds = float(pounds) - min_lbs
            cost = (excess_pounds * price_per_lb) + min_price
        else: 
            cost = min_price
        return cost
    
    def calculate(items):
        totals = {}
        min_price = float("inf")
        for store in STORES:
            price = 0
            for item in items:
                if item.name == "Wash-n-Fold":
                    cost = wash_n_fold(item.quantity, store.prices["Wash-n-Fold"])
                    price += cost
                # breakpoint()
                elif "Wash-n-Press" in item.name:
                    if not store.prices["Wash-n-Press"]["Wash-n-Press - Shirt"]:
                        price = None
                        break
                    cost = float(item.quantity) * store.prices["Wash-n-Press"]["Wash-n-Press - Shirt"]
                    price += cost
                else:
                    try:
                        if not store.prices["Dry Cleaning"][item.name]:
                            price = None
                            break
                        cost = float(item.quantity) * store.prices["Dry Cleaning"][item.name]
                        price += cost
                    except KeyError:
                        print(f"Service '{item.name}' not available at {store.name}")
                        continue
            totals.update({store.name: price})
        irrelevant_stores = [store for store in STORES if totals.get(store.name) is None]
        for store in irrelevant_stores:
            totals.pop(store.name)
        sorted_totals = sorted(totals.items(), key=operator.itemgetter(1))
        return sorted_totals, irrelevant_stores
                    
    def user_input(name):
        while True:
            try:
                quantity = float(input("\nPlease enter the quantity: \n"))
                item = LaundryItem(name, quantity, "items")
                items.append(item)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    message = """Available services:
    1. Wash-n-Fold
    2. Wash-n-Press - Shirt
    3. Dry Cleaning - Shirt
    4. Dry Cleaning - Pants
    5. Dry Cleaning - Dress
    6. Dry Cleaning - Suit
    7. Dry Cleaning - Blouse
    8. Dry Cleaning - Coat
    9. Dry Cleaning - Skirt
    10. Dry Cleaning - Sweater
    11. Dry Cleaning - Jacket
    12. Dry Cleaning - Blanket
    13. Calculate
    14. Exit
    """ 
    print(message)

    while True:
        choice = get_valid_choice(15)
        match choice:
            case "1":
                while True:
                    pounds = input("\nPlease enter the number of pounds:\n")
                    if pounds in map(str, range(1, 100)):
                        item = LaundryItem("Wash-n-Fold", float(pounds), "lbs")
                        items.append(item)
                        break
                    else:
                        print("Invalid option. Please select a valid number from the list.")
            case "2":
                user_input("Wash-n-Press - Shirt")
            case "3":
                user_input("Dry Cleaning - Shirt")
            case "4":
                user_input("Dry Cleaning - Pants")
            case "5":
                user_input("Dry Cleaning - Dress")
            case "6":
                user_input("Dry Cleaning - Suit")
            case "7":
                user_input("Dry Cleaning - Blouse")
            case "8":
                user_input("Dry Cleaning - Coat")
            case "9":
                user_input("Dry Cleaning - Skirt")
            case "10":
                user_input("Dry Cleaning - Sweater")
            case "11":
                user_input("Dry Cleaning - Jacket")
            case "12":
                user_input("Dry Cleaning - Blanket")
            case "13":
                totals, irrelevant_store = calculate(items)
                print("\nHere are the results:\n")
                for store in totals:
                    print(store[0] + ": $" + str(store[1]))
                print(", ".join([store.name for store in irrelevant_store]), " Stores don't have services you requested.\n")
                return
            case "14":
                exit()
            case _:
                break

def add_store():
    store_name = input("\nEnter the name of the new store: \n")

    print("Please enter the pricing information for the new store:\n")
    
    wash_n_fold_min_price = get_valid_float("Enter the minimum price for Wash-n-Fold: ")
    wash_n_fold_min_lbs = get_valid_float("Enter the minimum lbs for Wash-n-Fold: ")
    wash_n_fold_price_per_lb = get_valid_float("Enter the price per lb for Wash-n-Fold: ")
    wash_n_press_shirt_price = get_valid_float("Enter the price for Wash-n-Press - Shirt: ")
    dry_cleaning_shirt = get_valid_float("Enter the price for Dry Cleaning - Shirt: ")
    dry_cleaning_pants = get_valid_float("Enter the price for Dry Cleaning - Pants: ")
    dry_cleaning_dress = get_valid_float("Enter the price for Dry Cleaning - Dress: ")
    dry_cleaning_suit = get_valid_float("Enter the price for Dry Cleaning - Suit: ")
    dry_cleaning_blouse = get_valid_float("Enter the price for Dry Cleaning - Blouse: ")
    dry_cleaning_coat = get_valid_float("Enter the price for Dry Cleaning - Coat: ")
    dry_cleaning_skirt = get_valid_float("Enter the price for Dry Cleaning - Skirt: ")
    dry_cleaning_sweater = get_valid_float("Enter the price for Dry Cleaning - Sweater: ")
    dry_cleaning_jacket = get_valid_float("Enter the price for Dry Cleaning - Jacket: ")
    dry_cleaning_blanket = get_valid_float("Enter the price for Dry Cleaning - Blanket: ")

    prices = {
        "Wash-n-Fold": {
            "Wash-n-Fold - Min Price": wash_n_fold_min_price,
            "Wash-n-Fold - Min Lbs": wash_n_fold_min_lbs,
            "Wash-n-Fold - Price Per Lb": wash_n_fold_price_per_lb
        },
        "Wash-n-Press": {
            "Wash-n-Press - Shirt": wash_n_press_shirt_price
        },
        "Dry Cleaning": {
            "Dry Cleaning - Shirt": dry_cleaning_shirt,
            "Dry Cleaning - Pants": dry_cleaning_pants,
            "Dry Cleaning - Dress": dry_cleaning_dress,
            "Dry Cleaning - Suit": dry_cleaning_suit,
            "Dry Cleaning - Blouse": dry_cleaning_blouse,
            "Dry Cleaning - Coat": dry_cleaning_coat,
            "Dry Cleaning - Skirt": dry_cleaning_skirt,
            "Dry Cleaning - Sweater": dry_cleaning_sweater,
            "Dry Cleaning - Jacket": dry_cleaning_jacket,
            "Dry Cleaning - Blanket": dry_cleaning_blanket
        }
    }

    new_store = LaundryStore(name=store_name, prices=prices)
    STORES.append(new_store)

    print(f"New store '{store_name}' has been successfully added.")
                
def update_store():
    print('\nLets update a store!\n\nHere are the stores you can choose to update:')
    count = 1
    for store in STORES:
        print(str(count) + ". " + store.name)
        count += 1
    store_idx = int(get_valid_choice(len(STORES)+1)) - 1   
    message = """Here are the available services to update:
        1. Wash-n-Fold - Min Price
        2. Wash-n-Fold - Min Lbs
        3. Wash-n-Fold - Price Per Lb
        4. Wash-n-Press - Shirt
        5. Dry Cleaning - Shirt
        6. Dry Cleaning - Pants
        7. Dry Cleaning - Dress
        8. Dry Cleaning - Suit
        9. Dry Cleaning - Blouse
        10. Dry Cleaning - Coat
        11. Dry Cleaning - Skirt
        12. Dry Cleaning - Sweater
        13. Dry Cleaning - Jacket
        14. Dry Cleaning - Blanket
        15. Exit"""
    print(message)
    while True:
        store = STORES[store_idx]
        choice = get_valid_choice(16)
        match choice:
            case "1":
                store.prices["Wash-n-Fold"]["Wash-n-Fold - Min Price"] = get_valid_float("Please enter a new value:\n")
            case "2":
                store.prices["Wash-n-Fold"][ "Wash-n-Fold - Min Lbs"] = get_valid_float("Please enter a new value:\n")
            case "3":
                store.prices["Wash-n-Fold"]["Wash-n-Fold - Price Per Lb"] = get_valid_float("Please enter a new value:\n")
            case "4":
                store.prices["Wash-n-Press"]["Wash-n-Press - Shirt"] = get_valid_float("Please enter a new value:\n")
            case "5":
                store.prices["Dry Cleaning"]["Dry Cleaning - Shirt"] = get_valid_float("Please enter a new value:\n")
            case "6":
                store.prices["Dry Cleaning"]["Dry Cleaning - Pants"] = get_valid_float("Please enter a new value:\n")
            case "7":
                store.prices["Dry Cleaning"][ "Dry Cleaning - Dress"] = get_valid_float("Please enter a new value:\n")
            case "8":
                store.prices["Dry Cleaning"]["Dry Cleaning - Suit"] = get_valid_float("Please enter a new value:\n")
            case "9":
                store.prices["Dry Cleaning"]["Dry Cleaning - Blouse"] = get_valid_float("Please enter a new value:\n")
            case "10":
                store.prices["Dry Cleaning"][ "Dry Cleaning - Coat"] = get_valid_float("Please enter a new value:\n")
            case "11":
                store.prices["Dry Cleaning"]["Dry Cleaning - Skirt"] = get_valid_float("Please enter a new value:\n")
            case "12":
                store.prices["Dry Cleaning"]["Dry Cleaning - Sweater"] = get_valid_float("Please enter a new value:\n")
            case "13":
                store.prices["Dry Cleaning"]["Dry Cleaning - Jacket"] = get_valid_float("Please enter a new value:\n")
            case "14":
                store.prices["Dry Cleaning"]["Dry Cleaning - Blanket"] = get_valid_float("Please enter a new value:\n")
            case "15":
                return
            case _:
                return

def delete_store():
    print("\nLet's delete a store!\n\nHere are the stores you can choose to delete:")
    count = 1
    for store in STORES:
        print(str(count) + ". " + store.name)
        count += 1
    store_idx = int(get_valid_choice(len(STORES)+1)) - 1
    store = STORES[store_idx]
    STORES.remove(store)
    print(f"\nYour store '{store.name}' has been deleted.\n\nHere are your remaining stores:\n")
    count = 1
    for store in STORES:
        print(str(count) + ". " + store.name)
        count += 1

def exit_program():
    fieldnames = ["Store Name", "Wash-n-Fold - Min Price", "Wash-n-Fold - Min Lbs", "Wash-n-Fold - Price Per Lb", 
                  "Wash-n-Press - Shirt", "Dry Cleaning - Shirt", "Dry Cleaning - Pants", "Dry Cleaning - Dress", 
                  "Dry Cleaning - Suit", "Dry Cleaning - Blouse", "Dry Cleaning - Coat", "Dry Cleaning - Skirt", 
                  "Dry Cleaning - Sweater", "Dry Cleaning - Jacket", "Dry Cleaning - Blanket"]

    with open("laundry_STORES_UES.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for store in STORES:
            store_dict = store.to_dict()
            writer.writerow(store_dict)
    print("\nThanks for using Laundry Decider! Goodbye...")
    exit()

def main():
    def print_clean_choice():
        print("""
##############################################################################################################
##############################################################################################################
##                                                                                                          ##
##    L      AAAAA   U   U  N   N  DDDD   RRRR   Y   Y      DDDD  EEEEE  CCCC  III  DDDD   EEEEE  RRRR      ##
##    L      A   A   U   U  NN  N  D   D  R   R   Y Y       D   D E     C       I   D   D  E      R   R     ##
##    L      AAAAA   U   U  N N N  D   D  RRRR     Y        D   D EEEE  C       I   D   D  EEEE   RRRR      ##
##    L      A   A   U   U  N  NN  D   D  R  R     Y        D   D E     C       I   D   D  E      R  R      ##
##    LLLLL  A   A    UUU   N   N  DDDD   R   R    Y        DDDD  EEEEE  CCCC  III  DDDD   EEEEE  R   R     ##
##                                                                                                          ##
##############################################################################################################
##############################################################################################################
""")


    application_setup()
    welcome_message = "\nWelcome to Laundry Decider!\n"
    print_clean_choice()
    print(welcome_message)
    while True:
        input_mesage = """Options:
        1. Calculate prices
        2. Add Store
        3. Update Store
        4. Delete Store
        5. Exit
        """
        print(input_mesage)
        choice = input("Please select an option: \n")
        match choice:
            case "1":
                print("\nLet's calcuate the price! Have your laundry ready...\n")
                calculate_price()
            case "2":
                print("\nLet's add a store!\n")
                add_store()
            case "3":
                print("\nLet's update a store!\n")
                update_store()
            case "4":
                print("\nLet's delete a store!\n")
                delete_store()
            case "5":
                exit_program()
            case _:
                break

if (__name__) == "__main__":
    main()