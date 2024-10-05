# @author Payton Murphy-Blanchard

import sys
from time import sleep
from calculator import Calculator
from user import User

users = {}
passwords = []
stock_SIS_gels = []
stock_160 = []
stock_320 = []
stock_maurten = []
stock_caffeine = []

def main() :
    welcome_message()
    user_state = 1
    user_states = [1, 2]
    
    while user_state in user_states :
        user_state = main_menu(1)
        if user_state == 1 :
            main_menu(2)
        elif user_state == 2 :
            configure_ride()
        
def welcome_message() :
    print("Hello and welcome to Food Stores, the all in one nutrition calculator!")
    sleep(1)

def main_menu(program_state) :
    if program_state == 1 :
        options = [1, 2]
        user_state = int(input("\nPress 1 to login, or press 2 to make a quick calculation as a guest: "))
        while user_state not in options :
            print("Invalid input.")
            sleep(1)
            user_state = int(input("\nPress 1 to login, or press 2 to make a quick calculation as a guest: "))
        
        return user_state
    
    elif program_state == 2 :
        new_user = get_users("FoodStores.csv", users, stock_SIS_gels, stock_160, stock_320, stock_maurten, stock_caffeine)
        choice = get_choice(new_user)
        while choice != 5 :
            if choice == 1 :
                configure_ride()
            elif choice == 2 :
                add_food(new_user)
            elif choice == 3 :
                subtract_food(new_user)
            elif choice == 4 :
                print(f"\nYou currently have {new_user.stock_SIS} SIS gels, {new_user.stock_160} 160 satchels, {new_user.stock_320} 320 satchels, {new_user.stock_maurten} Maurten gels, and {new_user.stock_caffeine} caffeinated gels.")
            choice = get_choice(new_user)
        end_program("FoodStores.csv", new_user)
        
    
def configure_ride() :
    gel_type = ""
    need_caffeine = ""
    carbs = int(input("\nHow many carbs will you be consuming per hour? "))
    alltime = input("How long will you be riding? (Please enter your time in HH:MM). ").split()
    
    for time in alltime :
        hour, min = [int(i) for i in time.split(":")]
    
    if carbs <= 80 :
        gel_type = "SIS"
    else :
        gel_type = "SIS"
    
    if hour >= 2 and carbs > 100 :
        need_caffeine = "Yes"
    else : 
        need_caffeine = "No"
        
    new_ride = Calculator(carbs, hour, min, gel_type, need_caffeine)
    new_ride.calculate_food()   
    
    return
    
def get_users(filename, users, stock_SIS, stock_160, stock_320, stock_maurten, stock_caffeine) :
    inFile = filename
    inFile = open(inFile, 'r')
    for line in inFile:
        line = line.rstrip()
        temps = line.split(',')
        users[temps[0]] = [temps[1], temps[2], temps[3], temps[4], temps[5], temps[6]]
        
        
        '''users.append(temps[0])
        passwords.append(temps[1])
        stock_160.append(temps[2])
        stock_320.append(temps[3])
        stock_maurten.append(temps[4])
        stock_caffeine.append(temps[5])
        inFile.close()'''
        
    username = input("Please enter your username: ")
    if username not in users :
        print("It appears that you do not have an account.  Would you like to set one up?")
        user_choice = int(input("Press 1 to set up an account, or 2 to make a calculation as a guest: "))
        if user_choice == 1 :
            new_user = User("", "", 0, 0, 0, 0, 0)
            setup_new_user(users, new_user)
            
        elif user_choice == 2 :
            configure_ride()       
            return
            
    else :
        new_user = User(username, users[username][0], users[username][1], users[username][2], users[username][3], users[username][4], users[username][5])
        password = input("Please enter your password: ")
        while password != new_user.getpassword() :
            password = input("Incorrect.  Please enter your password: ")
        print(f"Welcome back {username}")
        
    return new_user
             
             
        
