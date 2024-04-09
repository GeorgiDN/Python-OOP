def genrange(start, end):

    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 10)))


# With class for exmaple
# class genrange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end:
#             raise StopIteration
#
#         result = self.start
#         self.start += 1
#         return result
#
#
# print(list(genrange(1, 10)))

