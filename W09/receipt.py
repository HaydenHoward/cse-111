import csv
from datetime import datetime
import random

def main():
    try:
        stores = ['Inkom Emporium', 'Safeway', 'Costco', 'Walmart']
        store = random.choice(stores)
        product_num = 0
        quantity = 1
        product_name = 1
        product_price = 2

        products_dict = read_dict("products.csv", product_num)
        # print(f"Products \n{products_dict}")
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            print(store)
            print()
            quant_sum = 0
            subtotal = 0

            for row_list in reader:
                # req_quant = float(row_list[quantity])
                prod_num = row_list[product_num]
                # quant_sum += req_quant
                if prod_num in products_dict:
                    req_quant = float(row_list[quantity])
                    # # prod_num = row_list[product_num]
                    quant_sum += req_quant

                    prod = products_dict[prod_num]
                    prod_name = prod[product_name]
                    prod_price = prod[product_price]
                    print(f"{prod_name}: {req_quant} @ {prod_price}")
                    subtotal += float(prod_price) * req_quant
                    subtotal = round(subtotal, 2)
            sales_tax = round(subtotal * .06, 2)
            total = sales_tax + subtotal

            print()
            print(f"Number of Items: {quant_sum}")
            print(f"Subtotal: {subtotal}")
            print(f"Sales Tax: {sales_tax}")
            print(f"Total: {total}")
            print()
            print(f"Thank you for shopping at the {store}.")
            current_date = datetime.now()
            print(f"{current_date:%a %b %d %X %Y}")
            #day_of_week Month date time year

    except FileNotFoundError as not_found_err:
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        
    except PermissionError as perm_err:
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        
    except KeyError as key_err:
        print()
        print(type(key_err).__name__, key_err, sep=": ")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """


    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary



if __name__ == "__main__":
    main()