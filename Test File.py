import datetime
import time
import FunctionsClassUsed
current_date = datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
print("The current date and time is: " + str(current_date))
start_exam = input("Press enter to start the exam: ")
current_time = time.time()
number = int(input("Number: "))
string = input("String: ")
elasped_time = time.time() - current_time

def timeconvert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    print("Time taken on exam: %02dm:%02ds" % (minutes, seconds))

timeconvert(int(elasped_time))
