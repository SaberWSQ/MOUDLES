"""
Program: unit_test.py
Author: Shiqi Wang
Last date modified: 09/02/2020



The purpose of this program is to be convert input years to months
"""


def convert_to_months(years):
    try:
        age_in_years = int(years)
    except ValueError:
        raise TypeError("Input number is not integer")

    if age_in_years < 1 or age_in_years > 5:
        raise ValueError("Input number is out of range, please input year between 1 and 5")

    age_in_months = int(years) * 12
    return age_in_months


def main():
    print('Enter your age: ')
    age_in_years = input()
    age_in_months = convert_to_months(age_in_years)
    print(f"{age_in_years} years is {age_in_months} months.")


if __name__ == '__main__':
    main()

"""
The input year should be range from 3 to 72,
if the input string cannot be converted into int, raise TypeError,
if the converted value is out of range, raise ValueError

The instruction is really confused, 
in the instruction, it says
'Call the function convert_to_months(age_in_months) and save the result in a variable age_in_years'
but convert_to_months should input age_in_years.
so I think it should input age_in_years, and the range from 1 to 5, instead of 3 to 72
"""