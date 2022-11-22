from csv import writer
import pymysql

#MYSQL FUNCS
    # Load environment variables from .env file
host = "localhost"
user = "root"
password = "password"
database = "test"

    # Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# connection object created
connection_var = connection.cursor()

#change to correct db
connection_var.execute('USE mini_project')

#ADD
def food_add_sql(add_id,add_name,add_price):
    sql = "INSERT INTO food_menu (product_id, name, price) VALUES (%s, %s, %s)"
    val = (add_id,add_name,add_price)
    connection_var.execute(sql, val)
    connection.commit()

def courier_add_sql(add_id,add_name,add_phone):
    sql="INSERT INTO couriers (courier_id, name, phone_number) VALUES (%s, %s, %s)"
    val = (add_id,add_name,add_phone)
    connection_var.execute(sql,val)
    connection.commit()

def order_add_sql(add_id,add_name,add_phone,add_address,add_courier_id,add_order_status,add_product_id):
    sql="INSERT INTO orders (order_id, name, phone_number, address, courier_id, order_status, product_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (add_id,add_name,add_phone,add_address,add_courier_id,add_order_status,add_product_id)
    connection_var.execute(sql,val)
    connection.commit()

#UPDATE
def update_food_sql(column_name,new_info,prod_id):
    if column_name!="name":
        sql="UPDATE food_menu SET {}={} WHERE product_id={}".format(column_name,new_info,prod_id)
    else:
        sql="UPDATE food_menu SET {}='{}' WHERE product_id={}".format(column_name,new_info,prod_id)
    connection_var.execute(sql)
    connection.commit()

def update_courier_sql(column_name,new_info,prod_id):
    if column_name=="courier_id":
        sql="UPDATE couriers SET {}={} WHERE courier_id={}".format(column_name,new_info,prod_id)
    else:
        sql="UPDATE couriers SET {}='{}' WHERE courier_id={}".format(column_name,new_info,prod_id)
    connection_var.execute(sql)
    connection.commit()

def update_order_sql(column_name,new_info,order_id,prod_id):
    if column_name in ["name","phone_number","address","order_status"]:
        sql="UPDATE orders SET {}='{}' WHERE order_id={} AND product_id={}".format(column_name,new_info,order_id,prod_id)
    else:
        sql="UPDATE orders SET {}={} WHERE order_id={} AND product_id={}".format(column_name,new_info,order_id, prod_id)
    connection_var.execute(sql)
    connection.commit()

#DELETE
def delete_sql(table_name,id_column_name,del_id):
    connection_var.execute("DELETE FROM {} WHERE {} = {}".format(table_name,id_column_name,del_id))
    connection.commit()

def orders_delete_sql(ord_id,prod_id):
    connection_var.execute("DELETE FROM orders WHERE order_id = {} AND product_id={}".format(ord_id,prod_id))
    connection.commit()

#SINGLE FUNCS
def print_sql(table):
    connection_var.execute(f'SELECT * FROM {table}')
    #gets headers
    col_names = [i[0] for i in connection_var.description]
    print(col_names)
    # fetchall gets all the data from the table we defined in execute
    rows = connection_var.fetchall()
    for row in rows:
        print(row)

def close_connection():
    connection_var.close()
    connection.close()

 #checking if user id input exists in sql table id
def valid_id(prompt, table):
    connection_var.execute(f'SELECT * FROM {table}')
    rows = connection_var.fetchall()
    valid_ids=[row[0] for row in rows]
    cont = True
    while cont:
        try:
            int_value = int(input(prompt))
            if int_value not in valid_ids:
                print(f"\033[31mid {int_value} does not exist\033[0m")
            else:
                cont=False
        except ValueError:
            print("\033[31mYou can ONLY use numbers!\033[0m")
    return int_value

    #int input error function where there is a max num user can input
def int_input_limit(prompt,num_limit):
    not_valid = True
    while not_valid:
        try:
            int_value = int(input(prompt))
            if int_value<0 or int_value>num_limit:
                print(f"\033[31moption {int_value} does not exist\033[0m")
            else:
                not_valid=False
        except ValueError:
            print("\033[31mYou can ONLY use numbers!\033[0m")
    return int_value


    #int input error func- type of input simply needs to be int regardless of len
def input_check(prompt,data_type):
    not_valid = True

    while not_valid:
        if data_type=="int":
            try:
                output = int(input(prompt))
                not_valid = False
            except ValueError:
                print("\033[31mYou can ONLY use numbers!\033[0m")
        
        if data_type=="float":
            try:
                output = float(input(prompt))
                not_valid = False
            except ValueError:
                print("\033[31mYou can ONLY use decimal numbers!\033[0m")

        elif data_type=="str":
            output = input(prompt)
            if output.isdigit()==True:
                print("\033[31mYou can ONLY use words!\033[0m")
            else:
                not_valid = False

    return output



#############TESTS#################

def test_int_input_limit():
    actual=int_input_limit("enter a number: ", 4)
    expected=3
    assert actual==expected
# test_int_input_limit()

def test_input_check():
    actual=input_check("enter a letter: ","str")
    expected="hello"
    assert expected==actual
# test_input_check()
