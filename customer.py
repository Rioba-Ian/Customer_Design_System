import csv

def all_customers():
    
    with open('customers.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            
            print(row)

new_customers = ['3', 'riri', 'Juja']

def check_customer(parsed_list):
    parsed_ID = parsed_list[0]
    with open('customers.csv') as fp:
        csv_reader = csv.reader(fp)
        data = list(csv_reader)
        # print(data)
        for i in range(len(data)):
            if parsed_ID in data[i]:
                print("Customer exists")

# check_customer(new_customers)

def delete_customer():
    with open('customers.csv', 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        user_id_delete = input("enter the customer id to delete: ")
        for line in lines:
            if not user_id_delete in line.split(',')[0]:
                file.write(line)
        file.truncate()
        print("Customer has been deleted.")

# delete_customer()

def add_customer():
    user_id_input = input("Please enter the customer ID you want to add: ")
    user_name_input = input("Please enter the customer's you want to add(e.g John): ")
    user_address_input = input("Please enter the customer's address (e.g Mswambweni) you want to add: ")
    added_customer_list= [user_id_input, user_name_input, user_address_input]
    print(f"The new customer is: ",added_customer_list)
    check_customer(parsed_list=added_customer_list)
    with open("customers.csv", "a+", newline="") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(added_customer_list) 
    

# add_customer()

def update_customer():
    user_input_update = input("Please enter the customer ID you want to update details: ")
    with open('customers.csv', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if user_input_update not in line.split(','):
                file.write(line)
        file.truncate()
                
        user_name_input_update = input("Please enter the new customer's name you want(e.g John): ")
        user_address_input_update = input("Please enter the new customer's address (e.g Mswambweni) you want: ")
        update_customer_list= [user_input_update, user_name_input_update, user_address_input_update]
        print(f'The customer now becomes: {update_customer_list}')
        with open("customers.csv", "a+", newline="") as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(update_customer_list) 

update_customer()