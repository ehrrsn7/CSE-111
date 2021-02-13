"""
Lab 04 - reciept.py
Author: Elijah Harrison
Instructor: John Reading
January 19th, 2021
"""

""" import / define """
import csv
from datetime import datetime

STORE_NAME          = "Inkom Emporium"
PRODUCTS_FILNAME    = "products.csv"
REQUEST_FILNAME     = "request.csv"

SALES_TAX_RATE      = 0.06


""" main """
def main():
    print_store_name()

    products = import_csv(PRODUCTS_FILNAME, csv_to_products)
    request  = import_csv(REQUEST_FILNAME,  csv_to_request)

    display_receipt(request, products)


""" display store name """
def print_store_name():
    print(STORE_NAME, '\n')

""" handling csv files / contents """
def import_csv(filename:str, callback):
    # open file
    try:
        with open(filename) as file:
            # initialize reader
            reader = csv.reader(file)

            # manipulate data
            return callback(reader)
    
    # handle missing file error
    except OSError as msg: print(msg)

class product:
    def __init__(self, product_id, product_name, product_price):
        self.id     = product_id
        self.name   = product_name
        self.price  = product_price

def csv_to_products(reader):
    products = []
    next(reader)
    for line in reader:
        products.append(product(line[0], line[1], line[2]))
    return products

class request_item:
    def __init__(self, product_id, amount):
        self.product_id = product_id
        self.amount     = amount

def csv_to_request(reader):
    request = []
    next(reader)
    for line in reader:
        request.append(request_item(line[0], line[1]))
    return request

""" display receipt """
def display_receipt(request:list, products:list):

    # initialize variables
    total_number_of_items   = int()
    subtotal                = float()
    sales_tax               = float()
    grand_total             = float()

    # parse through request and display items
    for item in request:

        # get request information
        product_name = ""
        item_amount = int(item.amount)
        product_total_price = float()
    
        # get product information
        for product in products:
            if product.id == item.product_id:
                product_name = product.name + ": "
                product_total_price = item_amount * float(product.price)

        # display item information        
        print(f"{product_name:18} {item_amount} @ {product_total_price:.2f}")

        # update totals
        total_number_of_items += item_amount
        subtotal += product_total_price

    # get totals
    sales_tax = subtotal * SALES_TAX_RATE
    grand_total = subtotal + sales_tax

    print(f"\nNumber of Items: {total_number_of_items :>10}")
    print(f"Subtotal:          {subtotal    :>8.2f}")
    print(f"Sales tax:         {sales_tax   :>8.2f}")
    print(f"Total:             {grand_total :>8.2f}")
    
    print(f"\nThank you for shopping at the {STORE_NAME}.")
    print(datetime.now().strftime("%a %b %-d %-H:%-M:%-S %-Y"))



""" run program """
if __name__ == "__main__": main()
