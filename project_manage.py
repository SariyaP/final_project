# import database module
import database
# define a funcion called initializing
import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

login = []
with open(os.path.join(__location__, 'login.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        login.append(dict(r))
print(login)

my_db = database.DB()
def initializing():

# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program
    persons_table = database.Table('persons', database.persons)
    login_table = database.Table('login', login)
    project_table = database.Table('project', [])
    advisor_request_table = database.Table('advisor', [])
    member_request_table = database.Table('member', [])
    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database
    my_db.insert(persons_table)
    my_db.insert(login_table)
    my_db.insert(project_table)
    my_db.insert(advisor_request_table)
    my_db.insert(member_request_table)

# define a funcion called login

def login():
    # login_info = my_db.search('login')
    # print(login_info)
    # username = str(input("Please input your username: "))
    # password = str(input("Please input your password: "))
    # for i in login_info:
    #     if i['username'] == username and i['password'] == password:
    #
    #         return None


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
