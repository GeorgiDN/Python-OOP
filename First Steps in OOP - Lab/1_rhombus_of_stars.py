def draw_rhombus(n):
    for i in range(n):
        offset = (n - i - 1) * ' '
        content = ('* ' * (i + 1))
        print(f'{offset}{content}')

    for i in range(n - 2, - 1, -1):
        offset = (n - i - 1) * ' '
        content = ('* ' * (i + 1))
        print(f'{offset}{content}')


rows = int(input())
draw_rhombus(rows)



# n = int(input())
# for i in range(n):
#     print(" " * (n-i-1) + "* " * (i+1))
# for i in range(n-2, -1, -1):
#     print(" " * (n-i-1) + "* " * (i+1))
