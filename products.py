import csv 

def all_products():

    with open('products.csv') as csv_file:
        file = csv.reader(csv_file)
        for row in file:
            print(row)

# all_products()

def add_product():
    user_id_input = input("Please enter the product ID you want: ")
    user_name_input = input("Please enter the product name: ")
    user_amount_input = int(input("Please enter the product amount: "))
    assert user_amount_input < 100, "Amount cannot exceed 100."
    user_price_input = float(input("Please enter the product price: "))
    added_product_list= [user_id_input, user_name_input, user_amount_input,user_price_input]
    print(f"The new product is: ",added_product_list)
    with open("products.csv", "a+", newline="") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(added_product_list) 

# add_product()

def delete_product():
    with open('products.csv', 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        product_id_delete = input("enter the product id to delete: ")
        for line in lines:
            if not product_id_delete in line.split(',')[0]:
                file.write(line)
        file.truncate()
        print("Product has been deleted.")

def update_product():
    user_input_update = input("Please enter the product ID you want to update details: ")
    with open('products.csv', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if user_input_update not in line.split(','):
                file.write(line)
        file.truncate()
                
        user_name_input_update = input("Please enter the new product name you want: ")
        user_amount_input_update = input("Please enter the new product amount you want: ")
        user_price_input_update = input("Please enter the new product amount you want: ")
        update_product_list= [user_input_update, user_name_input_update, user_amount_input_update, user_price_input_update]
        print(f'The product now becomes: {update_product_list}')
        with open("products.csv", "a+", newline="") as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(update_product_list) 