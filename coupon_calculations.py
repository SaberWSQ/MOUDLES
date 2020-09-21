"""
Program: coupon_calculation.py
Author: Shiqi Wang
Last date modified: 09/10/2020



The purpose of this program is to be calculate the price after coupon
"""


def calculate_price(price, cash_coupon, percent_coupon):
    price_after_cash = max(0, price - cash_coupon)
    price_after_percent_coupon = price_after_cash * (1 - percent_coupon)
    tax = price_after_percent_coupon * 0.06

    shipping = 0.0
    if price_after_percent_coupon <= 50:
        if price_after_percent_coupon <= 10:
            shipping = 5.95
        elif price_after_percent_coupon <= 30:
            shipping = 7.95
        elif price_after_percent_coupon <= 50:
            shipping = 11.95

    final_price = price_after_percent_coupon + tax + shipping
    return final_price


def main():
    price = float(input("The original price: "))
    cash_coupon = float(input("The cash coupon: "))
    percent_coupon = float(input("The percent coupon: "))
    print(f"The final price is {calculate_price(price, cash_coupon, percent_coupon)}")


if __name__ == '__main__':
    main()


