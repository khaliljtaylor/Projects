"""
Program Name: Purchase Cost Calculator
Author: Khalil Taylor
Date: December 15, 2025

Description:
This program calculates the total cost of a purchase based on user input.
The user enters the price per item and quantity purchased. The program then
calculates the subtotal, discount amount, tax amount, shipping cost,
and the final total amount paid.

Variables:
unit_price (float)   - Price of one item
quantity (int)       - Number of items purchased
subtotal (float)     - Total cost before discounts and taxes
discount_rate (float) - Discount percentage applied
discount_amount (float) - Amount discounted
tax_rate (float)     - Sales tax percentage
tax_amount (float)   - Amount of tax charged
shipping_cost (float) - Cost to ship the items
total_paid (float)   - Final amount paid by the customer

Program Flow:
1. Prompt user for unit price and quantity
2. Calculate subtotal
3. Determine discount rate based on subtotal
4. Calculate discount amount
5. Calculate tax amount
6. Calculate shipping cost
7. Calculate and display total amount paid
"""

# Constants
def main():
    TAX_RATE = 0.06          # 6% sales tax
    SHIPPING_PERCENTAGE = 0.02  # 2% shipping cost of total price   
    unit_price = float(input("Enter the price per item: $"))
    quantity = int(input("Enter the quantity purchased: "))
    subtotal = calc_subtotal(unit_price, quantity)
    discountAmount = calc_discount(subtotal)
    taxAmount = calc_Tax(subtotal, TAX_RATE, discountAmount)
    price = calc_price(subtotal, taxAmount, discountAmount)
    shippingcost = calc_shipping(subtotal, discountAmount, SHIPPING_PERCENTAGE)
    printresults(subtotal, discountAmount, taxAmount, shippingcost, price)

def enter_Data():
    unit_price = float(input("Enter the price per item: $"))
    quantity = int(input("Enter the quantity purchased: "))


# Calculate subtotal
def calc_subtotal(unit_price, quantity):
    subtotal = unit_price * quantity
    return subtotal;

# Determine discount rate
def calc_discount(subtotal):
    if subtotal >= 100:
        discount_rate = 0.05  # 5% discount
    else:
        discount_rate = 0.03  # 3% discount
    discount_amount = subtotal * discount_rate
    return discount_amount;

# Calculate tax amount
def calc_Tax(subtotal, TAX_RATE, discount_amount):
    tax_amount = (subtotal - discount_amount) * TAX_RATE
    return tax_amount;

# Calculate shipping cost
def calc_shipping(subtotal, discount_amount, SHIPPING_PERCENTAGE):
    shipping_cost = (subtotal - discount_amount) * SHIPPING_PERCENTAGE
    return shipping_cost;

# Calculate total amount paid
def calc_price(a1, a2, a3):
    a4 = a1 + a2 - a3
    return a4;

# Display results
def printresults(x1, x2, x3, x4, x5):
    print("\n----- Purchase Summary -----")
    print(f"Subtotal: ${x1:.2f}")
    print(f"Discount: -${x2:.2f}")
    print(f"Tax: ${x3:.2f}")
    print(f"Shipping Cost: ${x4:.2f}")
    print(f"Total Amount Paid: ${x5:.2f}")

main()
