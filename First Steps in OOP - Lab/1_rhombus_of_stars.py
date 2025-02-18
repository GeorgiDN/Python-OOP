n = int(input())

for i in range(n):
    print(' ' * (n - 1 - i) + '* ' * (i + 1))

for i in range(n - 2, -1, -1):
    print(' ' * (n - 1 - i) + '* ' * (i + 1))


################################################################################################################################################################
# def draw_rhombus(n):
#     for i in range(n):
#         offset = (n - i - 1) * ' '
#         content = ('* ' * (i + 1))
#         print(f'{offset}{content}')
#
#     for i in range(n - 2, - 1, -1):
#         offset = (n - i - 1) * ' '
#         content = ('* ' * (i + 1))
#         print(f'{offset}{content}')
#
#
# rows = int(input())
# draw_rhombus(rows)


################################################################################################################################################################
# def generate_line(count, symbol, offset_count=0):
#     offset = offset_count * ' '
#     content = (f'{symbol} ' * count).strip()
#     return f"{offset}{content}"
#
#
# def draw_line(count, symbol, offset_count=0):
#     print(generate_line(count, symbol, offset_count))
#
#
# def draw_rhombus(n):
#     for i in range(n):
#         draw_line(i + 1, '*', n - i - 1)
#
#     for i in range(n - 2, - 1, -1):
#         draw_line(i + 1, '*', n - i - 1)
#
#
# draw_rhombus(int(input()))

################################################################################################################################################################
"""3

  *    n = 3, i = 0, stars = 1
 * *   n = 3, i = 1, stars = 2
* * *  n = 3, i = 2, stars = 3
 * *
  *
  
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
"""



####################################################################################################################################################################################
# class InputData:
#     def __init__(self) -> None:
#         self.n: int = int(input())
#
#
# class PrintRow:
#     def print_row(self, size: int, row: int) -> None:
#         empty: str = " "
#         star: str = "* "
#         print(f"{empty * (size - row)}{star * row}")
#
#
# class RhombusPrinter:
#     def __init__(self, size: int) -> None:
#         self.size: int = size
#         self.print_row_obj: PrintRow = PrintRow()
#
#     def print_rhombus(self) -> None:
#         self._print_upper_part()
#         self._print_center_part()
#         self._print_bottom_part()
#
#     def _print_upper_part(self) -> None:
#         for row in range(1, self.size):
#             self.print_row_obj.print_row(self.size, row)
#
#     def _print_center_part(self) -> None:
#         self.print_row_obj.print_row(self.size, self.size)
#
#     def _print_bottom_part(self) -> None:
#         for row in range(self.size - 1, 0, -1):
#             self.print_row_obj.print_row(self.size, row)
#
#
# input_data: InputData = InputData()
# rhombus_printer: RhombusPrinter = RhombusPrinter(input_data.n)
# rhombus_printer.print_rhombus()
