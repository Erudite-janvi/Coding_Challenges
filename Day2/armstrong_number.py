def is_armstrong_number(number):
    original_number = number
    num_digits = len(str(number))
    armstrong_sum = 0

    while number > 0:
        digit = number % 10
        armstrong_sum += digit ** num_digits
        number //= 10

    return armstrong_sum == original_number
number = 153
if is_armstrong_number(number):
    print(number,"is an Armstrong number.")
else:
    print(number,"is not an Armstrong number.")
