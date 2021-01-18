import datetime


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
            question_two = int(input("2.\tHow many gigabytes are in a terabyte? (Input your answer in the form of a "
                                     "number): \n"))
            break
        except ValueError:
            print("Please input your answer in the form of a number")
    if question_two == 1024:
        count += 1
    else:
        correct_answer += "2.\tYour Answer: " + str(question_two) + "\t[Correct Answer: 1024]\n"

    while True:
        try:
            question_three = int(input("How many bytes does 16 bits equal? (Input your answer in the form of a "
                                       "number): \n"))
            break
        except ValueError:
            print("Please input your answer in the form of a number")
    if question_three == 2:
        count += 1
    else:
        correct_answer += "3.\tYour Answer: " + str(question_three) + "\t[Correct Answer: 2]\n"

    question_four = input("4.\tWhat does Megahertz(MHz) & Gigahertz (GHz) measure?: \n")
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

    question_six = input("6.\tDPI measures how many points of information can be captured in a ___: \n")
    if question_six.strip().lower() == "inch":
        count += 1
    else:
        correct_answer += "6.\tYour Answer: " + question_six + "\t[Correct Answer: inch]\n"

    while True:
        print(
            "\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]\n")
        print("7.\tDPI is NOT used for:\nA. Mouse\tB. Printer\t C. Cameras")
        question_seven = input()
        if question_seven.strip().lower() == "c":
            count += 1
            break
        elif question_seven.strip().lower() == "a" or question_seven.strip().lower() == "b":
            correct_answer += "7.\tYour Answer: " + question_seven + " \t[Correct Answer: C]\n"
            break
        elif question_seven.strip().lower() != "a" or question_seven.strip().lower() != "b":
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("8.\tPPI is used for:\nA. Smartphone Screens  \tB. TV Screen\tC. Keyboard")
        question_eight = input()
        if question_eight.strip().lower() == "a":
            count += 1
            break
        elif question_eight.strip().lower() == "b" or question_eight.strip().lower() == "c":
            correct_answer += "8.\tYour Answer: " + question_eight + "\t[Correct Answer: A]\n"
            break
        elif question_eight.strip().lower() != "b" or question_eight.strip().lower() != "c":
            print("Please enter a correct option (A, B, or C)")

    print("\nComputer Components and Malware\n-------------------------------")
    print("[Knowledge Questions]\n")
    question_nine = input("9.\tWhat component serves as a connection between the various different parts of a computer "
                          "system?: \n")
    if question_nine.strip().lower() == "motherboard":
        count += 1
    else:
        correct_answer += "9.\tYour Answer: " + question_nine + "\t[Correct Answer: motherboard]\n"

    question_ten = input("10.\tWhat does \"CPU\" stand for?: \n")
    if question_ten.strip().lower() == "central processing unit":
        count += 1
    else:
        correct_answer += "10.\tYour Answer: " + question_ten + "\t[Correct Answer: central processing unit]\n"

    question_eleven = input("11.\tWhat type of memory is the slowest in the memory hierarchy?: \n")
    if question_eleven.strip().lower() == "storage":
        count += 1
    else:
        correct_answer += "11.\tYour Answer: " + question_eleven + "\t[Correct Answer: storage]\n"

    while True:
        try:
            question_twelve = int(input("12.\tFor a 3 GHz dual core processor, what is the clock speed of a single core? ("
                                        "Input your answer in the form of a number): \n"))
            break
        except ValueError:
            print("Input your answer in the form of a number")
    if question_twelve == 3:
        count += 1
    else:
        correct_answer += "12.\tYour Answer: " + str(question_twelve) + "\t[Correct Answer: 3]\n"

    print("\n[Fill in the blanks]\n")
    question_thirteen = input("13.\tDual cord is two ____ on the same chip: \n")
    if question_thirteen.strip().lower() == "processors" or question_thirteen.strip().lower() == "processor":
        count += 1
    else:
        correct_answer += "13.\tYour Answer: " + question_thirteen + "\t[Correct Answer: processor]\n"

    question_fourteen = input("14.\tThe information processing cycle is as follows: Input, Processing, ______, Storage: \n")
    if question_fourteen.strip().lower() == "output":
        count += 1
    else:
        correct_answer += "14.\tYour Answer: " + question_fourteen + "\t[Correct Answer: output]\n"

    question_fifteen = input("15.\tThe processing chip, ___, serves as the brains of the computer: \n")
    if question_fifteen.strip().lower() == "cpu":
        count += 1
    else:
        correct_answer += "15.\tYour Answer: " + question_fifteen + "\t[Correct Answer: CPU]\n"

    while True:
        print(
            "\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]\n")
        print("This type of software or malware is installed on a computing device without the user's knowledge")
        print("16.\tBased on the description, what type of computer virus is this?:\nA. Spyware\t B. Trojan\t C. Adware")
        question_sixteen = input()
        if question_sixteen.strip().lower() == "a":
            count += 1
            break
        elif question_sixteen.strip().lower() == "b" or question_sixteen.strip().lower() == "c":
            correct_answer += "16.\tYour Answer: " + question_sixteen + "\t[Correct Answer: A]\n"
            break
        elif question_sixteen.strip().lower() != "a" or question_sixteen.strip().lower() != "b":
            print("Please enter a correct option (A, B, or C)")

    while True:
        print(
            "\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]")
        print("This is a program that replicates itself and destroys data and files on the computer")
        print("17.\tBased on the description, what type of computer virus is this?:\nA. Rootkit\tB. Worm\t C. Rogue "
              "Security Software")
        question_seventeen = input()
        if question_seventeen.strip().lower() == "b":
            count += 1
            break
        elif question_seventeen.strip().lower() == "a" or question_seventeen.strip().lower() == "c":
            correct_answer += "17.\tYour Answer: " + question_seventeen + "\t[Correct Answer: B]\n"
            break
        elif question_seventeen.strip().lower() != "a" or question_seventeen.strip().lower() != "c":
            print("Please enter a correct option (A, B, or C)")

    while True:
        print(
            "\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]")
        print("This malware records what you type on your pc, tracking your login-name, password and any forms of "
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
        elif question_eighteen.strip().lower() != "a" or question_eighteen.strip().lower() != "c":
            print("Please enter a correct option (A, B, or C)")

    print("\nYour exam score was " + str(count) + "/" + str(18))
    print(correct_answer)
    print("Finished exam time: " + str(datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")))
