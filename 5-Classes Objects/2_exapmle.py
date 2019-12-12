from os import system
from time import sleep

clear = lambda: system('clear')

def wait():
    for i in range(7):
        print("*", end=" ")
        sleep(0.2)

def welcome_screen():
    print("""
          ***      ******      ***   
        *** Welcome to Nimdows PX ***
          ***      ******      ***
    """)
    sleep(2)
    clear()

def calculator():
    
    while True:
        print("""   Calculator
                ----------------
          ( + ), ( - ), ( * ), ( / )
                     Exit: "e"    """)
        
        num1 = input("Enter the first number:")
        calc_op = input("Enter the operation:")
        num2 = input("Enter the second number:")

        if calc_op == "+":
            print("{} + {} = {}".format(num1, num2, num1 + num2))
        
        elif calc_op == "-":
            print("{} + {} = {}".format(num1, num2, num1 - num2))
        
        elif calc_op == "*":
            print("{} + {} = {}".format(num1, num2, num1 * num2))
        
        elif calc_op == "/":
            print("{} + {} = {}".format(num1, num2, num1 / num2))
        
def clock():

    

class Computer():
    def __init__(self, comp_stat = "off", screen_stat = "off", volume_stat = 0, app_list=["calculator"], app="desktop"):
        
        self.comp_stat = comp_stat
        self.screen_stat = screen_stat
        self.volume_stat = volume_stat
        self.app_list = app_list
        self.app = app

    def turn_on_comp(self):
        
        if self.comp_stat == "on":
            print("Computer is already on.")

        else:
            print("Your computer is openning.")
            wait()
            self.comp_stat = "on"
    
    def turn_on_screen(self):

        if self.screen_stat == "on":
            print("Screen is already on.")

        else: 
            print("Openning screen")
            self.screen_stat = "on"
    
    def volume_setting(self):

        while True:
            vol_choice = input("Volume down: '<'\nVolume up: '>'\nExit: e\nSelect operation:")
            
            if vol_choice == "<":
                if self.volume_stat != 0:
                    self.volume_stat -= 1
                    print("Volume:", self.volume_stat)

            elif vol_choice == ">":
                if self.volume_stat != 20:
                    self.volume_stat += 1
                    print("Volume:", self.volume_stat)
            
            elif vol_choice == "e":
                break

            else:
                print("Wrong choice.")
                sleep(1)
    
    def add_new_app(self, app_name):
        print("""
              ------------------------------------------
              --- Available applications to install  ---
              ------------------------------------------
              ---    1.Calculator                    ---
              ---    2.Clock                         ---
              ---    3.Snake Game                    ---
              ---    4.Rock Paper Scissor Game       ---
              ---    5.Fuel Calculation              ---
              ------------------------------------------
              """)
        self.app_list.append(app_name)
        print("New application was installed")

    def __len__(self):
        
        return len(self.app_list)
    
    def __str__(self):
        
        return "\nComputer status: {}\nScreen status: {}\nVolume: {}\nCurrent application: {}\nInstalled applications: {}\n".format(self.comp_stat, self.screen_stat, self.volume_stat, self.app, self.app_list)

    def tools_menu(self):
        
        while True:
            
            answer = input("""
              ------------------------------------------
              ---       Tools                        ---
              ------------------------------------------
              ---    1. Calculator                   ---
              ---    2. Clock                        ---
              ---          Exit (e)                  ---
              ------------------------------------------
             """)
            
            if answer == "1":
                calculator()

            elif answer == "2":
                clock() 
            
            elif answer == "e":
                break

                


asus = Computer()   # My object 

welcome_screen()

print("""
    ------------------------------------------
    ---       Nbendows Menu                ---
    ------------------------------------------
    ---    1. Tools                        ---
    ---    2. Games                        ---
    ---    3. Settings                     ---
    ---    4. Software Manager             ---
    ---    5. Help                         ---
    ---    6. Shutdown the computer        ---
    ------------------------------------------
    """)

while True:
    operation = input("Select the operation:")

    if operation == "1":






