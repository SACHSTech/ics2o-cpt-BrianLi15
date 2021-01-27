""""
Due to the constant repetition of the same format of codes used throughout my program, I have decided to explain each
primary QUESTION section instead of commenting on every question in the file. All question's created and used will be
explained on this file.
"""

# To begin... we have to first label some count variables, as well as import a module for future purposes.
import datetime
count = 0
correct_answer = "Questions You Got Wrong: \n"

"""
- The count variable will keep count of the user's test score. When they get a question correct, their count will go up
by one, if they get it wrong, the count will remain the same. At the end of the test, the count will be printed out 
for the user to see.
 
- The "correct_answer" variable keeps track of the user input, and what they get wrong. On each question, an else 
statement will be there to indicate if the user input is WRONG. This means that when a user's answer is incorrect, their
input will then be added to this variable along with the correct answer. This information will then be printed after the
exam is over. (This will be shown later)
"""

# We can demonstrate the variable's importance and role through the first question:
print("\nComputer Unit Measurements\n--------------------------")
print("[Knowledge Questions]\n")
question_one = input("1.\tType the LETTER symbol for the computer unit, \"Bit\": \n")
if question_one.strip() == "b":
    count += 1
else:
    correct_answer += "1.\tYour Answer: " + question_one + "\t[Correct Answer: b]\n"


# Header (print statements), this indicates a section of the exam.
print("\nComputer Unit Measurements\n--------------------------")
print("[Knowledge Questions]\n")

# Asks for user input (Question statement)
question_one = input("1.\tType the LETTER symbol for the computer unit, \"Bit\": \n")

# Processes whether or not the user input is correct. If the user's input is "b", then the count variable will go up
# and the correct_answer variable is NOT BEING USED.
# If the user input is WRONG, it will go to the else statement, where it then adds the user's answer along with the
# actual correct answer into the "correct_answer" variable
if question_one.strip() == "b":
    count += 1
else:
    correct_answer += "1.\tYour Answer: " + question_one + "\t[Correct Answer: b]\n"

"""
The question shown above was a basic input question, about half of the exam's questions consists of this format.
The basic knowledge questions and fill in the blank questions all follow this basic format and only vary between the
beginning print statements.
"""

# Example of a fill in the blank question, notice how the format is the same:
question_five = input("5.\tMB/s, MBps, GB/s GBps) measures how much data can be ____: \n")
if question_five.strip().lower() == "transferred":
    count += 1
else:
    correct_answer += "5.\tYour Answer: " + question_five + "\t[Correct Answer: transferred]\n"


# However, a sub category of these questions exist, number questions, which call for the use of try and except blocks.
# An example of this question is shown in question 3:
while True:
    try:
        question_three = int(input("\n3.\tHow many bytes does 16 bits equal? (Input your answer in the form of a "
                                       "number): \n"))
        break
    except ValueError:
        print("Please input your answer in the form of a number")
if question_three == 2:
    count += 1
else:
    correct_answer += "3.\tYour Answer: " + str(question_three) + "\t[Correct Answer: 2]\n"

# The processing follows the same format (if and else statements, if user input is correct, count += 1, if wrong,
# their input is then recorded) However, the difference is this block of code:

while True:
    try:
        question_three = int(input("\n3.\tHow many bytes does 16 bits equal? (Input your answer in the form of a "
                                       "number): \n"))
        break
    except ValueError:
        print("Please input your answer in the form of a number")

# by putting a while True statement along with a try and except block, it will continue asking the user for an integer
# as the question asks for an answer in the form of a number. The while loop breaks once the user enters a integer.

# Now, the remaining question format is the multiple choice questions:
print("\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]\n")
while True:
    print("This type of software or malware is installed on a computing device without the user's knowledge")
    print(
        "16.\tBased on the description, what type of computer virus is this?:\nA. Spyware\t B. Trojan\t C. Adware")
    question_sixteen = input()
    if question_sixteen.strip().lower() == "a":
        count += 1
        break
    elif question_sixteen.strip().lower() == "b" or question_sixteen.strip().lower() == "c":
        correct_answer += "16.\tYour Answer: " + question_sixteen + "\t[Correct Answer: A]\n"
        break
    else:
        print("Please enter a correct option (A, B, or C)")

# Although it looks significantly bigger and longer, the base processing and formatting is the same.

# This prints out a section header, indicating that the user has reached the multiple choice portion of the exam
print("\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]\n")

# The series of print statements ask the question, and the input statement below asks for the user input.
# Note: These statements are in a while loop, which means that it will repeatedly ask the user for an input if they
# do not enter an answer of "A", "B", or "C". Numbers and words will be rejected.
print("This type of software or malware is installed on a computing device without the user's knowledge")
print("16.\tBased on the description, what type of computer virus is this?:\nA. Spyware\t B. Trojan\t C. Adware")
question_sixteen = input()

# This answer validation is demonstrated in the if-elif statements:
if question_sixteen.strip().lower() == "a":
    count += 1
    break
elif question_sixteen.strip().lower() == "b" or question_sixteen.strip().lower() == "c":
    correct_answer += "16.\tYour Answer: " + question_sixteen + "\t[Correct Answer: A]\n"
    break
