import time
import datetime
from threading import Thread


# This function asks the user for thier information
def getinformation():
    name = str(input("Write your name: "))
    while True:
        try:
            grade = int(input("Write your current grade: "))
            break
        except ValueError:
            print("Please input a number (No decimal or letters)")

    teacher = str(input("Write your teacher's name: "))

    current_date = datetime.datetime.now()
    print("The current date and time is: " + str(current_date))
    print("Once the exam starts, the timer will begin and you will have 20 minutes to do the exam. The timer will be "
          "displayed for you to see.")
    start_exam = input("Press enter to start the timer and exam: ")


# This sets the timer, it will start when the user finishes the previous function
def timer(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        countdown = '{:02d}:{:02d}'.format(mins, secs)
        print(countdown, end="\r")
        time.sleep(1)
        t -= 1
    print("Exam is over")


def questions():
    number = int(input("Write a number: "))
    string = input("Write a string: ")


if __name__ == '__main__':
      Thread(target=timer(int(20))).start()
      Thread(target=questions()).start()
