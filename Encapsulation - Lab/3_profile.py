import re


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) not in range(5, 16):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        password_length = self._check_length(value)
        digits = self._check_for_digits(value)
        upper_case_letter = self._check_for_upper_letters(value)

        if password_length and digits and upper_case_letter:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

    #Helper methods
    def _check_length(self, psword):
        len_pattern = r'(.{8,})'
        match = re.findall(len_pattern, psword)
        if match:
            return True
        return False

    def _check_for_digits(self, psword):
        digit_pattern = r"\d"
        match = re.findall(digit_pattern, psword)
        if match:
            return True
        return False

    def _check_for_upper_letters(self, psword):
        upper_case_pattern = r"[A-Z]"
        match = re.findall(upper_case_pattern, psword)
        if match:
            return True
        return False


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)





# class Profile:
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, value):
#         if 5 <= len(value) <= 15:
#             self.__username = value
#             return
#         raise ValueError("The username must be between 5 and 15 characters.")
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         match_uppercase = any(x.isupper() for x in value)
#         match_digits = any(y.isdigit() for y in value)
#
#         if len(value) >= 8 and match_uppercase and match_digits:
#             self.__password = value
#             return
#         raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#
#     def __str__(self):
#         return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'

