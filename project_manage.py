# import database module
import database
# define a funcion called initializing
import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

my_db = database.DB()
def initializing():

# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program
    person_table = database.Table('person', database.open_csv("person", 'persons'))
    info_table = database.Table('login', database.open_csv("info", 'login'))
    advisor = database.Table('advisor', database.open_csv('advisor', 'Advisor_Pending'))
    member = database.Table('member', database.open_csv('member', 'Member_Pending'))
    project = database.Table('project', database.open_csv('project', 'Project_Table'))

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database
    my_db.insert(person_table)
    my_db.insert(info_table)
    my_db.insert(project)
    my_db.insert(advisor)
    my_db.insert(member)

# define a funcion called login

def login():
    # login_info = my_db.search('login')
    # username = str(input("Please input your username: "))
    # password = str(input("Please input your password: "))
    # for i in login_info:
    #     print(i)
    #     if i['username'] == username and i['password'] == password:
    #         return [i['ID'], i['role']]
    #     return None
    pass


# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
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
