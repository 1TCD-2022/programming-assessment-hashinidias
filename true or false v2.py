"""
Filename: true_or_false:
Author: Hashini Dias:
Date: July 8th 2022:
Description: This a true or false quiz:
"""

import random

ANSWERS= ["True","True","False","False","True","False","True","True","False","False","True","True"]
QUESTIONS=["Denis Glover wrote the poem The Magpies",
           "God Save the King was New Zealand's national anthem up to and during WWII",
           "Kiri Te kanawa is a wellington-born opera singer",
           "phar Lap was a New Zealand born horse who won the Melbourne Cup",
           "Queen Victoria was the the reigning monarch of England at the time of the treaty",
           "Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80's",
           "Te Rauparaha us credited with intellectual property rights of kamate"
          "The all blacks are New Zealand's top rugby game",
           "The Treaty of Waitangi was signed at parliament",
           "The Treaty of Waitangi was signed in 1901"
           "Thomas Bracken wrote the words to the national anthem God Defends New Zealand",
           "Aotearoa commonly means Land of the Long White Cloud"]

           
print (""" Welcome to true or false, you have 12 questions to answer. A set of question
will pop up try your best to answer correctly, after you have answered you
will know if you answered right or wrong. """)



to_start_game = input("Would you like to start the quiz. Enter Yes or No: ")
if to_start_game.lower() == "yes":
    print ("You entered yes")
    random_question = (random.choice(QUESTIONS))
    print(random_question)
    user_answer = input(" What is the answer, True or False ")
    if user_answer.title() == ANSWERS[QUESTIONS.index(random_question)]:
        print("Good job, you got it correct")
    else:
        print("You got it wrong")
elif to_start_game.lower() == "no":
    print ("You entered no, the game will end now")
