def reverse_text(string):
    string_as_list = list(string)

    while string_as_list:
        yield string_as_list.pop()


for char in reverse_text("step"):
    print(char, end='')
