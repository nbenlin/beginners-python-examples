import random
import time
import os

clear = lambda: os.system('cls')

def waiting():
    
    for i in range(1, 8):
        print("*", end="")
        time.sleep(0.3)
    clear()
    

class Remote_control():

    def __init__(self, tv_status = "Off", tv_volume = 0, channel_list = ["TTV"], channel = "TTV"):
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel
    
    def tv_on(self):
        
        if self.tv_status == "On":
            print("TV is already on... . .")
        else:
            print("TV turning on")
            waiting()
            self.tv_condition = "On"

    def tv_off(self):

        if self.tv_status == "Off":
            print("TV is already off... . . .")
        else:
            print("TV is shutting down")
            waiting()
            self.tv_status = "Off"

    def volume_settings(self):

        while True:
            answer = input("Volume down: '<'\nVolume up: '>'\nExit: e\nSelect operation:")

            if answer == "<":
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print("Volume:", self.tv_volume)
            elif answer == ">":
                if self.tv_volume != 30:
                    self.tv_volume += 1
                    print("Volume:", self.tv_volume)
            elif answer == "e":
                print("Volume settings are updated.")
                break
            else:
                print("Volume down: '<'\nVolume up: '>'\nExit: exit")
        
    def add_channel(self, channel_name):

        print("Adding new channel....")
        waiting()
        self.channel_list.append(channel_name)
        print("New channel added... . .")

    def random_channel(self):

        rand_ch = random.randint(0, len(self.channel_list) - 1)
        self.channel = self.channel_list[rand_ch]

        print("Current channel:", self.channel)

    def __len__(self):
        
        return len(self.channel_list)

    def __str__(self):
        return "\nTV status: {}\nTV volume: {}\nChannel list: {}\nCurrent channel: {}\n".format(self.tv_status, self.tv_volume, self.channel_list, self.channel)

remote_control = Remote_control()   # Here we create the object 

print("""
***********************************
****      TV Application       ****
***********************************
****    1. Turn On TV          ****
****    2. Turn Off TV         **** 
****    3. Volume Settings     ****
****    4. Add new channel     ****
****    5. Number of channels ****
****    6. Random channel      ****
****    7. TV information      ****
****                           ****
****    (For exit press q)     ****
***********************************
""")

while True:

    operation = input("Select operation:")

    if operation == "q":
        print("Application is closing...")
        waiting()
        break

    elif operation == "1":
        remote_control.tv_on()
    
    elif operation == "2":
        remote_control.tv_off()
    
    elif operation == "3":
        remote_control.volume_settings()
    
    elif operation == "4":
        channel_names = input("Enter channels using the ',' :")

        channel_list = channel_names.split(",")

        for i in channel_list:
            remote_control.add_channel(i)
    
    elif operation == "5":
        print("Number of channels:", len(remote_control))

    elif operation == "6":
        remote_control.random_channel()

    elif operation == "7":
        print(remote_control)

    else:
        print("Invalid operation... .")


