from project.movie_specification.movie import Movie


class Thriller(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError(f"Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value

    def details(self):
        return (f"Thriller - Title:{self.title}, Year:{self.year}, "
                f"Age restriction:{self.age_restriction}, Likes:{self.likes}, "
                f"Owned by:{self.owner.username}")


# user1 = User("John", 20)
# print(user1)
#
# movie = Action("movie", 1990, user1, 20)
# print(movie.take_details())







# from project.movie_specification.movie import Movie
# # from project.user import User
#
#
# class Thriller(Movie):
#     AGE_LIMIT = 16
#     TYPE = "Thriller"
#
#     def __init__(self, title: str, year: int, owner: object, age_restriction: int):
#         super().__init__(title, year, owner, age_restriction)
#
#     def details(self):
#         return self.take_details()
