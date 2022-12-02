# This will give you a calculator program , with choice to choose what you want to do.
# we will import sys and termcolor lib for this.

import sys
from termcolor import colored, cprint
color = colored("See You Soon", "blue", attrs=['reverse', 'blink'] )

# Here we will create functions for add,sub, multiplication and divide methods.

def add(a, b):
    answer = colored( a + b, "red", attrs=['reverse', 'blink'] )
    print("Your Answer is ", "=", '\033[1m' + str(answer) + '\033[0m' + "\n")
    
def sub(a, b):
    answer = colored( a - b, "white", attrs=['reverse', 'blink'] ) 
    print("Your Answer is ", "=", '\033[1m' + str(answer) + '\033[0m' + "\n")

def mult(a, b):
    answer = colored( a * b, "yellow", attrs=['reverse', 'blink'] )
    print("Your Answer is ", "=", '\033[1m' + str(answer) + '\033[0m' + "\n")
  
def div(a , b):
    answer = colored( a / b, "green", attrs=['reverse', 'blink'] )
    print("Your Answer is ", "=", '\033[1m' + str(answer) + '\033[0m' + "\n")

# Now we will use While to loop the above outputs. for every method

while True:
    print("A.", '\033[1m' + 'Addition' + '\033[0m')
    print("B.", '\033[1m' + 'Substraction' + '\033[0m')
    print("C.", '\033[1m' + 'Multiply'  + '\033[0m')
    print("D.", '\033[1m' + 'Division' + '\033[0m')
    print("E.",  '\033[1m' + 'Exit'+ '\033[0m' + "\n")

    Yourchoice = input("input your choice: ")

    if Yourchoice == "a" or Yourchoice == "A":
        print("Addition")
        a = int(input("Please give  your first number: "))
        b = int(input("Please give  your second number: "))
        add(a, b)
    elif Yourchoice == "b" or Yourchoice == "B":
        print("Substraction")
        a = int(input("Please give  your first number: "))
        b = int(input("Please give  your second number: "))
        sub(a, b)
    elif Yourchoice == "c" or  Yourchoice == "C":
        print("Multiply")
        a = int(input("Please give  your first number: "))
        b = int(input("Please give  your second number: "))
        mult(a, b)
    elif Yourchoice == "d" or Yourchoice == "D":
        print("Division")
        a = int(input("Please give  your first number: "))
        b = int(input("Please give  your second number: "))
        div(a , b)
    elif Yourchoice == "e" or Yourchoice == "E":
        print(color)  
        print("")
        quit()
