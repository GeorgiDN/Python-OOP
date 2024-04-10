class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = list(self.dictionary)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.dictionary):
            raise StopIteration()
        key = self.keys[self.idx]
        value = self.dictionary[key]
        self.idx += 1

        return key, value
#
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
#

# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)




# class dictionary_iter:
#     def __init__(self, dict):
#         self.dict = dict
#         self.items = list(dict.items())
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if not self.items:
#             raise StopIteration()
#
#         key_value = self.items.pop(0)
#         return key_value
#
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
