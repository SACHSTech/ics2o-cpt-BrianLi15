import FunctionsClassUsed
import datetime
import time

print("Welcome to the ICS2O1a Examination!")
print("\n---------------------------------------------------------------------------------------------------------------"
      "----")
print(" This examination will cover every single subject learned in this quadmester, from the understanding computer\n "
      "unit to the basics of python and even computer and society knowledge questions. All answers can be answered\n "
      "with capital or lowercase letters, however, if you have a spelling error, it will not count towards your final\n "
      "score. Follow the instruction on each section EXACTLY in order to ensure full marks when doing the\n "
      "examination. The bonus questions will be worth more points than others. At the end of the examination,\n "
      "the questions you got wrong will be displayed and the correct answer will be shown with it. You will be timed\n "
      "during this examination, your time taken will be shown at the end, if you finish the exam in under 3 minutes,\n "
      "you will be rewarded two extra points on your final mark. ")
print("---------------------------------------------------------------------------------------------------------------"
      "-----\n")

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

current_time = time.time()
FunctionsClassUsed.questions()
elapsed_time = (time.time() - current_time)

FunctionsClassUsed.timeconverter(int(elapsed_time))
if int(elapsed_time) < 180:
    print("You completed the exam in under 3 minutes, + 2 on your final mark (Note: This bonus is not shown, "
          "add the values yourself)!")
print("\nExam Certificate: \nName: " + name + "\nTeacher: " + teacher + "\nGrade: " + str(grade))

