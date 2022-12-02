# This programm will check if the URL is running or not.

import urllib.request as urllib 
from termcolor import colored, cprint

not_reachable = colored("Site Not Working", "red", attrs=['reverse', 'bold', 'underline'])


def checker(url):
    print("Checking Connectivity")
    print("")
    responce = urllib.urlopen(url)

    color_code = colored(responce.getcode(),"green", attrs=['reverse', 'bold', 'blink'] )

    if responce.getcode() == 200:    
     print("Connected to", url , "Succesfully")
     print("")
     print("The responce code was:", color_code)
     print("")
    else:
     print (not_reachable)
    

print("This Program will check Websites avaibility" + "\n")
print("")
input_url=input("Please Input the Websites URL To check: ")
print("")
checker(input_url)


