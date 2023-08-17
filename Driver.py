# @author Payton Murphy-Blanchard

import sys
from time import sleep
from calculator import Calculator

def main() :
    EXIT = "5"
    choice = "0"
    welcome_message()
    user_state = main_menu(1)
    
    if user_state == 1 :
        print("I'm sorry, that feature is not available right now.")      
        
    
    elif user_state == 2 :
        calculate_food()
        
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
        pass
    
def calculate_food() :
    gel_type = ""
    need_caffeine = ""
    carbs = int(input("\nHow many carbs will you be consuming per hour? "))
    alltime = input("Enter your ride time in HH:MM\n").split()
    
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
        
    
    
        
        
        
main()