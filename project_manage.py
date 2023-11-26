import database
import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

my_db = database.DB()


def initializing():
    person_table = database.Table('person', database.open_csv("person", 'persons'))
    info_table = database.Table('login', database.open_csv("info", 'login'))
    advisor = database.Table('advisor', database.open_csv('advisor', 'Advisor_Pending'))
    member = database.Table('member', database.open_csv('member', 'Member_Pending'))
    project = database.Table('project', database.open_csv('project', 'Project_Table'))
    my_db.insert(person_table)
    my_db.insert(info_table)
    my_db.insert(project)
    my_db.insert(advisor)
    my_db.insert(member)

def login():
    login_info = my_db.search('login')
    username = str(input("Please input your username: "))
    password = str(input("Please input your password: "))
    for i in login_info.table:
        if i['username'] == username and i['password'] == password:
            return [i['ID'], i['role']]
        return None


# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit

def exit():
    pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e.,
   # writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


def table_edit(table_name):
    while True:
        editing = my_db.search(table_name)
        print("What do you want to do with it?")
        print("1. Insert information", "2. Update information", "3. Delete information", "0. Exit", sep='\n')
        choice = input("Input your choice: ")
        if choice == "1":
            print(f"Information format: {list(editing.table[1].keys())}")
            insert_information = list(input("Enter information: "))
            editing.insert(insert_information)
        elif choice == "2":
            key_value = input("What key do you want to edit: ")
            item_value = input("Change it to: ")
            editing.update(key_value, item_value)
        elif choice == "3":
            delete_id = input("Enter Member ID or Project ID to delete: ")
            editing.delete(delete_id)
        elif choice == "0":
            break


def table_access():
    while True:
        print("Which table do you want to access?")
        print("1. Login info",
              "2. Users info",
              "3. Project",
              "4. Advisor pending",
              "5. Member Pending",
              "0. Exit", sep='\n')
        choices = str(input('Input your choice: '))
        if choices == "1":
            table_edit('login')
        elif choices == "2":
            table_edit('person')
        elif choices == "3":
            table_edit('project')
        elif choices == "4":
            table_edit('advisor')
        elif choices == "5":
            table_edit('member')
        elif choices == "0":
            break


def admin():
    while True:
        print("Welcome admin")
        print("1. Manage the table", "0. Exit", sep='\n')
        choice = str(input("Input your choice: "))
        if choice == '1':
            table_access()
        elif choice == "0":
            break

def student():
    pass
# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    admin()
    # see and do admin related activities
elif val[1] == 'student':
    student()
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
