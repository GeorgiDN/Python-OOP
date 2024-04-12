from math import sqrt


def get_primes(all_numbers):
    for number in all_numbers:
        if number < 2:
            continue
        for idx in range(2, int(sqrt(number)) + 1):
            if number % idx == 0:
                break
        else:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
