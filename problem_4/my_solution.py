def digit_counter(num_to_check):
    counter = 0
    while num_to_check >= 1:
        num_to_check = num_to_check / 10
        counter += 1
    return counter


def is_palindrome(num_to_check):
    digits_num = digit_counter(num_to_check)
    if digits_num % 2 == 0:
        iterations = digits_num // 2
    else:
        iterations = (digits_num // 2) + 1
    for i in range(1, iterations + 1):
        first_digit = num_to_check // (10 ** (digits_num - i)) % 10
        last_digit = num_to_check % (10 ** i) // (10 ** (i - 1))
        if not first_digit == last_digit:
            return False
    return True


def largest_palindrome(num_of_digits):
    n = 0
    for first_number in range(999, 100, -1):
        for second_number in range(first_number, 100, -1):
            if is_palindrome(first_number * second_number) and first_number * second_number > n:
                n = first_number * second_number
                print(first_number, second_number)
    return n


print(largest_palindrome(3))


