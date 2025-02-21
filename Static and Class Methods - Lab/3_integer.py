from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) != float:
            return "value is not a float"

        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, roman_number):
        roman_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
                          }
        int_value = 0
        for i in range(len(roman_number)):
            if roman_number[i] in roman_numerals:
                if i + 1 < len(roman_number) and roman_numerals[roman_number[i]] < roman_numerals[roman_number[i + 1]]:
                    int_value -= roman_numerals[roman_number[i]]
                else:
                    int_value += roman_numerals[roman_number[i]]

        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))



###################################################################
# DO NOT PASS IN JUDGE
# from math import floor
#
# import roman
#
#
# class Integer:
#     def __init__(self, value: int):
#         self.value = value
#
#     @classmethod
#     def from_float(cls, float_value):
#         if type(float_value) != float:
#             return "value is not a float"
#
#         return cls(floor(float_value))
#
#     @classmethod
#     def from_roman(cls, roman_number):
#         return cls(roman.fromRoman(roman_number))
#
#     @classmethod
#     def from_string(cls, value):
#         if not isinstance(value, str):
#             return "wrong type"
#         try:
#             return cls(int(value))
#         except ValueError:
#             return "wrong type"


################################################################
# import math
#
#
# class Integer:
#     def __init__(self, value: int):
#         self.value = value
#
#     @classmethod
#     def from_float(cls, float_value):
#         if type(float_value) != float:
#             return "value is not a float"
#
#         return cls(math.floor(float_value))
#
#     @classmethod
#     def from_roman(cls, value):
#         """
#               :type value: str
#               :rtype: int
#               """
#         roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
#                  'CD': 400, 'CM': 900}
#         i = 0
#         num = 0
#         while i < len(value):
#             if i + 1 < len(value) and value[i:i + 2] in roman:
#                 num += roman[value[i:i + 2]]
#                 i += 2
#             else:
#                 # print(i)
#                 num += roman[value[i]]
#                 i += 1
#         return cls(num)
#
#
#     @classmethod
#     def from_string(cls, value):
#         if type(value) != str:
#             return "wrong type"
#         return cls(int(value))
