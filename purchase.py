import csv

from numpy import product
from make_purchase import make_purchase

from products import all_products, search_product

purchases_made = []

space_small = """
              """

space_big = """
        
        """

with open('products.csv','r+') as csv_file:
    file_product = csv.reader(csv_file)
    data_product = list(file_product)

with open('customers.csv','r+') as csv_file:
    file_customer = csv.reader(csv_file)
    data_customer = list(file_customer)


# def not_zero(validate):
#     # checks that the amount given is not zero or less than 0.
#     if validate < 0:
#         "You have entered a value less than zero. "


def purchase_item():
    customer_exists = False
    product_exists= False
    total_purchase = 0
    # print(space)
    customer_id_from_user = input("Enter customer id to purchase: ")
    for customer in range(len(data_customer)):
        if customer_id_from_user in data_customer[customer][0]:
            customer_exists = True
            print("Customer name is: ", data_customer[customer][1])

    print(space_small)
    product_id_from_user = input("Enter product id to purchase: ")
    # check if id in product exists
    for product in range(len(data_product)):
        if product_id_from_user == data_product[product][0]:
            product_exists = True
            print(space_small)
            print(f"The product is:  {data_product[product][1]} \nThere are {data_product[product][2]} in the store.")

    if customer_exists and product_exists:
        print(space_small)
        purchase_item_quantity = int(input("Enter the quantity you would like to purchase for the product: "))
        space_small
        for i in range(len(data_product)):
            if product_id_from_user in data_product[i][0]:
                name = data_product[i][1]
                quantity = int(data_product[i][2])
                price = float(data_product[i][3])
                if purchase_item_quantity > quantity:
                    print(name + "can't be sold because the quantity in stock is lower than ordered."+str(quantity)+'\nPlace another quantity for the order.')
                    purchase_item()
                else:
                      cost = purchase_item_quantity * price

                      purchases_made.append([product_id_from_user, name, quantity, cost])
                      print(purchases_made)

                      another_purchase = input("""
                      1. Check out with sale.
                      2. Make another purchase.

                      Your selection:  """)

                      if another_purchase == "1":
                          checking_out()
                      elif another_purchase == "2":
                        purchase_item()

def update_stock():
    new_list_item = []
    updated_list_item = []
    for purchase in range(len(purchases_made)):
        update_ID = purchases_made[purchase][0]
        quantity = purchases_made[purchase][3]

        for product in range(len(data_product)):
            if update_ID in data_product[product][0]:
                new_list_item.append(product)
                print(new_list_item)



def checking_out():
    total_spent = 0
    # print(space)
    for purchase in range(len(purchases_made)):
        total_spent += purchases_made[purchase][3]
    print(space_big)
    print(f'You have spent {total_spent}')

    customer_pay = float(input("Amount of cash given:"))
    if customer_pay < total_spent:
            print(f"""You have entered insufficient funds.
                        Total amount due is {total_spent}""")
            
            customer_pay_2 = input("""
                                    1. enter another cash amount.
                                    2. Exit
                                    
                                    Select an option: """)
            
            if customer_pay_2 == "1":
                checking_out()
            else:
                print(space_big)
                print("Exiting")
        
    else:
            balance = customer_pay - total_spent
            # print(space)
            print("Your purchase receipt is as follows:")
            print(f"""
                Total Spent: {total_spent}
                Paid: {customer_pay}
                Balance: {balance}
                """)
            # print(space)
            update_stock()



            # updated stock




purchase_item()
