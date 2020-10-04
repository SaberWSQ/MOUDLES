"""
Program: validate_input_in_functions.py
Author: Shiqi Wang
Last date modified: 10/01/2020


The purpose of this program is to write a function to get a valid test score from user prompt
"""


def score_input(test_name, test_score='0', invalid_message='Invalid test score, try again'):
    """Validate the test_score, return correct information or invalid message

    :param str test_name: user name
    :param str test_score: user test score
    :param str invalid_message: if the input test score is invalid, display this message
    :return: str, either correct information or invalid message
    """

    try:
        test_score = float(test_score)
    except ValueError as err:
        raise ValueError('Input score is not a number. Try again')

    if test_score < 0 or test_score > 100:
        return invalid_message

    return f"Test name: {test_name}\nTest score: {test_score}"
    # return { test_name: test_score}


def main():
    name = "Shiqi Wang"
    invalid_message = 'Invalid test score, try again'
    while True:
        test_score = input("Please input your score: ")
        try:
            res = score_input(name, test_score)
        except ValueError as err:
            print(str(err))
        else:
            print(res)
            if res != invalid_message:
                break


if __name__ == '__main__':
    main()
