def read_next(*args):
    for current_item in args:
        for element in current_item:
            yield element


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')




# def read_next(*args):
#     idx = 0
#
#     while idx < len(args):
#         for item in args[idx]:
#             yield item
#         idx += 1
