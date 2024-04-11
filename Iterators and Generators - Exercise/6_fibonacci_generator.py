def fibonacci():
    start_number, next_number = 0, 1
    while 1:
        yield start_number
        start_number, next_number = next_number, start_number + next_number


generator = fibonacci()
for i in range(5):
    print(next(generator))

