# This Program will check your General Knowledge, on based of 8 questions and print out result in percentage.
import sys
from termcolor import colored, cprint

# This is a Dictionary contains key=value 
quiz ={
    "Question1":{
    "question": "What is the capital of India?",
    "answer" : "New Delhi"
    },
    "Question2":{
    "question": "What is the capital of UK?",
    "answer": "London"
    },
    "Question3":{
    "question": "What is the capital of Sri-lanka?",
    "answer": "colombo"
    },
    "Question4":{
    "question": "What is the capital of Nepal?",
    "answer": "Kathmandu"
    },
    "Question5":{
    "question": "What is the capital of USA?",
    "answer": "Washington DC"
    },
    "Question6":{
    "question": "What is the capital of Italy?",
    "answer": "Rome"
    },
    "Question7":{
    "question": "What is the capital of China?",
    "answer": "Beijing"
    },
    "Question8":{
    "question": "What is the capital of UAE?",
    "answer": "Abu Dhabi"
    },
}

score = 0

# Here we will use above dictionary values as key and value.
for key, value in quiz.items():
    print(value["question"])
    answer = input('answer:')
    if answer.lower() ==  value["answer"].lower():
        print('You are Right')
        score = score + 1
        print("Your Score is " + str(score))
        print("")
    else:
        print("This is Wrong!!" )
        print("The answer is : ", '\033[1m' + value["answer"] + '\033[0m')
        print("")
        print("Your Score is : " + str(score))
        print("")


print ( "You Total Score is: " + str(score) + "/8 ")
print("")
percent = "Your percentile is : " + str(int(score/8 * 100)) + "%"

colorpercent_red = colored("Your percentile is : " + str(int(score/8 * 100)) + "%", "red", attrs=['reverse','bold', 'blink'])
colorpercent_green = colored("Your percentile is : " + str(int(score/8 * 100)) + "%", "green", attrs=['reverse','bold', 'blink'])
print("")

temp = ""
for m in percent:
    if m.isdigit():
        temp = temp + m

fail = 30

if int(temp) < int(fail):
     print(colorpercent_red)
     print("You Need to Improve Your General Knowledge")
else: 
     print(colorpercent_green)
     print("Keep Up the Good Work Flowing!!")

print("")


        
