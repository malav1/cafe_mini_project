import ast
from funcs import read_file_list, append_to_file, write_to_file, index_item, int_input_limit, input_check

food_menu_list=read_file_list("food_menu.csv")
couriers_list=read_file_list("couriers.csv")
orders_list=read_file_list("orders.csv")

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
            print(food_menu_list)


        #adding new item to food menu csv
        elif usr_product==2:
            continue_welcome=False

            usr_new_product=input_check("\nenter the new item you would like to add to the menu: ","str")
            usr_new_product_price=input_check("\nenter the price you would like to add with it as a float: ","float")
            
            #appending to csv file
            append_to_file("food_menu.csv",f'{{"name": "{usr_new_product}", "price": {usr_new_product_price}}}\n')

            print(f"\033[32m***{usr_new_product} has been added successfully***\033[0m")
          

        #replacing item
        elif usr_product==3:
            continue_welcome=False
          
            print()
            #showing list items and their index positions via loop
            index_item(food_menu_list)
            item_index_repl=int_input_limit("\nplease enter the index of the item you would like to replace: ",(len(food_menu_list)-1))

            new_item_name=input_check("please enter the name of the new item: ","str")
            new_item_price=input_check("please enter the price of the new item: ","float")

            food_menu_list.pop(item_index_repl)
            food_menu_list.insert(item_index_repl,f'{{"name": "{new_item_name}", "price": {new_item_price}}}')
            write_to_file("food_menu.csv",food_menu_list)
                
            print(f"\033[32m***{new_item_name} has been added successfully***\033[0m")


        #delete food item from csv
        elif usr_product==4:
            continue_welcome=False
          
            index_item(food_menu_list)
            item_del_index=int_input_limit("\nplease enter the index of the item you would like to delete: ",(len(food_menu_list)-1))

            food_menu_list.pop(item_del_index)
            write_to_file("food_menu.csv",food_menu_list)
                
            print(f"\033[32m***item at index {item_del_index} has been successfully deleted***\033[0m")

          
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
            print(couriers_list)


        #adding new courier
        elif usr_courier==2:
            continue_welcome=False

            usr_new_courier=input_check("\nenter the new courier's name: ","str")
            usr_new_courier_num=input_check("\nenter their number: ","int")

            append_to_file("couriers.csv",f'{{"name": "{usr_new_courier}", "phone": "{usr_new_courier_num}"}}\n')

            print(f"\033[32m***{usr_new_courier} has been added successfully***\033[0m")
          

        #replacing courier
        elif usr_courier==3:
            continue_welcome=False

            print()
            index_item(couriers_list)
            courier_index_repl=int_input_limit("\nplease enter the index of the courier you would like to replace: ",(len(couriers_list)-1))

            new_courier_name=input_check("please enter the name of the new courier: ","str")
            new_courier_num=input_check("\nenter the courier's number: ")

            couriers_list.pop(courier_index_repl)
            couriers_list.insert(courier_index_repl,f'{{"name": "{new_courier_name}", "number": {new_courier_num}}}')
            write_to_file("couriers.csv",couriers_list)
                
            print(f"\033[32m***{new_courier_name} has been added successfully***\033[0m")


        #delete courier from csv
        elif usr_courier==4:
            continue_welcome=False

            index_item(couriers_list)
            courier_del_index=int_input_limit("\nplease enter the index of the courier you would like to delete: ",(len(couriers_list)-1))

            couriers_list.pop(courier_del_index)
            write_to_file("couriers.csv",couriers_list)
                
            print(f"\033[32m***item at index {courier_del_index} has been successfully deleted***\033[0m")


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
            print(orders_list)


        #add an order
        if usr_order==2:
            continue_welcome=False

         #new order info user input
            order_name=input_check("new order name: ","str")
            order_address=input("new order address: ")
            order_phone=input_check("new order phone number: ","int")

            #printing courier and their indicies
            print()
            index_item(couriers_list)           
            order_courier=int_input_limit("enter the index of your chosen courier for the new order: ", (len(couriers_list)-1))

            #printing food menu items and their indicies
            print()
            index_item(food_menu_list)                  
            order_items=int_input_limit("enter the index of your chosen item(s) for the new order: ", (len(food_menu_list)-1))

            append_to_file("orders.csv", f'{{"order_name": "{order_name}", "order_address": "{order_address}", "order_phone": "{order_phone}", "courier": {int(order_courier)}, "order_status": "preparing", "items": "{order_items}"}}\n')

            print(f"\033[32m***{order_name}'s order has been successfully registered***\033[0m")


        #update order details
        if usr_order==3:
            continue_welcome=False

            orders_list_dic=[ast.literal_eval(e) for e in orders_list]                

            index_item(orders_list_dic)
            new_index=int_input_limit("\nplease enter the index of the order you wish to update: ", (len(orders_list_dic)-1))

            new_name=input_check("please enter the updated name (or leave blank to not update): ","str")
            if new_name != '': orders_list_dic[new_index]["order_name"]= new_name
            new_address=input("please enter the updated address (or leave blank to not update): ")
            if new_address != '': orders_list_dic[new_index]["order_address"]= new_address
            new_phone=input_check("please enter the updated phone number (or leave blank to not update): ","int")
            if new_phone != '': orders_list_dic[new_index]["order_phone"]= str(new_phone)
            new_courier=input_check("please enter the updated courier (or leave blank to not update): ","int")
            if new_courier != '': orders_list_dic[new_index]["courier"]= new_courier
            new_status=input_check("please enter the updated status (or leave blank to not update): ","str")
            if new_status != '': orders_list_dic[new_index]["order_status"]= new_status
            new_items=input("please enter the updated items (or leave blank to not update): ")
            if new_items != '': orders_list_dic[new_index]["items"]= new_items           

            write_to_file("orders.csv",orders_list_dic)

            print(f"\033[32m***order at index {new_index} has been successfully updated***\033[0m")


        #delete order
        if usr_order==4:
            continue_welcome=False
          
            index_item(orders_list)
            new_index=int_input_limit("\nplease enter the index of the order you wish to delete: ", (len(orders_list)-1))

            orders_list.pop(new_index)
            write_to_file("orders.csv",orders_list)
                
            print(f"\033[32m***order at index {new_index} has been successfully deleted***\033[0m")
