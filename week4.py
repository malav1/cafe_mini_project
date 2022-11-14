import ast

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

    usr_welcome=int(input("please enter 0️⃣, 1️⃣, 2️⃣ or 3️⃣ : "))

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
        usr_product=int(input("please enter 0️⃣, 1️⃣, 2️⃣, 3️⃣ or 4️⃣ : "))

        #view food menu csv
        if usr_product==1:
            continue_welcome=False
            #looping through csv, stripping "\n" and adding to list
            with open("mini project/food_menu.csv","r") as file:
                food_menu_list=[x.strip() for x in file.readlines()]
                print(food_menu_list)

        #adding new item to food menu csv
        elif usr_product==2:
            continue_welcome=False
            #appending to csv file
            usr_new_product=input("\nenter the new item you would like to add to the menu: ")
            usr_new_product_price=input("\nenter the price you would like to add with it as a float: ")
            
            with open("mini project/food_menu.csv","a+") as file:
                file.write(f'{{"name": "{usr_new_product}", "price": {float(usr_new_product_price)}}}\n')

            print(f"\033[32m***{usr_new_product} has been added successfully***\033[0m")
          

        #replacing item
        elif usr_product==3:
            continue_welcome=False
            print()
          
            with open("mini project/food_menu.csv","r") as file:
                food_menu_list=[x.strip() for x in file.readlines()]
            #showing list items and their index positions via loop
            for i,e in enumerate(food_menu_list):
                print(f"item:{e}  index:{i}")
              
            item_index_repl=int(input("\nplease enter the index of the item you would like to replace: "))
            new_item_name=input("please enter the name of the new item: ")
            new_item_price=input("please enter the price of the new item: ")
            food_menu_list.pop(item_index_repl)
            food_menu_list.insert(item_index_repl,f'{{"name": "{new_item_name}", "price": {float(new_item_price)}}}')

            #replacing old csv with contents of newly edited list. "\n" is not added if its last list element to avoid '' being counted as a list element if csv needs to be turned into list again for, eg food menu viewing.
            with open("mini project/food_menu.csv","w+") as file:
                for e in food_menu_list:
                    file.write(f"{e}\n")
                
            print(f"\033[32m***{new_item_name} has been added successfully***\033[0m")

        #delete food item from csv
        elif usr_product==4:
            continue_welcome=False
          
            with open("mini project/food_menu.csv","r") as file:
                food_menu_list=[x.strip() for x in file.readlines()]
          
            for i,e in enumerate(food_menu_list):
                print(f"item:{e}  index:{i}")

            item_del_index=int(input("\nplease enter the index of the item you would like to delete: "))
            food_menu_list.pop(item_del_index)

            with open("mini project/food_menu.csv","w+") as file:
                for e in food_menu_list:
                    file.write(f"{e}\n")
                
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
        usr_courier=int(input("please enter 0️⃣, 1️⃣, 2️⃣, 3️⃣ or 4️⃣ : "))

        #view courier menu
        if usr_courier==1:
            continue_welcome=False
            with open("mini project/couriers.csv","r") as file:
              couriers_list=[x.strip() for x in file.readlines()]
              print(couriers_list)

        #adding new courier
        elif usr_courier==2:
            continue_welcome=False
            usr_new_courier=input("\nenter the courier you would like to add: ")
            usr_new_courier_num=input("\nenter the courier's number: ")
            with open("mini project/couriers.csv","a+") as file:
              file.write(f'{{"name": "{usr_new_courier}", "phone": "{usr_new_courier_num}"}}\n')

            print(f"\033[32m***{usr_new_courier} has been added successfully***\033[0m")
          

        #replacing item
        elif usr_courier==3:
            continue_welcome=False
            print()
          
            with open("mini project/couriers.csv","r") as file:
              couriers_list=[x.strip() for x in file.readlines()]
            for i,e in enumerate(couriers_list):
                print(f"item:{e}  index:{i}")
              
            courier_index_repl=int(input("\nplease enter the index of the courier you would like to replace: "))
            new_courier_name=input("please enter the name of the new courier: ")
            new_courier_num=input("\nenter the courier's number: ")
            couriers_list.pop(courier_index_repl)
            couriers_list.insert(courier_index_repl,f'{{"name": "{new_courier_name}", "number": {new_courier_num}}}')
          
            with open("mini project/couriers.csv","w+") as file:
              for e in couriers_list:
                  file.write(f"{e}\n")
                
            print(f"\033[32m***{new_courier_name} has been added successfully***\033[0m")

        #delete courier from csv
        elif usr_courier==4:
            continue_welcome=False
          
            with open("mini project/couriers.csv","r") as file:
              couriers_list=[x.strip() for x in file.readlines()]

            for i,e in enumerate(couriers_list):
                print(f"item:{e}  index:{i}")
              
            courier_del_index=int(input("\nplease enter the index of the item you would like to delete: "))
            couriers_list.pop(courier_del_index)

            with open("mini project/couriers.csv","w+") as file:
                for e in couriers_list:
                    file.write(f"{e}\n")
                
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
        usr_order=int(input("please enter 0️⃣, 1️⃣, 2️⃣, 3️⃣, 4️⃣ or 5️⃣ : "))

        #view orders
        if usr_order==1:
            continue_welcome=False
            with open("mini project/orders.csv","r") as file:
                orders_list=[x.strip() for x in file.readlines()]
                print(orders_list)


        #add an order
        if usr_order==2:
            continue_welcome=False


          #new order info user input
            order_name=input("new order name: ")
            order_address=input("new order address: ")
            order_phone=input("new order phone number: ")

            #printing courier and their indicies
            print()
            with open("mini project/couriers.csv","r") as file:
                couriers_list=[x.strip() for x in file.readlines()]

            for i,e in enumerate(couriers_list):
                print(f"INDEX {i} COURIER: {e}")            
            order_courier=input("new order courier index: ")

            #printing food menu items and their indicies
            print()
            with open("mini project/food_menu.csv","r") as file:
                food_menu_list=[x.strip() for x in file.readlines()]

            for i,e in enumerate(food_menu_list):
                print(f"INDEX {i} ITEM: {e}")                   
            order_items=input("new order item indices: ")


            with open("mini project/orders.csv","a+") as file:
                file.write(f'{{"order_name": "{order_name}", "order_address": "{order_address}", "order_phone": "{order_phone}", "courier": {int(order_courier)}, "order_status": "preparing", "items": "{order_items}"}}\n')

            print(f"\033[32m***{order_name}'s order has been successfully registered***\033[0m")

        #update order details
        if usr_order==3:
            continue_welcome=False

            with open("mini project/orders.csv","r") as file:
                orders_list=[x.strip() for x in file.readlines()]
                orders_list_dic=[ast.literal_eval(e) for e in orders_list]                

            for i,e in enumerate(orders_list_dic):
                print(f"INDEX {i} ORDER: {e}")
              

            new_index=int(input("\nplease enter the index of the order you wish to update: "))

            new_name=input("please enter the updated name (or leave blank to not update): ")
            if new_name != '': orders_list_dic[new_index]["order_name"]= new_name

            new_address=input("please enter the updated address (or leave blank to not update): ")
            if new_address != '': orders_list_dic[new_index]["order_address"]= new_address

            new_phone=input("please enter the updated phone number (or leave blank to not update): ")
            if new_phone != '': orders_list_dic[new_index]["order_phone"]= new_phone

            new_courier=input("please enter the updated courier (or leave blank to not update): ")
            if new_courier != '': orders_list_dic[new_index]["courier"]= new_courier

            new_status=input("please enter the updated status (or leave blank to not update): ")
            if new_status != '': orders_list_dic[new_index]["order_status"]= new_status

            new_items=input("please enter the updated items (or leave blank to not update): ")
            if new_items != '': orders_list_dic[new_index]["items"]= new_items           

            with open("mini project/orders.csv","w+") as file:
                for e in orders_list_dic:
                    file.write(f"{e}\n")

            print(f"\033[32m***order at index {new_index} has been successfully updated***\033[0m")

        #delete order
        if usr_order==4:
            continue_welcome=False
       
            with open("mini project/orders.csv","r") as file:
                orders_list=[x.strip() for x in file.readlines()]
          
            for i,e in enumerate(orders_list):
                print(f"INDEX {i} ORDER: {e}")

            new_index=int(input("\nplease enter the index of the order you wish to delete: "))
            orders_list.pop(new_index)

            with open("mini project/orders.csv","w+") as file:
                for e in orders_list:
                    file.write(f"{e}\n")
                
            print(f"\033[32m***order at index {new_index} has been successfully deleted***\033[0m")
