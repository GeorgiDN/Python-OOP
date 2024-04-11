class sequence_repeat:
    def __init__(self, sequence, num):
        self.sequence = sequence
        self.num = num
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            start_idx = self.idx
            self.idx += 1
            return self.sequence[start_idx % len(self.sequence)]
        raise StopIteration()



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')