else:
    print("Please enter a correct option (A, B, or C)")

"""
If the user's answer is the correct letter, it will break from the while loop and add a point to their final score
If the user's answer is one of the options, it will break from the loop but it won't add a point to their final score.
Instead, it will add to the "correct_answer" variable which is used to display what the user got wrong at the end.

If the user input is not "A", "B", or "C", then it will ask for another input (shown as else statement)
"""

# The three PRIMARY forms of questions on the exam are the one's explained above, now moving on to....
# BONUS QUESTIONS!!
print("\n[Bonus Questions!]")
print("\nFor these harder questions, they are worth one to three points each.")
print(
    "you will have three attempts to do them, it will ask for another input if your answer is wrong. The points you")
print("get for answering each question correct will be determined based on your number of attempts for each. ")
print("(First attempt = 3 points, second attempt = 2 points and third attempt = 1 points)\n")
user_attempt = 0
list_attempts = []
print_boolean = True
while user_attempt != 3:
    question_thirtythree = input("33.\tWhat is the method signature for a class constructor?: \n")
    user_attempt += 1
    if question_thirtythree.strip().lower() == "def __init__(self)" and user_attempt == 1:
        count += 3
        print("Correct!")
        print_boolean = False
        break
    elif question_thirtythree.strip().lower() == "def __init__(self)" and user_attempt == 2:
        count += 2
        print("Correct!")
        print_boolean = False
        break
    elif question_thirtythree.strip().lower() == "def __init__(self)" and user_attempt == 3:
        count += 1
        print("Correct!")
        print_boolean = False
        break
    list_attempts.append(question_thirtythree)
if print_boolean:
    correct_answer += "33.\tYour Answers:\nAttempt One: " + list_attempts[0] + "\nAttempt Two: " + \
                      list_attempts[1] + "\nAttempt Three: " + list_attempts[
                          2] + "\n[Correct Answer: def __init__(self)]"

# Although this looks excruciatingly long, I will break up the main portion of the question with comments:

# These are all print statements used to explain the rules of the bonus question
print("\n[Bonus Questions!]")
print("\nFor these harder questions, they are worth one to three points each.")
print("you will have three attempts to do them, it will ask for another input if your answer is wrong. The points you")
print("get for answering each question correct will be determined based on your number of attempts for each. ")
print("(First attempt = 3 points, second attempt = 2 points and third attempt = 1 points)\n")

# These are variables that are set up for the question (They will be altered depending on the user's input:
# - "user_attempt" being used to track the number of user attempts.
# - "list_attempts" being used to record all of the user's input
# - "print_boolean" being used to track whether or not the user's answers was correct.
user_attempt = 0
list_attempts = []
print_boolean = True

# This while loop is used to measure the user's attempt, everytime they submit an answer that's WRONG, it will add a
# point into the user's attempt, and ask the question again. When the user_attempt reaches 3 points, the while loop will break.
while user_attempt != 3:
    question_thirtythree = input("33.\tWhat is the method signature for a class constructor?: \n")
    user_attempt += 1

# Now, this series of if-elif statements are used to calculate the amount points the user will get based on their number
# of attempts. As shown below, if their input is the correct answer and it's their first attempt, 3 points is rewarded.
# Additionally, notice how it changed to print_boolean from True to False. (I will explain this right after)
# It also adds their answers to a list if their input is WRONG. This will be used to print out later.
    if question_thirtythree.strip().lower() == "def __init__(self)" and user_attempt == 1:
        count += 3
        print("Correct!")
        print_boolean = False
        break
    elif question_thirtythree.strip().lower() == "def __init__(self)" and user_attempt == 2:
        count += 2
        print("Correct!")
        print_boolean = False
        break
    elif question_thirtythree.strip().lower() == "def __init__(self)" and user_attempt == 3:
        count += 1
        print("Correct!")
        print_boolean = False
        break
    list_attempts.append(question_thirtythree)

# After the while loop is done, it goes the print_boolean statement. If the user answered the question correctly in the
# given three attempts, the print_boolean is turned False, and thus, will not add anything to the "correct_answer" variable.
# If the user didn't get the correct answer in all three attempts, it will execute the print_boolean variable and thus,
# add the user's attempt to the correct_answer variable. All of the user's attempt is stored in a list and will be printed.
if print_boolean:
    correct_answer += "33.\tYour Answers:\nAttempt One: " + list_attempts[0] + "\nAttempt Two: " + \
                      list_attempts[1] + "\nAttempt Three: " + list_attempts[2] + "\n[Correct Answer: def __init__(self)]"

# Now that's all the questions, finally, for the final print statements:
# This prints the end of the exam
print("\nYou have finished the examination, well done!")

# This prints out the user score out of 32.
print("\nYour exam score was " + str(count) + "/" + str(32))

# This prints out what question the users got wrong, their responses, and what was the actual correct answer
print("\n" + correct_answer)

# Finally, this prints out the user's finished exam time. (The current time)
print("\nFinished exam time: " + str(datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")))

