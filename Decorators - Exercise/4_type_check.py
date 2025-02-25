def type_check(_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], _type):
                return 'Bad Type'
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))




# def type_check(type_):
#     def decorator(func):
#         def wrapper(*args):
#             for el in args:
#                 if not isinstance(el, type_):
#                     return "Bad Type"
#             return func(*args)
#         return wrapper
#     return decorator


# @type_check(int)
# def times2(num):
#     return num*2


# print(times2(2))
# print(times2('Not A Number'))
