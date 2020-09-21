"""
Program: validation_with_try.py
Author: Shiqi Wang
Last date modified: 09/10/2020



The purpose of this program is to validate user's input with 'try' statement
"""


def average(score1, score2, score3):
    if score1 < 0:
        raise ValueError

    elif score2 < 0:
        raise ValueError

    elif score3 < 0:
        raise ValueError

    else:
        NUMBER_TESTS = 3
        return float((score1 + score2 + score3) / NUMBER_TESTS)


def main():
    score1 = float(input("Score1: "))
    score2 = float(input("Score2: "))
    score3 = float(input("Score3: "))
    try:
        average_score = average(score1, score2, score3)
    except ValueError:
        print("In your inputs, at least one of the scores is negative number. Please make all of them positive")
        return
    print(f"The average score is {average_score}")


if __name__ == '__main__':
    main()
