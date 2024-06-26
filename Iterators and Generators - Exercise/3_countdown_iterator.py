class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            self.start = self.count
            self.count -= 1
            return self.start
        raise StopIteration()



# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")





# class countdown_iterator:
#     def __init__(self, count):
#         self.count = count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count < 0:
#             raise StopIteration()
#         number = self.count
#         self.count -= 1
#         return number
#
#
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")





# class countdown_iterator:
#     def __init__(self, count: int):
#         self.count = count
#         self.start = self.count + 1
#         self.end = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.end:
#             raise StopIteration
#
#         self.start -= 1
#
#         return self.start
#
#
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")
