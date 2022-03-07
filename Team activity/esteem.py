from netrc import NetrcParseError
from tkinter import NE


Negative = -1
Positive = 1
def main():
    intro()
    question()

def intro():
    print("This program is an implementation of the Rosenberg \nSelf-Esteem Scale. This program will show you ten \nstatements that you could possibly apply to yourself. \nPlease rate how much you agree with each of the \nstatements by responding with one of these four letters:\n")
    print("D means you strongly disagree with the statement. \nd means you disagree with the statement. \na means you agree with the statement. \nA means you strongly agree with the statement.")

def question():
    score = 0
    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    score += answer(Positive)

    print("2. I feel that I have a number of good qualities.")
    score += answer(Positive)

    print("3. All in all, I am inclined to feel that I am a failure.")
    score += answer(Negative)

    print("4. I am able to do things as well as most other people.")
    score += answer(Positive)

    print("5. I feel I do not have much to be proud of.")
    score += answer(Negative)

    print("6. I take a positive attitude toward myself.")
    score += answer(Positive)

    print("7. On the whole, I am satisfied with myself.")
    score += answer(Positive)

    print("8. I wish I could have more respect for myself.")
    score += answer(Negative)

    print("9. I certainly feel useless at times.")
    score += answer(Negative)

    print("10. At times I think I am no good at all.")
    score += answer(Negative)
    print(f"\nYour score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")
 
def answer(pos_neg):
    response = input("Enter D, d, a, or A: ")
    if response == "D":
        score = 0
    elif response == "d":
        score = 1
    elif response == "a":
        score = 2
    elif response == "A":
        score = 3
    else:
        print("enter valid input")
        response = input("Enter D, d, a, or A: ")
    if pos_neg == Negative:
        score = 3 - score
    return score

main()
