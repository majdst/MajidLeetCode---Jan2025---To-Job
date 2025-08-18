def greatest_product(num_string):

    max_product = 0
    max_digits = ''

    for i in range(len(num_string) - 4):

        window = num_string[i: i+5]

        product = 1

        for char in window:
            product *= int(char)

        if product > max_product:

            max_product = product
            max_digits = window
    return max_product, max_digits

def main():

    while True:
        number = input('Enter a number')

        while len(number) < 5 or not number.isdigit():

            number = input('Invalid input, Re-enter: ')
        
        result, digits = greatest_product(number)
        print(f"Highest product: {result}")
        print(f"Digits used: {digits}")

        stop = input('Do you wanna stop(Y/N): ').upper()

        if stop == 'Y':
            break

main()