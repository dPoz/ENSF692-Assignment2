# input_processing.py
# David Pozniak, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

import sys

class Sensor:

    def __init__(self, light, person, vehicle):
        self.state1 = [0 ,light , person, vehicle]

    # update_status(self, change,change_to_what) takes itself, what to change (e.g. light, person, vehicle), and what it changes to and updates
    # the state of the object to reflect those changes. It returns nothing, but modifies the properties of the object.
    def update_status(self, change, change_to_what): 
        self.state1[change] = change_to_what

# print_message(sensor) takes an object of class Sensor and prints out the required action, followed by the objects current state.
# print_message(sensor) returns nothing.
def print_message(sensor):
    message = "Light =", sensor.state1[1], ", Pedestrian =", sensor.state1[2], ", Vehicle =", sensor.state1[3], ".\n"
    if (sensor.state1[1] == "green" and sensor.state1[2] == "no" and sensor.state1[3] == "no"):
        print("\nProceed\n")
        print(*message)
    elif(sensor.state1[1] == "yellow" and sensor.state1[2] == "no" and sensor.state1[3] == "no"):
        print("\nCaution\n")
        print(*message)
    else:
        print("\nSTOP\n")
        print(*message)

# main() function is to provide a simple engine enabling Car Vision Detector Processing, it continuously monitors for any changes in
# the state with respect to light, person, and vehicle, updates the state, and provides instructions based on the updated state.
# main() function has 2 tuples and 1 object. The two tuples are used to validate "vision" input to enable  improper input handling
# as required. The object is of class Sensor, with default "Proceed" state of "green", "no", "no", for light, person, vehicle, respectively.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    # Creating an object of type sensor with default state condition of: "green", "no", "no", for light, person, vehicle, respectively.
    sense = Sensor("green", "no", "no")
    
    # Both valid* tuples are to validate vision input, they are the only acceptable inputs.
    validVisionChange = ("green", "red", "yellow", "yes", "no")
    validVisionInput = ("0", "1", "2", "3")

    # This is the primary while loop that allows continuous Car Vision Detector Processing, the only way to end the program is to enter 0.
    while True:

        change = ""

        # The Car Vision Detector Processor continuously monitors for any valid vision input. If an invalid vision input is identified, the
        # message "You must select either 1, 2, 3, or 0.", is printed.
        while change not in validVisionInput:
            print("Are changes are detected in the vision input?")
            change = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
            if change not in validVisionInput:
                print("You must select either 1, 2, 3, or 0.\n")
            
        # exit if input is "0".
        if change == "0": 
            sys.exit()
        else:
            change = int(change)

        # Once valid input is detected, Car Vision Detector Processor identifies the new state.
        change_to_what = input("What change has been identified?: ")

        # exit if input is "0".
        if change_to_what == "0": 
            sys.exit()

        # If an invalid new state is identified, the message "Invalid vision change", followed by the instruction and current state, is printed.
        if change_to_what in validVisionChange:
            sense.update_status(change, change_to_what)
        else:
            print("Invalid vision change.")

        print_message(sense)

if __name__ == '__main__':
    main()