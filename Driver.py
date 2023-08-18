# @author Payton Murphy-Blanchard

import sys
from time import sleep
from calculator import Calculator
from user import User
from reader import Reader

users = {}
stock_SIS_gels = []
stock_160 = []
stock_320 = []
stock_maurten = []
stock_caffeine = []

def main() :
    EXIT = "5"
    choice = "0"
    welcome_message()
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
        get_users("FoodStores.csv", users, passwords, stock_SIS_gels, stock_160, stock_320, stock_maurten, stock_caffeine)
    
def configure_ride() :
    gel_type = ""
    need_caffeine = ""
    carbs = int(input("\nHow many carbs will you be consuming per hour? "))
    alltime = input("How long will you be riding? (Please enter your time in HH:MM). ").split()
    
    for time in alltime :
        hour, min = [int(i) for i in time.split(":")]
    
    if carbs <= 80 :
        gel_type = "Maurten"
    else :
        gel_type = "SIS"
    
    if hour >= 2 :
        need_caffeine = "Yes"
    else : 
        need_caffeine = "No"
        
    new_ride = Calculator(carbs, hour, min, gel_type, need_caffeine)
    new_ride.calculate_food()   
    
def get_users(filename, users, stock_160, stock_320, stock_maurten, stock_caffeine) :
    inFile = filename
    inFile = open(inFile, 'r')
    for line in inFile:
        line = line.rstrip()
        temps = line.split(',')
        users.append(temps[0])
        passwords.append(temps[1])
        stock_160.append(temps[2])
        stock_320.append(temps[3])
        stock_maurten.append(temps[4])
        stock_caffeine.append(temps[5])
        inFile.close()
        
    username = input("Please enter your username: ")
    if username not in users :
        print("It appears that you do not have an account.  Would you like to set one up?")
        user_choice = int(input("Press 1 to set up an account, or 2 to make a calculation as a guest: "))
        if user_choice == 1 :
            new_user = User("", "", 0, 0, 0, 0)
            setup_new_user(users, new_user)
            
    else :
        password = input("Please enter your password: ")
             
             
        if user_choice == 2 :
            configure_ride(users, passwords)
        
def setup_new_user(users, new_user) :
    new_name = input("\nPlease enter your name: ")
    while new_name in users :
        print("I'm sorry, that name is already taken.")
        sleep(1)
        new_name = input("\nPlease enter your name: ")
    new_user.setuser(new_name)
    new_password = input("Please enter your new password (case sensitive): ")
    new_user.setpassword(new_password)
    
    
    
    
main()