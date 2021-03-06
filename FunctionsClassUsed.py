import datetime


# This function converts milliseconds (which is the base time used for measuring how long a program takes to run)
# into minutes and seconds, it also formats the time into a timer. (Ex: %02dm:%02ds) It does this by constantly dividing
# the milliseconds.
def timeconverter(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    print("Time taken on exam: %02dm:%02ds" % (minutes, seconds))


# This functions asks all the questions, as well as gathers the user's answers. It will also display their final score
# and the questions they got wrong.
def questions():
    count = 0
    correct_answer = "Questions You Got Wrong: \n"

    print("\nComputer Unit Measurements\n--------------------------")
    print("[Knowledge Questions]\n")
    question_one = input("1.\tType the LETTER symbol for the computer unit, \"Bit\": \n")
    if question_one.strip() == "b":
        count += 1
    else:
        correct_answer += "1.\tYour Answer: " + question_one + "\t[Correct Answer: b]\n"

    while True:
        try:
            question_two = int(input("\n2.\tHow many gigabytes are in a terabyte? (Input your answer in the form of a "
                                     "number): \n"))
            break
        except ValueError:
            print("Please input your answer in the form of a number!")
    if question_two == 1024:
        count += 1
    else:
        correct_answer += "2.\tYour Answer: " + str(question_two) + "\t[Correct Answer: 1024]\n"

    while True:
        try:
            question_three = int(input("\n3.\tHow many bytes does 16 bits equal? (Input your answer in the form of a "
                                       "number): \n"))
            break
        except ValueError:
            print("Please input your answer in the form of a number!")
    if question_three == 2:
        count += 1
    else:
        correct_answer += "3.\tYour Answer: " + str(question_three) + "\t[Correct Answer: 2]\n"

    question_four = input("\n4.\tWhat does Megahertz (MHz) & Gigahertz (GHz) measure?: \n")
    if question_four.strip().lower() == "processing speed":
        count += 1
    else:
        correct_answer += "4.\tYour Answer: " + question_four + "\t[Correct Answer: processing speed]\n"

    print("\n[Fill in the blanks]\n")
    question_five = input("5.\tMB/s, MBps, GB/s GBps) measures how much data can be ____: \n")
    if question_five.strip().lower() == "transferred":
        count += 1
    else:
        correct_answer += "5.\tYour Answer: " + question_five + "\t[Correct Answer: transferred]\n"

    question_six = input("\n6.\tDPI measures how many points of information can be captured in a ___: \n")
    if question_six.strip().lower() == "inch":
        count += 1
    else:
        correct_answer += "6.\tYour Answer: " + question_six + "\t[Correct Answer: inch]\n"

    print("\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]\n")
    while True:
        print("7.\tDPI is NOT used for:\nA. Mouse\tB. Printer\t C. Cameras")
        question_seven = input()
        if question_seven.strip().lower() == "c":
            count += 1
            break
        elif question_seven.strip().lower() == "a" or question_seven.strip().lower() == "b":
            correct_answer += "7.\tYour Answer: " + question_seven + " \t[Correct Answer: C]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("\n8.\tPPI is used for:\nA. Smartphone Screens  \tB. TV Screen\tC. Keyboard")
        question_eight = input()
        if question_eight.strip().lower() == "a":
            count += 1
            break
        elif question_eight.strip().lower() == "b" or question_eight.strip().lower() == "c":
            correct_answer += "8.\tYour Answer: " + question_eight + "\t[Correct Answer: A]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

    print("\nComputer Components and Malware\n-------------------------------")
    print("[Knowledge Questions]\n")
    question_nine = input("9.\tWhat component serves as a connection between the various different parts of a computer "
                          "system?: \n")
    if question_nine.strip().lower() == "motherboard":
        count += 1
    else:
        correct_answer += "9.\tYour Answer: " + question_nine + "\t[Correct Answer: motherboard]\n"

    question_ten = input("\n10.\tWhat does \"CPU\" stand for?: \n")
    if question_ten.strip().lower() == "central processing unit":
        count += 1
    else:
        correct_answer += "10.\tYour Answer: " + question_ten + "\t[Correct Answer: central processing unit]\n"

    question_eleven = input("\n11.\tWhat type of memory is the slowest in the memory hierarchy?: \n")
    if question_eleven.strip().lower() == "storage":
        count += 1
    else:
        correct_answer += "11.\tYour Answer: " + question_eleven + "\t[Correct Answer: storage]\n"

    while True:
        try:
            question_twelve = int(
                input("\n12.\tFor a 3 GHz dual core processor, what is the clock speed of a single core? ("
                      "Input your answer in the form of a number): \n"))
            break
        except ValueError:
            print("Input your answer in the form of a number!")
    if question_twelve == 3:
        count += 1
    else:
        correct_answer += "12.\tYour Answer: " + str(question_twelve) + "\t[Correct Answer: 3]\n"

    print("\n[Fill in the blanks]\n")
    question_thirteen = input("13.\tDual cord is two ____ on the same chip: \n")
    if question_thirteen.strip().lower() == "processors" or question_thirteen.strip().lower() == "processor":
        count += 1
    else:
        correct_answer += "13.\tYour Answer: " + question_thirteen + "\t[Correct Answer: processor or processors]\n"

    question_fourteen = input("\n14.\tThe information processing cycle is as follows: Input, Processing, ______, "
                              "Storage: \n")
    if question_fourteen.strip().lower() == "output":
        count += 1
    else:
        correct_answer += "14.\tYour Answer: " + question_fourteen + "\t[Correct Answer: output]\n"

    question_fifteen = input("\n15.\tThe processing chip, ___, serves as the brains of the computer: \n")
    if question_fifteen.strip().lower() == "cpu":
        count += 1
    else:
        correct_answer += "15.\tYour Answer: " + question_fifteen + "\t[Correct Answer: CPU]\n"

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

    while True:
        print("\nThis is a program that replicates itself and destroys data and files on the computer")
        print("17.\tBased on the description, what type of computer virus is this?:\nA. Rootkit\tB. Worm\t C. Rogue "
              "Security Software")
        question_seventeen = input()
        if question_seventeen.strip().lower() == "b":
            count += 1
            break
        elif question_seventeen.strip().lower() == "a" or question_seventeen.strip().lower() == "c":
            correct_answer += "17.\tYour Answer: " + question_seventeen + "\t[Correct Answer: B]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("\nThis malware records what you type on your pc, tracking your login-name, password and any forms of "
              "sensitive information.")
        print("18.\tBased on the description, what type of computer virus is this?:\nA. Ransomware\tB. Keylogger\t"
              "C. Browser Hijacker")
        question_eighteen = input()
        if question_eighteen.strip().lower() == "b":
            count += 1
            break
        elif question_eighteen.strip().lower() == "a" or question_eighteen.strip().lower() == "c":
            correct_answer += "18.\tYour Answer: " + question_seventeen + "\t[Correct Answer: B]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("\nJim is buying computer parts and he wants to know what he might needs, here is the list of items he "
              "has below:")
        print("1.\tCPU")
        print("2.\tMemory")
        print("3.\tGPU)")
        print("4.\tHard Drive")
        print("5.\tPower Supply/Battery")
        print("\n19.\tBased on the list above, does he have all the components needed to build a computer?:\nA. "
              "Yes\tB. No")
        question_nineteen = input()
        if question_nineteen.strip().lower() == "b":
            count += 1
            break
        elif question_nineteen.strip().lower() == "a":
            correct_answer += "19.\tYour Answer: " + question_nineteen + "\t[Correct Answer: B]\n"
            break
        else:
            print("Please enter a correct option (A or B)")

    print("\nPython Basics\n-------------")
    print("[Knowledge Questions]\n")

    question_twenty = input("20.\tWhat do you write to convert a user input into a \"decimal only\" variable? (Ex: "
                            "int, etc.): \n")
    if question_twenty.strip().lower() == "float" or question_twenty.strip().lower() == "float()":
        count += 1
    else:
        correct_answer += "20.\tYour Answer: " + question_twenty + "\t[Correct Answer: float or float()]\n"

    print("\nname = not True")
    print("for x in range(3):")
    print("\tname = True")
    question_twentyone = input("21.\tBased on the program above, what boolean value is the variable, \"name\"?: \n")
    if question_twentyone.strip().lower() == "true":
        count += 1
    else:
        correct_answer += "21.\tYour Answer: " + question_twentyone + "\t[Correct Answer: True]\n"

    print("\ns = \"I love Python programming\"")
    print("print(s[2:5] + s[22:]")
    question_twentytwo = input("22.\tBased on the program above, what is the output?: \n")
    if question_twentytwo.strip() == "loving":
        count += 1
    else:
        correct_answer += "22.\tYour Answer: " + question_twentytwo + "\t[Correct Answer: loving]\n"

    print("\nprint(9 * 5 // 9 + 3 * 2)")
    while True:
        try:
            question_twentythree = int(input("23.\tWhat is the output of the program above? (Input your answer in the "
                                             "form of a number): \n"))
            break

        except ValueError:
            print("Please input your answer in the form of a number!")

    if question_twentythree == 11:
        count += 1
    else:
        correct_answer += "23.\tYour Answer: " + str(question_twentythree) + "\t[Correct Answer: 11]\n"

    question_twentyfour = input("\n24.\tWhat needs to be added infront of a integer value/variable to print it?: \n")
    if question_twentyfour.strip().lower() == "str" or question_twentyfour.strip().lower() == "str()":
        count += 1
    else:
        correct_answer += "24.\tYour Answer: " + question_twentyfour + "\t[Correct Answer: str or str()]\n"

    print("\n[Fill in the blanks]\n")
    print("Add a variable that will make the following statement correct:")
    question_twentyfive = input("25.\t2 __ 3 = 8: \n")
    if question_twentyfive.strip().lower() == "**":
        count += 1
    else:
        correct_answer += "25.\tYour Answer: " + question_twentyfive + "\t[Correct Answer: **]\n"

    print("\nAdd a variable that will make the following statement correct:")
    question_twentysix = input("26.\t2 _ 3 = 2: \n")
    if question_twentysix.strip().lower() == "%":
        count += 1
    else:
        correct_answer += "26.\tYour Answer: " + question_twentysix + "\t[Correct Answer: %]\n"

    print("\nAdd a sign to allow the statement to run:")
    question_twentyseven = input("27.\tFor i in range(3)_\n\tprint(i) \n")
    if question_twentyseven.strip().lower() == ":":
        count += 1
    else:
        correct_answer += "27.\tYour Answer: " + question_twentyseven + "\t[Correct Answer: \":\"]\n"

    print("\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]\n")
    while True:
        print("What is the difference between // and %?:")
        print("28.\tA. There is no difference\n\tB. % will return the remainder after dividing two values while // "
              "does integer division (ignoring remainder)\n\tC. % will find the GCF of two variable while // will find "
              "the LCM")
        question_twentyeight = input()
        if question_twentyeight.strip().lower() == "b":
            count += 1
            break
        elif question_twentyeight.strip().lower() == "a" or question_twentyeight.strip().lower() == "c":
            correct_answer += "28.\tYour Answer: " + question_twentyeight + "\t[Correct Answer: B]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("\nWhat is wrong with the following program?:")
        print("Two number = int(input())")
        print("Text = input()")
        print("print(str(two number) * text)")
        print("29.\tA. There is nothing wrong\tB. Line 1\tC. Line 3")
        question_twentynine = input()
        if question_twentynine.strip().lower() == "b":
            count += 1
            break
        elif question_twentynine.strip().lower() == "a" or question_twentynine.strip().lower() == "c":
            correct_answer += "29.\tYour Answer: " + question_twentynine + "\t[Correct Answer: B]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("\nWhat's the difference between (i += 1) and (i = i + 1)")
        print(
            "30.\tA. There is no difference\tB. += makes i the sum of i + i + 1\t C. += multiplies i with itself by one")
        question_thirty = input()
        if question_thirty.strip().lower() == "a":
            count += 1
            break
        elif question_thirty.strip().lower() == "b" or question_thirty.strip().lower() == "c":
            correct_answer += "30.\tYour Answer: " + question_thirty + "\t[Correct Answer: A]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("\nWhat's the output of this program?:")
        print("boolean_value = True\nif not boolean_value:\n\tprint(10)")
        print("31.\tA. The output would be nothing\tB. An error will pop up\t C. 10")
        question_thirtyone = input()
        if question_thirtyone.strip().lower() == "a":
            count += 1
            break
        elif question_thirtyone.strip().lower() == "b" or question_thirtyone.strip().lower() == "c":
            correct_answer += "31.\tYour Answer: " + question_thirtyone + "\t[Correct Answer: A]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("\nWhat's the output of this program?:")
        print("for x in 100:")
        print("\tprint(\"hot dogs\")")
        print("32.\tA. The output would be nothing\tB. An error will pop up\t C. It wil print hot dogs 100 times")
        question_thirtytwo = input()
        if question_thirtytwo.strip().lower() == "b":
            count += 1
            break
        elif question_thirtytwo.strip().lower() == "a" or question_thirtytwo.strip().lower() == "c":
            correct_answer += "32.\tYour Answer: " + question_thirtytwo + "\t[Correct Answer: B]\n"
            break
        else:
            print("Please enter a correct option (A, B, or C)")

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

    user_attempt_two = 0
    list_attempts_two = []
    print_boolean_two = True
    while user_attempt_two != 3:
        print("\ndef catalan(n):\n\tif n <= 1:\n\t\t\n\telse:\n\t\tr = 0\n\t\tfor i in range(n):\n\t\t\tr+= catalan("
              "i) * catalan(n-i-1)\n\t\treturn r\n\nprint(catalan(3))")
        question_thirtyfour = input("\n34.\tWhat is the output of the program above?: \n")
        user_attempt_two += 1
        if question_thirtyfour.strip().lower() == "5" and user_attempt_two == 1:
            count += 3
            print("Correct!")
            print_boolean_two = False
            break
        elif question_thirtyfour.strip().lower() == "5" and user_attempt_two == 2:
            count += 2
            print("Correct!")
            print_boolean_two = False
            break
        elif question_thirtyfour.strip().lower() == "5" and user_attempt_two == 3:
            count += 1
            print("Correct!")
            print_boolean_two = False
            break
        list_attempts_two.append(question_thirtyfour)
    if print_boolean_two:
        correct_answer += "\n34.\tYour Answers:\nAttempt One: " + list_attempts_two[0] + "\nAttempt Two: " + \
                          list_attempts_two[1] + "\nAttempt Three: " + list_attempts_two[2] + "\n[Correct Answer: 5]"

    print("\nYou have finished the examination, well done!")
    print("\nYour exam score was " + str(count) + "/" + str(32))
    print("\n" + correct_answer)
    print("\nFinished exam time: " + str(datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")))
