import random

import database
import os
from datetime import datetime

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

my_db = database.DB()


def initializing():
    person_table = database.Table('person', database.open_csv("person", 'persons'))
    info_table = database.Table('login', database.open_csv("info", 'login'))
    advisor = database.Table('advisor', database.open_csv('advisor', 'Advisor_Pending'))
    member = database.Table('member', database.open_csv('member', 'Member_Pending'))
    project = database.Table('project', database.open_csv('project', 'Project_Table'))
    grade = database.Table('grade', database.open_csv('grade', 'Grading'))
    my_db.insert(person_table)
    my_db.insert(info_table)
    my_db.insert(project)
    my_db.insert(advisor)
    my_db.insert(member)
    my_db.insert(grade)


def login():
    while True:
        login_info = my_db.search('login')
        print("Enter your username and password")
        username = str(input("Please input your username: "))
        password = str(input("Please input your password: "))
        for i in login_info.table:
            if i['username'] == username and i['password'] == password:
                return[i['ID'], i['role']]
        print("Wrong username or password!")


def exit():
    database.write('member', 'Member_Pending', my_db)
    database.write('advisor', 'Advisor_Pending', my_db)
    database.write('project', 'Project_Table', my_db)
    database.write('grade', 'Grading', my_db)


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


def find_member():
    while True:
        infos = input("Enter ID or type 0 to exit:")
        if infos == '0':
            break
        else:
            for i in my_db.search('login').table:
                if infos == i['ID']:
                    print(f"{i['Username']}")
                    if i['role'] == 'student':
                        invite_member(i['ID'])
                    elif i['role'] == 'faculty':
                        invite_advisor(i['ID'])


def invite_member(id):
    decision = str(input(f"Invite user {id} to be the member of your project? y/n"))
    if decision == 'y':
        projectid = str(input("Enter your project ID: "))
        my_db.search('member').insert(projectid, id, 'Pending', 'None')
    if decision == 'n':
        pass


def invite_advisor(id):
    decision = str(input(f"Invite user {id} to be the advisor of your project? y/n"))
    if decision == 'y':
        projectid = str(input("Enter your project ID: "))
        my_db.search('advisor').insert(projectid, id, 'Pending', 'None')
    if decision == 'n':
        pass


def create_project():
    project_id = random.randint(10000, 99999)
    project_name = str(input("What do you want to name this project? "))
    leader_id = val[0]
    my_db.search('project').insert({"ProjectID": project_id, 'Title': project_name, 'Lead': leader_id,
                                    'Member1': 'None', 'Member2': 'None', 'Advisor': 'None', 'Status': 'Created',
                                    'Information': 'Empty'})
    print('Project created!')


def edit_project():
    while True:
        editing = input("Enter your project name you want to edit: ")
        if editing == '0':
            break
        elif editing not in my_db.search('project').table:
            print('There is no project!')
        choice = input("What do you want to edit?\n"
                       "1. Insert information\n"
                       "2. Member\n"
                       "3. Advisor\n"
                       "4. Submit\n"
                       "0. Exit\n")
        if choice == '1':
            project = my_db.search('project').filter(lambda x: x['Title'] == editing)
            if project.table[0]['Status'] == 'Submitted':
                print("This project is already submitted.")
                unsub = input("Do you want to unsubmit the project? y/n \n")
                if unsub == 'y':
                    project.update_table('Status', 'Editing')
                else:
                    break
            else:
                if project.table[0]['Information'] == 'Empty':
                    new_information = input("Write your project information\n")
                    project.update_table('Information', new_information)
                    my_db.search('project').filter(lambda x: x['Title'] == editing).update_table('Status', 'Editing')
                else:
                    new_information = input("Write your project information")
                    old_informtaion = project['Information']
                    project.update_table('Information', old_informtaion+' '+new_information)
        elif choice == '2':
            project = my_db.search('project').filter(lambda x: x['Title'] == editing)
            if project.table[0]['Lead'] != val[0]:
                print("You don't have permission!")
                break
            else:
                while True:
                    member = input("Enter ID of the user you want to remove from the project")
                    if member not in project[0]:
                        print('There is no matching ID!')
                        break
                    else:
                        if project.table[0]['Member1'] == member:
                            project.update_table('Member1', 'None')
                        else:
                            project.update_table('Member2', 'None')
        elif choice == '3':
            project = my_db.search('project').filter(lambda x: x['Title'] == editing)
            if project.table[0]['Lead'] != val[0]:
                print("You don't have permission!")
                break
            else:
                advisor = input("Are you sure you want to remove advisor? y/n \n")
                if advisor == 'y':
                    print('Advisor removed')
                    project.update_table('Advisor', 'None')
                else:
                    break
        elif choice == '4':
            project = my_db.search('project').filter(lambda x: x['Title'] == editing)
            sure = input("Submit your project? y/n \n")
            if sure == 'y':
                project.update_table('Status', 'Submitted')
            else:
                break


