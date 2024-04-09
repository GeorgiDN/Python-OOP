def squares(end):
    n = 1

    while n <= end:
        yield n ** 2
        n += 1


print(list(squares(5)))


# 50/100 - judge

# class squares:
#     def __init__(self, end):
#         self.start = 0
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#
#         self.start += 1
#         return self.start ** 2
#
#
# print(list(squares(5)))


