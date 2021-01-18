import datetime

def questions():
    count = 0

    print("\nComputer Unit Measurements\n--------------------------")
    print("[Knowledge Questions]\n")
    question_one = input("1.\tType the LETTER symbol for the computer unit, \"Bit\": \n")
    if question_one.strip() == "b":
        count += 1

    while True:
        try:
            question_two = int(input("2.\tHow many gigabytes are in a terabyte? (Input your answer in the form of a "
                                     "number): \n"))
            break
        except ValueError:
            print("Please input your answer in the form of a number")
    if question_two == 1024:
        count += 1

    while True:
        try:
            question_three = int(input("How many bytes does 16 bits equal? (Input your answer in the form of a "
                                       "number): \n"))
            break
        except ValueError:
            print("Please input your answer in the form of a number")
    if question_three == 2:
        count += 1

    question_four = input("4.\tWhat does Megahertz(MHz) & Gigahertz (GHz) measure?: \n")
    if question_four.strip().lower() == "processing speed":
        count += 1

    print("\n[Fill in the blanks]")
    question_five = input("5.\tMB/s, MBps, GB/s GBps) measures how much data can be ____: \n")
    if question_five.strip().lower() == "transferred":
        count += 1

    question_six = input("6.\tDPI measures how many points of information can be captured in a ___: \n")
    if question_six.strip().lower() == "inch":
        count += 1

    while True:
        print(
            "\n[Multiple Choice Questions, write the existing LETTER corresponding to the answer (Ex: A, B, C, etc.)]")
        print("7.\tDPI is NOT used for:\nA. Mouse\tB. Printer\t C. Cameras")
        question_seven = input()
        if question_seven.strip().lower() == "c":
            count += 1
            break
        elif question_seven.strip().lower() == "a" or question_seven.strip().lower() == "b":
            break
        elif question_seven.strip().lower() != "a" or question_seven.strip().lower() != "b":
            print("Please enter a correct option (A, B, or C)")

    while True:
        print("8.\tPPI is used for:\nA. Smartphone Screens \tB. TV Screen\tC. Keyboard")
        question_eight = input()
        if question_eight.strip().lower() == "a":
            count += 1
            break
        elif question_eight.strip().lower() == "b" or question_eight.strip().lower() == "c":
            break
        elif question_eight.strip().lower() != "b" or question_eight.strip().lower() != "c":
            print("Please enter a correct option (A, B, or C)")

    print("\nComputer Components and Malware\n-------------------------------")
    print("[Knowledge Questions]\n")
    question_nine = input("What component serves as a connection between the various different parts of a computer "
                          "system?: \n")
    if question_nine.strip().lower() == "motherboard":
        count += 1

    question_ten = input("What does \"CPU\" stand for?: \n")
    if question_ten.strip().lower() == "central processing unit":
        count += 1

    question_eleven = input("What type of memory is the slowest in the memory hierarchy?: \n")
    if question_eleven.strip().lower() == "storage":
        count += 1

    while True:
        try:
            question_twelve = int(input("For a 3 GHz dual core processor, what is the clock speed of a single core? (Input your "
              "answer in the form of a number): \n"))
            break
        except ValueError:
            print("Input your answer in the form of a number")
    if question_twelve == 3:
        count += 1

    print("\n[Fill in the blanks]")
    
    print("\nYour exam score was " + str(count) + "/" + str(7))
    print("Finished exam time: " + str(datetime.datetime.now()))
