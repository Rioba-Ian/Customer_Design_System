from customer import all_customers, delete_customer, add_customer, update_customer
from products import all_products, add_product,delete_product
def menu():
    while True:
        print("""

        CUSTOMER
        1. Add a customer.
        2. Delete a customer. 
        3. View customers.
        4. Update a customer's records.

        PRODUCTS
        5. Insert a product.
        6. View all the products. 
        7. Delete a product in products. 
        8. Modify/update a product. 
        9. Exit/Quit.        
        """)
        ans = input("Enter your selection: ")
        if ans == '1':
            print("You have selected Add a customer.")
            add_customer()
        elif ans == '2':
            print("You have selected delete a customer.")
            delete_customer()
        elif ans == '3':
            print("You have selected view customers")
            all_customers()
        elif ans == '4':
            print("You have selected Update customer's record")
            update_customer()
        elif ans == '5':
            print("You have selected Update customer's record")
            add_product()
        elif ans == '6':
            print("You have selected Update customer's record")
            all_products()
        elif ans == '7':
            print("You have selected Update customer's record")
            delete_product()
        elif ans == '9':
            print("You have exited the program.")
            break
        else:
            print("Please enter a valid selection")
            continue
        

menu()