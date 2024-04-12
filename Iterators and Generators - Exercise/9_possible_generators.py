
from itertools import permutations


def possible_permutations(numbers):
    result = permutations(numbers)

    for permutation in result:
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
# [print(n) for n in possible_permutations([1])]




