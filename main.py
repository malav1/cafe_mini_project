# initialisation- food menu
food_menu=["cake","sandwich","coffee","salad"]
orders=[{"order_name": "John",
"order_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"order_phone": "0789887334",
"order_status": "preparing"}]

# user input for welcome menu- while loop to come back to welcome menu.
continue_welcome=True
while continue_welcome:

    welcome_menu=""""\n\n
                🧂LULU'S CAFE - ADMIN ACCESS🧂 
                    ------------------
                      0️⃣ Exit 
                      1️⃣ Food Menu 
                      2️⃣ Orders Menu

"""
    print(welcome_menu)

    usr_welcome=int(input("please enter 0️⃣, 1️⃣ or 2️⃣ : "))

    #exit
    if usr_welcome==0: break

    #product menu
    if usr_welcome==1:
        product_menu="""\n\n
                        ------------------
                          ~PRODUCT MENU~
                            ---------
                        0️⃣ Return to welcome screen
                        1️⃣ View Food Menu 
                        2️⃣ Add to Food Menu
                        3️⃣ Replace Food Menu items 
                        4️⃣ Delete Food Menu items 

    """
        print(product_menu)

        # user input for product menu
        usr_product=int(input("please enter 0️⃣, 1️⃣, 2️⃣, 3️⃣ or 4️⃣ : "))

        #view food menu
        if usr_product==1:
            continue_welcome=False
            print(f"Items on the Food Menu: {food_menu}")

        #adding new item to food menu
        elif usr_product==2:
            continue_welcome=False
            usr_new_product=input("\nenter the new item you would like to add to the menu: ")
            food_menu.append(usr_new_product)
            print(f"\033[32m***{usr_new_product} has been added successfully***\033[0m")

        #replacing item
        elif usr_product==3:
            continue_welcome=False
            print()
            for i,e in enumerate(food_menu):
                print(f"item:{e}  index:{i}")
            item_index_repl=int(input("\nplease enter the index of the item you would like to replace: "))
            new_item_name=input("please enter the name of the new item: ")
            food_menu.pop(item_index_repl)
            food_menu.insert(item_index_repl,new_item_name)
            print(f"\033[32m***{new_item_name} has been added successfully***\033[0m")

        elif usr_product==4:
            continue_welcome=False
            print(f"\nthese are the current items on the menu: {food_menu}")
            item_del_index=int(input("please enter the index of the item you wish to delete: "))
            food_menu.pop(item_del_index)
            print(f"\033[32m***item at index {item_del_index} has been successfully deleted***\033[0m")


    #orders menu
    if usr_welcome==2:
        order_menu="""\n\n
                ------------------
                    ~ORDER MENU~
                    ---------
                0️⃣ Return to welcome screen
                1️⃣ View Orders 
                2️⃣ Add an Order
                3️⃣ Update Order details 
                4️⃣ Delete an Order

    """
        print(order_menu)

        # user input for order menu
        usr_order=int(input("please enter 0️⃣, 1️⃣, 2️⃣, 3️⃣, 4️⃣ or 5️⃣ : "))

        #view orders
        if usr_order==1:
            continue_welcome=False
            print(f"Orders: {orders}")

        #add an order
        if usr_order==2:
            continue_welcome=False
            order_name=input("please enter customer name for this new order: ")
            order_address=input("please enter customer address for this new order: ")
            order_phone=input("please enter customer phone number for this new order: ")
            orders.append({"order_name":order_name,"order_address":order_address,"order_phone":order_phone,"order_status":"preparing"})
            print(f"\033[32m***{order_name}'s order has been successfully registered***\033[0m")

        #update order details
        if usr_order==3:
            continue_welcome=False
            for i,e in enumerate(orders):
                print(f"\n\033[4mORDER\033[0m:{e} \033[4mINDEX\033[0m:{i}")
            new_index=int(input("\nplease enter the index of the new you wish to update: "))

            new_name=input("please enter the updated name (or leave blank to not update): ")
            if new_name != '': orders[new_index]["order_name"]= new_name

            new_address=input("please enter the updated address (or leave blank to not update): ")
            if new_address != '': orders[new_index]["order_address"]= new_address

            new_phone=input("please enter the updated phone number (or leave blank to not update): ")
            if new_phone != '': orders[new_index]["order_phone"]= new_phone

            new_status=input("please enter the updated status (or leave blank to not update): ")
            if new_status != '': orders[new_index]["order_status"]= new_status

            print(f"\033[32m***order at index {new_index} has been successfully updated***\033[0m")

        #delete order
        if usr_order==4:
            continue_welcome=False
            for i,e in enumerate(orders):
                print(f"\n\033[4mORDER\033[0m:{e} \033[4mINDEX\033[0m:{i}")
            new_index=int(input("\nplease enter the index of the order you wish to delete: "))
            orders.pop(new_index)
            print(f"\033[32m***order at index {new_index} has been successfully deleted***\033[0m")


