# These lines are used to import the modules, I will be using functions of it later in the program.
import FunctionsClassUsed
import datetime
import time

# These lines are printing the title and header of the program. It also prints the rules and instructions for the exam.
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

# These line of codes ask for the user's information (their information is then printed at the end of the exam)
name = str(input("Write your name: "))
teacher = str(input("Write your teacher's name: "))

# This try and except block prevents the user from entering a decimal or string for their grade
# It will also keep asking the user for an input (until they give a valid answer)
while True:
    try:
        grade = int(input("Write your current grade: "))
        break
    except ValueError:
        print("Please input a number (No decimal or letters)")

# This prints out the current date and time using the datetime module
current_date = datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
print("The current date and time is: " + str(current_date))

# This is used to initiate the exam (Users have to press enter and then the functions will run, it will also start
# the timer)
start_exam = input("Press enter to start the exam: ")

# This is the timer, it commences once the user presses enter, and it will continue running until the user finishes
# all the questions
current_time = time.time()

# This calls the function of questions (the questions are created on another file and the commenting will be on the
# other file
FunctionsClassUsed.questions()

# This is also apart of the timer, this stops the timer and measures the time taken for the user to finish all the
# questions
elapsed_time = (time.time() - current_time)

# This line of code calls another function from the function file, the function converts milliseconds into viewable
# numbers (Ex: 1000 milliseconds = 00:01s)
FunctionsClassUsed.timeconverter(int(elapsed_time))

# This if statement prints out the bonus points for the user if they finished the exam in under 3 minutes.
if int(elapsed_time) < 180:
    print("You completed the exam in under 3 minutes, + 2 on your final mark (Note: This bonus is not shown, "
          "add the values yourself)!")

# The final print statement prints out all the user information
print("\nExam Certificate: \nName: " + name + "\nTeacher: " + teacher + "\nGrade: " + str(grade))

