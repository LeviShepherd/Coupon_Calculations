"""
Program: coupon_calculations.py
Author: Levi Shepherd
Last date modified: 9/21/2020

The purpose of this program is to  take input for amount of purchase,
cash coupon amount, and percent coupon, then calculate and display the
total order amount.
"""


# Calculate the total amount due based on user input for price, cash coupon and percent coupons
def calculate_price(price, cash_coupon, percent_coupon):
    TAX_RATE = 1.06
    SHIP_10 = 5.95
    SHIP_30 = 7.95
    SHIP_50 = 11.95
    CASH_5 = 5
    CASH_10 = 10
    PERCENT_10 = .90
    PERCENT_15 = .85
    PERCENT_20 = .80
    subtotal = 0

    # Factoring in coupons, cash discounts and tax
    # Determine subtotal with all instances of no cash discount
    if cash_coupon == 0:
        if percent_coupon == 0:
            subtotal = (price * TAX_RATE)
        elif percent_coupon == 10:
            subtotal = (price * PERCENT_10) * TAX_RATE
        elif percent_coupon == 15:
            subtotal = (price * PERCENT_15) * TAX_RATE
        else:
            subtotal = (price * PERCENT_20) * TAX_RATE
    # Determine subtotal with all instances of a 5 dollar cash discount
    elif cash_coupon == 5:
        if percent_coupon == 0:
            subtotal = (price - CASH_5) * TAX_RATE
        elif percent_coupon == 10:
            subtotal = ((price - CASH_5) * PERCENT_10) * TAX_RATE
        elif percent_coupon == 15:
            subtotal = ((price - CASH_5) * PERCENT_15) * TAX_RATE
        else:
            subtotal = ((price - CASH_5) * PERCENT_20) * TAX_RATE
    # Determine subtotal with all instances of a 10 dollar cash discount
    else:
        if percent_coupon == 0:
            subtotal = (price - CASH_10) * TAX_RATE
        elif percent_coupon == 10:
            subtotal = ((price - CASH_10) * PERCENT_10) * TAX_RATE
        elif percent_coupon == 15:
            subtotal = ((price - CASH_10) * PERCENT_15) * TAX_RATE
        else:
            subtotal = ((price - CASH_10) * PERCENT_20) * TAX_RATE

    # Determine total
    if subtotal <= 10:
        total = subtotal + SHIP_10

    return total


if __name__ == '__main__':
    pass
