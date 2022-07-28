"""
Filename: true_or_false:
Author: Hashini Dias:
Date: July 8th 2022:
Description: This a true or false quiz:
"""

import random

ANSWERS= ["True","True","False","False","True","False","True"]
QUESTIONS=["Denis Glover wrote the poem The Magpies",
           "God Save the King was New Zealand's national anthem up to and during WWII",
           "Kiri Te kanawa is a wellington-born opera singer",
           "phar Lap was a New Zealand born horse who won the Melbourne Cup",
           " Queen Victoria was the the reigning monarch of England at the time of the treaty",
           "Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80's",
           "Te Rauparaha us credited with intellectual property rights of kamate"]
          
print (""" Welcome to true or false, you have 7 questions to answer. A set of question
will pop up try your best to answer correctly, after you have answered you
will know if you answered right or wrong. """)

user_answer = input ("Would you like to start the quiz. Enter Yes or No")
if user_answer == "Yes":
    print (" you entered Yes")

elif user_answer =="No":
    print (" You entered No")
    
