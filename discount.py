
def calculate_discount(price, discount_percent):
    final_price = 0
    if discount_percent >= 20:
        final_price = (80 * price) / 100
    else:
        final_price = price
    return final_price


price = int(input('Enter the price of the item: '))
discount_percent = int(input('Enter the percentage of the discount: '))

final_price = calculate_discount(price, discount_percent)
print(f'The final price is (after discount if applicable) = ${final_price}')