class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return self.min_length <= len(name)

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        name, rest = email.split("@")
        email, domain = rest.split(".")
        return all([self.__is_name_valid(name) and self.__is_mail_valid(email) and self.__is_domain_valid(domain)])


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))




# class EmailValidator:
#     def __init__(self, min_length: int, mails: list, domains: list):
#         self.min_length = min_length
#         self.mails = mails
#         self.domains = domains
#
#     def __is_name_valid(self, name):
#         return self.min_length <= len(name)
#
#     def __is_mail_valid(self, mail):
#         if any(m == mail for m in self.mails):
#             return True
#         return False
#
#
#     def __is_domain_valid(self, domain):
#         if any(d for d in self.domains if d == domain):
#             return True
#         return False
#
#     def validate(self, email):
#         name, rest = email.split("@")
#         email, domain = rest.split(".")
#         if self.__is_name_valid(name) and self.__is_mail_valid(email) and self.__is_domain_valid(domain):
#             return True
#         return False

