import FunctionsClassUsed
import datetime
import time
from threading import Thread

timer = 1200
# I will be importing all functions I will need to use for the examination

print("Welcome to the ICS2O1a Examination!")
print("---------------------------------------------------------------------------------------------------------------"
      "----")
print(" This examination will cover every single subject learned in this quadmester, from the understanding computer\n "
      "unit to the basics of python and even computer and society knowledge questions. All answers can be answered\n "
      "with capital or lowercase letters, however, if you have a spelling error, it will not count towards your final\n "
      "score. Follow the instruction on each section EXACTLY in order to ensure full marks when doing the\n "
      "examination. Some questions will be worth more points than others. At the end of the examination,\n "
      "the questions you got wrong will be displayed and the correct answer will be shown with it. There is going to\n "
      "be a timer on this test, you will have 20 minutes to finish this test, if you do not finish the exam in time,\n "
      "the exam will automatically close and the remianing questions unanswered will counted as zero. ")
print("---------------------------------------------------------------------------------------------------------------"
      "-----")

name = str(input("Write your name: "))
while True:
    try:
        grade = int(input("Write your current grade: "))
        break
    except ValueError:
        print("Please input a number (No decimal or letters)")

teacher = str(input("Write your teacher's name: "))

current_date = datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
print("The current date and time is: " + str(current_date))
start_exam = input("Press enter to start the exam: ")
FunctionsClassUsed.questions()
print("\nExam Certificate: \nName: " + name + "\nTeacher: " + teacher + "\nGrade: " + str(grade))