def delete_project():
    deletepro = input("Enter your project title to delete: ")
    for i in my_db.search('project').filter(lambda x: x['Title'] == deletepro):
        my_db.search('project').table.delete(i['ProjectID'])


def see_project():
    while True:
        user_project = []
        num = 0
        for i in my_db.search('project').table:
            if i['Lead'] == val[0]:
                num += 1
                user_project.append(i)
                print(f"{num}.")
                print(f"Title: {i['Title']}")
                print(f"ProjectID: {i['ProjectID']}")
        break
    if val[1] == 'student':
        while True:
            choice = input("What do you want to do with your project? \n"
                           "1. Edit\n"
                           "2. Create new project\n"
                           "3. Delete project\n"
                           "0. Exit\n")
            if choice == '1':
                edit_project()
            elif choice == '2':
                create_project()
            elif choice == '3':
                delete_project()
            else:
                break


def notification(id):
    while True:
        count = 0
        project_info = my_db.search("project").table
        project_id = []
        if len(project_info) > 0:
            if val[1] == 'student':
                for i in my_db.search('member').table:
                    if i['to_be_member'] == id and i['Response'] == 'Pending':
                        count += 1
                        project_id.append(i['ProjectID'])
                if count > 1:
                    print(f"You have {count} notifications!")
                elif count == 1:
                    print(f"You have {count} notifications!")
                elif count == 0:
                    print(f"You have no notification!")
                    break
            else:
                for i in my_db.search('advisor').table:
                    if i['to_be_advisor'] == id and i['Response'] == 'Pending':
                        count += 1
                        project_id.append(i['ProjectID'])
                if count > 1:
                    print(f"You have {count} notifications!")
                elif count == 1:
                    print(f"You have {count} notifications!")
                elif count == 0:
                    print(f"You have no notification!")
                    break

            check = str(input("Do you want to check the notification? y/n \n"))
            if check == 'y':
                for i in project_info:
                    if i['ProjectID'] in project_id :
                        print(f"Title: {i['Title']} Owner: {i['Lead']} \n"
                              f"Member: {i['Member1']},{i['Member2']} \n"
                              f"Advisor: {i['Advisor']} \n"
                              f"Status: {i['Status']}")
                        decision = str(input("Accept invite? y/n \n"))
                        if val[1] == 'student':
                            update_project = my_db.search('member').filter(
                                lambda x: x['ProjectID'] in project_id and x['to_be_member'] == val[0]).update_table(
                                'Response', 'Seen')
                            if decision == 'y':
                                change = my_db.search('member').filter(
                                    lambda x:x['ProjectID'] == i['ProjectID']).update_table('Response', 'Accepted')
                                print(f"You can now view {i['ProjectID']} as member")
                                if my_db.search("project").table[0]['Member1'] == 'None':
                                    my_db.search("project").filter(
                                        lambda x: x['ProjectID'] == i['ProjectID']).update_table(
                                        'Member1', f'{id}')
                                    my_db.search('member').filter(
                                        lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_member'] == val[
                                            0]).update_table('Response', 'Accepted')
                                    my_db.search('member').filter(
                                        lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_member'] == val[
                                            0]).update_table('Response_date', datetime.today().strftime('%Y-%m-%d'))
                                else:
                                    my_db.search("project").filter(
                                        lambda x: x['ProjectID'] == i['ProjectID']).update_table('Member2', f'{id}')
                                    my_db.search('member').filter(
                                        lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_member'] == val[
                                            0]).update_table('Response', 'Accepted')
                                    my_db.search('member').filter(
                                        lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_member'] == val[
                                            0]).update_table('Response_date', datetime.today().strftime('%Y-%m-%d'))
                            else:
                                my_db.search('member').filter(
                                    lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_member'] == val[
                                        0]).update_table('Response', 'Denied')
                                my_db.search('member').filter(
                                    lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_member'] == val[
                                        0]).update_table('Response_date', datetime.today().strftime('%Y-%m-%d'))
                        else:
                            update_project = my_db.search('member').filter(
                                lambda x: x['ProjectID'] in project_id and x['to_be_member'] == val[0]).update_table(
                                'Response', 'Seen')
                            if decision == 'y':
                                change = my_db.search('advisor').filter(
                                    lambda x: x['ProjectID'] == i['ProjectID']).update_table('Response', 'Accepted')
                                print(f"You can now view {i['ProjectID']} as advisor")
                                my_db.search("project").filter(
                                    lambda x: x['ProjectID'] == i['ProjectID']).update_table('Advisor', f'{id}')
                                my_db.search('member').filter(
                                    lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_advisor'] == val[
                                        0]).update_table('Response', 'Accepted')
                                my_db.search('member').filter(
                                    lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_advisor'] == val[
                                        0]).update_table('Response_date', datetime.today().strftime('%Y-%m-%d'))
                            else:
                                my_db.search('advisor').filter(
                                    lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_advisor'] == val[
                                        0]).update_table('Response', 'Denied')
                                my_db.search('advisor').filter(
                                    lambda x: x['ProjectID'] == i['ProjectID'] and x['to_be_advisor'] == val[
                                        0]).update_table('Response_date', datetime.today().strftime('%Y-%m-%d'))
            else:
                break
        else:
            print("There is no notification!")


