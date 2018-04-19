# -*- coding: utf-8 -*-
"""
@author: Amaury Ortega <amauryocortega@gmail.com>
"""
import re
from Digit import Digit


def usage():
    return """    LCD_Printer
    @author: Amaury Ortega <amauryocortega@gmail.com>
    
    Program to print numbers in LCD style.
    
    Input should have this format: SIZE,####
    Where:
        SIZE: Digit from 1 to 10
        ####: Any sequence of digits
    ------------------------------------------
    |Special Input: 0,0 will stop the program|
    ------------------------------------------
    """


def wrongInput(user_input):
    return "Wrong input '" + user_input + "' please, verify the format.\n" + """
    Input should have this format: SIZE,####
    Where:
        SIZE: Digit from 1 to 10
        ####: Any sequence of digits
    ------------------------------------------
    |Special Input: 0,0 will stop the program|
    ------------------------------------------
    """


def main():
    # Usage
    print(usage())
    # Main loop
    while True:
        # Input
        user_input = str(input("Input: "))

        # Verify input with regex
        if not re.match("^(([1-9]|10),[0-9]+|0,0)$", user_input):
            # Wrong input format
            print(wrongInput(user_input))
        elif not user_input == "0,0":
            # Right input
            size, digits = user_input.split(",")

            # Preparing for output
            output = ["" for line in range(int(size) * 2 + 3)]

            # Dealing with each digit individually
            for digit in digits:
                # Instancing Digit class
                digit_to_print = Digit(int(size), int(digit))

                # Adding Digit in LCD format to output array
                for line_index in range(len(output)):
                    output[line_index] += digit_to_print.lcdNumber()[line_index] + " "

            # Showing all lines
            for line in output:
                # Removing that last " "
                print(line[:-1])
        else:
            # 0,0
            # End of program
            print("Thanks for using this software")
            break

# Main
if __name__ == '__main__':
    main()
