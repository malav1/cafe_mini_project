#connection will stay open till the end. object is created at the start and connection is closed when the application ends. its expensive to keep opening and closing

import ast
from funcs import int_input_limit, input_check, print_sql, food_add_sql, courier_add_sql, delete_sql, close_connection, update_food_sql, update_courier_sql, order_add_sql, update_order_sql, orders_delete_sql

# user input for welcome menu- while loop to come back to welcome menu.
continue_welcome=True
while continue_welcome:


    print(""""\n\n
                🧂LULU'S CAFE - ADMIN ACCESS🧂 
                    ------------------
                      0️⃣ Exit 
                      1️⃣ Food Menu 
                      2️⃣ Couriers Menu
                      3️⃣ Orders Menu
""")

    usr_welcome=int_input_limit("please enter 0️⃣, 1️⃣, 2️⃣ or 3️⃣ : ",3)

    #exit
    if usr_welcome==0: break


    #product menu
    if usr_welcome==1:
        print("""\n\n
                        ------------------
                          ~PRODUCT MENU~
                            ---------
                        0️⃣ Return to welcome screen
                        1️⃣ View Food Menu 
                        2️⃣ Add to Food Menu
                        3️⃣ Replace Food Menu items 
                        4️⃣ Delete Food Menu items 
    """)
        # user input for product menu
        usr_product=int_input_limit("please enter 0️⃣, 1️⃣, 2️⃣, 3️⃣ or 4️⃣ : ",4)


        #view food menu csv
        if usr_product==1:
            continue_welcome=False
            print_sql("food_menu")
            close_connection()


        #adding new item to food menu sql db
        elif usr_product==2:
            continue_welcome=False

            new_id=input_check("\nenter the new item id: ","int")
            new_product=input_check("enter the new item name: ","str")
            new_price=input_check("enter its price as a float: ","float")
            
            #appending to sql table
            food_add_sql(new_id,new_product,new_price)
            close_connection()

            print(f"\033[32m***{new_product} has been added successfully***\033[0m")
          

        #UPDATE item
        elif usr_product==3:
            continue_welcome=False
          
            print()
            #showing food menu items and their ids via sql
            print_sql("food_menu")
            item_id=input_check("\nplease enter the id of the item you would like to update: ","int")

            updated_name=input_check("\nenter the updated name (or leave blank to not update): ","str")
            if updated_name != '':update_food_sql("name",updated_name,item_id)

            updated_price=input_check("enter the updated price as a float (or enter 0 to not update): ","float")
            if updated_price != 0:update_food_sql("price",updated_price,item_id)

            updated_id=input_check("enter the updated id (or enter 0 to not update): ","int")
            if updated_id != 0:update_food_sql("product_id",updated_id,item_id)

            close_connection()
            print(f"\033[32m***record with id {item_id} has been successfully updated***\033[0m")


        #delete food menu record from sql
        elif usr_product==4:
            continue_welcome=False
          
            print_sql("food_menu")
            item_del_id=input_check("\nplease enter the id of the item you would like to delete: ","int")

            delete_sql("food_menu","product_id",item_del_id)
            close_connection()

            print(f"\033[32m***record of item with id {item_del_id} has been successfully deleted***\033[0m")

          
    #courier menu
    if usr_welcome==2:
        print("""\n\n
                        ------------------
                          ~COURIER MENU~
                            ---------
                        0️⃣ Return to welcome screen
                        1️⃣ View Couriers 
                        2️⃣ Add to Couriers
                        3️⃣ Replace Courier
                        4️⃣ Delete Courier
    """)
        # user input for courier menu
        usr_courier=int_input_limit("please enter 0️⃣, 1️⃣, 2️⃣, 3️⃣ or 4️⃣ : ",4)


        #view courier menu
        if usr_courier==1:
            continue_welcome=False
            print_sql("couriers")
            close_connection()


        #adding new courier
        elif usr_courier==2:
            continue_welcome=False

            new_id=input_check("\nenter the new courier's id: ","int")
            new_name=input_check("enter the new courier's name: ","str")
            new_number=input_check("enter their number: ","int")

            #appending to sql table
            courier_add_sql(new_id,new_name,new_number)
            close_connection()

            print(f"\033[32m***{new_name} has been added successfully***\033[0m")
          

        #UPDATING courier
        elif usr_courier==3:
            continue_welcome=False

            print()
            print_sql("couriers")
            updating_id=input_check("\nplease enter the id of the courier you would like to update: ","int")

            updated_name=input_check("\nplease enter the updated name (or leave blank to not update): ","str")
            if updated_name != '':update_courier_sql("name",updated_name,updating_id)

            updated_num=input_check("please enter the courier's updated number (or enter 0 to not update): ","int")
            if updated_num != 0:update_courier_sql("phone_number",updated_num,updating_id)

            updated_id=input_check("enter the updated id (or enter 0 to not update): ","int")
            if updated_id != 0:update_courier_sql("courier_id",updated_id,updating_id)
                
            close_connection()
            print(f"\033[32m***record with id {updating_id} has been successfully updated***\033[0m")


        #delete courier from csv
        elif usr_courier==4:
            continue_welcome=False

            print_sql("couriers")
            courier_del_id=input_check("\nplease enter the id of the courier you would like to delete: ","int")

            delete_sql("couriers","courier_id",courier_del_id)
            close_connection()
                
            print(f"\033[32m***record of courier with id {courier_del_id} has been successfully deleted***\033[0m")


    #orders menu
    if usr_welcome==3:
        print("""\n\n
                ------------------
                    ~ORDER MENU~
                    ---------
                0️⃣ Return to welcome screen
                1️⃣ View Orders 
                2️⃣ Add an Order
                3️⃣ Update Order details 
                4️⃣ Delete an Order
    """)
        # user input for order menu
        usr_order=int_input_limit("please enter 0️⃣, 1️⃣, 2️⃣, 3️⃣ or 4️⃣ : ",4)


        #view orders
        if usr_order==1:
            continue_welcome=False
            print_sql("orders")
            close_connection()


        #add an order
        if usr_order==2:
            continue_welcome=False

         #new order info user input
            order_id=input_check("\nnew order id: ","int")
            order_name=input_check("customer name for new order: ","str")
            order_address=input("customer address for new order: ")
            order_phone=input_check("customer phone number for new order: ","int")
            order_status=input_check("new order status: ","str")

            #printing courier sql table and getting uder to choose courier id
            print()
            print_sql("couriers")           
            order_courier=input_check("enter the id of your chosen courier for the new order: ", "int")

            #printing food menu
            print()
            print_sql("food_menu")                
            order_item=input_check("enter the id of the item to add to the new order: ", "int")

            order_add_sql(order_id, order_name,order_phone,order_address,order_courier,order_status,order_item)
            close_connection()

            print(f"\033[32m***{order_name}'s order has been successfully registered***\033[0m")


        #update order details
        if usr_order==3:
            continue_welcome=False

            print()
            print_sql("orders")
            order_id=input_check("\nplease enter the order id of the order you would like to update: ","int")

            product_id=input_check("please enter the product id of the order you would like to update: ","int")

            updated_name=input_check("\nplease enter the customer's updated name (or leave blank to not update): ","str")
            if updated_name != '':update_order_sql("name",updated_name,order_id,product_id)

            updated_num=input_check("please enter the customer's updated number (or enter 0 to not update): ","int")
            if updated_num != 0:update_order_sql("phone_number",updated_num,order_id,product_id)

            updated_address=input_check("please enter the updated address (or leave blank to not update): ","str")
            if updated_address != '':update_order_sql("address",updated_address,order_id,product_id)

            #printing courier menu which shows courier ids before asking for updated courier id
            print()
            print_sql("couriers")
            updated_courier_id=input_check("enter the updated courier id (or enter 0 to not update): ","int")
            if updated_courier_id != 0:update_order_sql("courier_id",updated_courier_id,order_id,product_id)

            updated_order_status=input_check("please enter the updated order status (or leave blank to not update): ","str")
            if updated_order_status != '':update_order_sql("order_status",updated_order_status,order_id,product_id)

            #printing food menu which shows product ids before asking for updated product id
            print()
            print_sql("food_menu")
            updated_product_id=input_check("enter the updated product id (or enter 0 to not update): ","int")
            if updated_product_id != 0:update_order_sql("product_id",updated_product_id,order_id,product_id)

            updated_id=input_check("enter the updated id (or enter 0 to not update): ","int")
            if updated_id != 0:update_order_sql("order_id",updated_id,order_id,product_id)

            close_connection()

            print(f"\033[32m***order record has been successfully updated***\033[0m")


        #delete order
        if usr_order==4:
            continue_welcome=False
          
            print_sql("orders")
            order_del_id=input_check("\nplease enter the order id of the order you would like to delete: ","int")
            product_del_id=input_check("please enter the product id of the order you would like to delete: ","int")

            orders_delete_sql(order_del_id,product_del_id)
            close_connection()
                
            print(f"\033[32m***order record has been successfully deleted***\033[0m")
