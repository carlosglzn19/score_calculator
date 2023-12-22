'''Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.'''

#Input section
score_input = input("Enter score between 0.0 and 1.1: ")

#Looking for typing errors
try:
    score = float(score_input)
except:
    print("Please try again and enter a valid number")
    quit()

#Checking grades and score range
if score < 0.0 or score > 1.0:
    print("Please enter a number between 0.0 and 1.1")
elif score >= .9:
    print("A")
elif score >= .8:
    print("B")
elif score >= .7:
    print("C")
elif score >= .6:
    print("D")
else:
    print("F")