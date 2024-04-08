class reverse_iter:
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable_object:
            raise StopIteration
        return self.iterable_object.pop()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
