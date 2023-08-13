import os

from threading import Thread
from time import sleep

import real_time_data
import saved_data
from api import start_api


def start_command_loop():
    while True:
        command = input("Give input").split(" ")
        #TODO could add help command which tells what commands can be used. Could also add quit command.
        if len(command) < 2 or len(command) > 3:
            print("Wrong number of arguments in input")
        if len(command) == 2 and command[0] == "get":
            print(real_time_data.get_data(command[1]))
        elif len(command) == 3 and command[0] == "get" and command[1] == "saved":
            saved_data.get_data(command[2])
        else:
            print("Something wrong with the input. PLease confirm that it is correct")

def start_api_func():
    start_api()

if __name__ == '__main__':
    # Change the working dir to the dir of this file
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    print(dname)
    os.chdir(dname)

    # Start the cli and api in their own threads so both of them can be used simultanously
    p1 = Thread(target=start_api_func)
    p1.start()
    # Wait for a moment that api has the time to start. This way the text in the command prompt will be cleaner.
    sleep(1)
    p2 = Thread(target=start_command_loop)
    p2.start()
    p1.join()
    p2.join()

