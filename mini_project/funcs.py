#looping through csv, stripping "\n" and adding to list
def read_file_list(path):
    with open(path,"r") as file:
        output_list=[x.strip() for x in file.readlines()]
        return output_list

#appending to csv file
def append_to_file(path,content):
    with open(path,"a+") as file:
        file.write(content)

#replacing old csv with contents of newly edited list. "\n" is not added if its last list element to avoid '' being counted as a list element if csv needs to be turned into list again for, eg food menu viewing.
def write_to_file(path,usr_list):
    with open(path,"w+") as file:
        for e in usr_list:
            file.write(f"{e}\n")

#showing list items and their index positions via loop
def index_item(usr_list):
    for i,e in enumerate(usr_list):
        print(f"INDEX {i}: {e}")   

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

def test_read_file_list():
    expected=['{"first_name":"john","last_name":"smith"}']
    actual=read_file_list("mock_file.csv")
    assert expected==actual
# test_read_file_list()

def test_append_to_file():
    append_to_file("mock_file.csv",'{"first_name":"tim","last_name":"roe"}')
    expected=read_file_list("mock_file.csv")[-1]
    assert expected=='{"first_name":"tim","last_name":"roe"}'
# test_append_to_file()

def test_write_to_file():
    write_to_file("mock_file.csv",['{"first_name":"john","last_name":"smith"}'])
    expected=read_file_list("mock_file.csv")
    assert expected==['{"first_name":"john","last_name":"smith"}']
# test_write_to_file()

def test_index_item():
    actual=index_item(['{"first_name":"john","last_name":"smith"}'])
    expected=None
    assert actual==expected
# test_index_item()

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