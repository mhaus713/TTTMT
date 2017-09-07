import sys
import TTTMTDict

def main(argv) :

    output = ""

    filename = input("please enter the name of the file you'd like to read: ")

    with open('filename') as f:
        line = f.readlines()

    for line in f:
        if line == "UUUEEGGH?!?!":
            output += ">"
        elif line == "EELREEEE??!!":
            output += "<"
        elif line == "EELLROOO?!?!?":
            output += "+"
        elif line == "AAARRGHHROOO?!?":
            output += "-"
        elif line == "REEREE!!??":
            output += "]"
        elif line == "AAARRGHHREE?!?!":
            output += "["
        elif line == "EEE!!!!":
            output += "."
        elif line == "VRROOOOM!!!!":
            output += ","

