count = 0
correct_answer = ""
while True:
    print("Jim is buying computer parts and he wants to know what he might needs, here is the list of items he "
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

print(count)
print(correct_answer)