def evaluation():
    advised = sub_project()
    while True:
        evaluate = input('Enter project ID to evaluate(or 0 to exit):')
        if evaluate in advised:
            grader1 = input('Enter ID of other faculty:')
            grader2 = input("Enter ID of other faculty:")
            my_db.search('grade').insert({
                'ProjectID': evaluate, 'Grader1': grader1, "Grader2": grader2, "Grade1": 'None', 'Grade2': "None",
                'Final_grade': 'None'})
            my_db.search('project').filter(lambda x:x['ProjectID'] == [evaluate]).update('Status', 'Grading')
        if evaluate == '0':
            break
        else:
            print('There is no such project')

def grade():
    if len(my_db.search('grade').table) > 0:
        for i in my_db.search('grade').table:
            if val[0] in i['Grade1']:
                projectid = i['ProjectID']
                graded = my_db.search('project').filter(lambda x: x['ProjectID'] == projectid)
                print(f"Title: {graded['title']}\n"
                      f"Information: {graded['Information']}")
                grade_ = input("What will you rate this project?")
                my_db.search('grade').filter(lambda x: x['ProjectID'] == projectid).update_table('Grade1',grade_)
                print('Thank you for rating!')
            if val[0] in i['Grade2']:
                projectid = i['ProjectID']
                graded = my_db.search('project').filter(lambda x: x['ProjectID'] == projectid)
                print(f"Title: {graded['title']}\n"
                      f"Information: {graded['Information']}")
                grade_ = input("What will you rate this project?")
                my_db.search('grade').filter(lambda x: x['ProjectID'] == projectid).update_table('Grade2', grade_)
                my_db.search('grade').filter(
                    lambda x: x['ProjectID'] == projectid).update_table('Final_grade',
                f"{int(grade_)+int(my_db.search('grade').filter(lambda x: x['ProjectID'] == projectid)['Grade1'])/2:.2f}")
                my_db.search('project').filter(lambda x: x['ProjectID'] == projectid).update_table('Status', 'Graded')
                print('Thank you for rating!')
    else:
        print("There is nothing to grade")


def sub_project():
    submitted = my_db.search('project').filter(lambda x: x['Status'] == 'Submitted' and x['Advisor'] == val[0])
    if len(submitted) > 0:
        submitted_id = []
        for i in submitted.table:
            print(f"Title: {i['Title']} Owner: {i['Lead']} \n"
                  f"Member: {i['Member1']},{i['Member2']} \n"
                  f"Advisor: {i['Advisor']} \n"
                  f"Status: {i['Status']}\n"
                  f"Information: {i['information']}")
            submitted_id.append(i['ProjectID'])
        return submitted_id
    else:
        print('There is no submitted project')


def student():
    while True:
        info = my_db.search("login").table
        id_info = [i for i in info if val[0] in i['ID']]
        print(f"Hi, {id_info[0]['username']}")
        notification(val[0])
        print(f"What do you want to do?\n"
              f"1. See project",
              "2. Invite member",
              "0. Exit", sep='\n')
        choices = input()
        if choices == "1":
            see_project()
        elif choices == "2":
            find_member()
        elif choices == "0":
            break
        else:
            pass


def faculty():
    while True:
        info = my_db.search("login").table
        id_info = [i for i in info if val[0] in i['ID']]
        print(f"Hi, {id_info[0]['username']}")
        notification(id)
        print(f"What do you want to do?\n"
              f"1. See all project",
              "2. See submitted report",
              "3. Evaluation",
              "4. Grade",
              "0. Exit", sep='\n')
        choice = input()
        if choice == '1':
            num = 0
            for i in my_db.search('project').table:
                num += 1
                print(f"{num}.")
                print(f"Title: {i['Title']}")
                print(f"ProjectID: {i['ProjectID']}")
        elif choice == '2':
            sub_project()
        elif choice == '3':
            evaluation()
        elif choice == '4':
            grade()
        elif choice == '0':
            break
        else:
            pass


while True:
    initializing()
    val = login()
    if val[1] == 'admin':
        admin()
        exit()
    elif val[1] == 'student':
        student()
        exit()
    elif val[1] == 'faculty':
        faculty()
        exit()