def setup_new_user(users, new_user) :
    new_name = input("\nPlease enter your name: ")
    while new_name in users :
        print("I'm sorry, that name is already taken.")
        sleep(1)
        new_name = input("\nPlease enter your name: ")
    new_user.setuser(new_name)
    new_password = input("Please enter your new password (case sensitive): ")
    new_user.setpassword(new_password)
    new_SIS = int(input("Please enter the number of SIS gels you currently have: "))
    new_user.setSIS(new_SIS)
    new_160 = int(input("Please enter the number of Maurten 160 satchels you currently have: "))
    new_user.set160(new_160)
    new_320 = int(input("Please enter the number of Maurten 320 satchels you currently have: "))
    new_user.set320(new_320)
    new_maurten = int(input("Please enter the number of non-caffeinated Maurten gels you currently have: "))
    new_user.setmaurten(new_maurten)
    new_caffeine = int(input("Please enter the number of caffeinated gels you currently have: "))
    new_user.setcaffeine(new_caffeine)
    
    users[new_name] = [new_password, new_SIS, new_160, new_320, new_maurten, new_caffeine]
    
    return

def get_choice(new_user) :
    print(f"\nYou currently have {new_user.stock_SIS} SIS gels, {new_user.stock_160} 160 satchels, {new_user.stock_320} 320 satchels, {new_user.stock_maurten} Maurten gels, and {new_user.stock_caffeine} caffeinated gels.")
    new_user.inventorycheck()
    choices = [1, 2, 3, 4, 5]
    print("\n(1) Calculate the food for a new ride.")
    print("(2) Add food to your supply.")
    print("(3) Remove food from your supply.")
    print("(4) View your supply.")
    print("(5) Exit and save.")
    choice = int(input("Choice? "))
    while choice not in choices :
        print("Unknown choice.  Please try again.")
        sleep(1)
        print("\n(1) Calculate the food for a new ride.")
        print("(2) Add food to your supply.")
        print("(3) Remove food from your supply.")
        print("(4) View your supply.")
        print("(5) Exit and save.")
        choice = int(input("Choice? "))       
    return choice    

def add_food(new_user) :
    choices = [1, 2, 3, 4, 5]
    print("What food would you like to add?")
    print("\n(1) SIS gels")
    print("(2) 160 Satchels")
    print("(3) 320 Satchels")
    print("(4) Maurten gels")
    print("(5) Caffeinated gels")
    choice = int(input("Choice? "))
    while choice not in choices :
        choice = int(input("Invalid choice.  Please try again: "))
    x = int(input("How much would you like to add? "))
        
    if choice == 1 :
        new_user.setSIS(int(new_user.stock_SIS) + x)
    if choice == 2 :
        new_user.set160(int(new_user.stock_160) + x)
    if choice == 3 :
        new_user.set320(int(new_user.stock_320) + x)
    if choice == 4 :
        new_user.setmaurten(int(new_user.stock_maurten) + x)
    if choice == 5 :
        new_user.setcaffeine(int(new_user.stock_caffeine) + x)
        
    return

def subtract_food(new_user) :
    choices = [1, 2, 3, 4, 5]
    print("What food would you like to subtract?")
    print("\n(1) SIS gels")
    print("(2) 160 Satchels")
    print("(3) 320 Satchels")
    print("(4) Maurten gels")
    print("(5) Caffeinated gels")
    choice = int(input("Choice? "))
    while choice not in choices :
        choice = int(input("Invalid choice.  Please try again: "))
    x = int(input("How much would you like to subtract? "))    
    if choice == 1 :
        new_user.setSIS(int(new_user.stock_SIS) - x)
    if choice == 2 :
        new_user.set160(int(new_user.stock_160) - x)
    if choice == 3 :
        new_user.set320(int(new_user.stock_320) - x)
    if choice == 4 :
        new_user.setmaurten(int(new_user.stock_maurten) - x)
    if choice == 5 :
        new_user.setcaffeine(int(new_user.stock_caffeine) - x)    
        
    return

def view_food(user) :
    pass

def end_program(filename, new_user) :
    users[new_user.user] = [new_user.password, new_user.stock_SIS, new_user.stock_160, new_user.stock_320, new_user.stock_maurten, new_user.stock_caffeine]
    inFile = filename
    inFile = open(inFile, 'w')
    new_file = ""
    for user in users.keys() :
        new_file += str(user) + ","
        for x in users[user] :
            new_file += (str(x) + ",")
        new_file += "\n"
    inFile.write(new_file)
    inFile.close()
    print("Thank you for using Food Stores!  Your information has been saved!")
    sys.exit()
        
        
    
main()