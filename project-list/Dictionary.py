# This will give you a programm with diffrent dictionary methods.
from PyDictionary import PyDictionary
dictionary = PyDictionary()

while True:
    print("A.", '\033[1m' + 'WORD' + '\033[0m')
    print("B.", '\033[1m' + 'ANTONYM' + '\033[0m')
    print("C.", '\033[1m' + 'SYNONYMS'  + '\033[0m')
    print("D.", '\033[1m' + 'TRANSLATE' + '\033[0m')
    print("E.",  '\033[1m' + 'Exit'+ '\033[0m' + "\n")

    Yourchoice = input("input your choice: ")

    if Yourchoice == "a" or Yourchoice == "A":
        print("WORD")
        print()
        Word = (input("Please type the Word, You need Meaning of: "))
        print()
        ret_word = dictionary.meaning(Word)
        print(ret_word)
        print()
    elif Yourchoice == "b" or Yourchoice == "B":
        print("ANTONYM")
        print()
        ant = (input("Please type the Word, You need antonyms of: "))
        print()
        print(dictionary.antonym(ant))
    elif Yourchoice == "c" or Yourchoice == "C":
        print("SYNONYMS")
        print()
        syn = (input("Please type the Word, You need synonyms of: "))
        print()
        print (dictionary.synonym(syn)) 
    elif Yourchoice == "d" or Yourchoice == "D":
        print("TRANSLATE")
        print()
        trans = (input("Please type the Sentence, You need to Translate : "))
        print()
        print (dictionary.translate(trans,'hi')) 
    else:
        Yourchoice == "e" or Yourchoice == "E"
        print()
        print("GoodBye, Take Care!")
        print()
        quit()