import string
import random
from user import User
from user import Credentials

def create_user(username, password):
    """
    Function to create a user
    """
    new_user = User(username, password)
    return new_user

def save_user(user):
    """
    Function to save a user
    """
    user.save_user()

def delete_user(user):
    """
    Function to delete a user
    """
    user.delete_user()

def find_user(number):
    """
    Function to find a user
    """
    return User.find_user__by_number(number)

def display_user():
    """
    Function to display users
    """
    return User.display_users()

def create_account(account_username, account_name, account_password):
    """
    Function to create a new accounts object
    """
    new_account = Credentials(account_username, account_name, account_password)
    return new_account

def save_account(user):
    """
    Function to save a created account object
    """
    user.save_account()

def delete_account(user):
    """
    Function to delete a Credentials 
    """
    user.delete_user()

def find_account(number):
    """
    Function to find credentials by username
    """
    return Credentials.find_account_by_number(number)

def display_account():
    """
    Function to display accounts
    """
    return Credentials.display_account()



def main():
    while True:
        print("-" * 70)
        print("Welcome to Password Locker. Select Signup or Login to continue")
        print("-" * 70)
        print("Signup or Login")
        option = input().lower()

        if option  == "signup":
            print("\n")
            print("Create Account")
            print("-" * 25)
            print("Enter name...")
            name= input()
            print("Enter username...")
            username = input()
            print("Set  password...")
            password = input()
            save_user(create_user(username, password))
            print("Your account was created successfully using the following details")
            print("-"*10)
            print(f"Name: {name}\nUsername: {username} \nPassword: {password}")
            print("\n")

        elif option == "login":
            print("Enter Username")
            login_username = input()
            print("Enter Password")
            login_password  = input()
            
            if find_user(login_password):
                print("\n")
                print("To create a credential (CC),view a credential (VC) or delete a credential (DC) ")
                print("-"*50)
                print("CC or VC")
                choose = input().lower()

                if choose == 'cc':
                    print("Add your Account Credentials")
                    print('-' *25)
                    account_username = login_username
                    print("Enter Account Name")
                    account_name = input()
                    print("\n")
                    print("Generate Random Password(R) or Create New Password(N)")
                    decision = input().lower()
                    if decision == 'r':
                        characters = string.ascii_letters +string.digits
                        account_password = ''.join(random.choice(characters)
                        for x in range(random.randint(6, 16))) 
                        print(f'Password: {account_password}')
                    elif decision == 'n':
                        print("Enter Your Password")
                        account_password = input()
                    else:
                        print("Enter a  valid choice")
                    save_account(create_account(account_username, account_name, account_password))
                    print("\n")
                    print(account_username, account_name, account_password)

                elif choose == "vc":
                    if(find_account(account_username)):
                        print("Here is a list of your account credentials")
                        print("-"*25)
                        for user in display_account():
                            print(f"Account: {user.account_name} \nPassword: {user.account_password} \n\n")

                elif choose == "dc":
                    print("Enter the account name of the Credentials you want to delete")
                    search_name = input().lower()
                    search_name = input().lower()

                    if(find_account(search_name)): 
                        delete_account(search_name)    
                        print("-"*25)
                        for account in display_account():
                            print(f"Account: {account.account_name} \nPassword: {account.account_password} deleted successfully")
                     
                    else:
                        print("Invalid Credentials")
                else:
                    print("Please try again")
            else:
                print("Incorrect Info. Please try again")
                print("\n")
        else:
            print("Kindly choose a valid option")  
            print("\n")
if __name__ == '__main__':
    main()