from project.movie_specification.movie import Movie


class Fantasy(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 6):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError(f"Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    def details(self):
        return (f"Fantasy - Title:{self.title}, Year:{self.year}, "
                f"Age restriction:{self.age_restriction}, Likes:{self.likes}, "
                f"Owned by:{self.owner.username}")






# from project.movie_specification.movie import Movie
# # from project.user import User
#
#
# class Fantasy(Movie):
#     AGE_LIMIT = 6
#     TYPE = "Fantasy"
#
#     def __init__(self, title: str, year: int, owner: object, age_restriction: int):
#         super().__init__(title, year, owner, age_restriction)
#
#     def details(self):
#         return self.take_details()



# user1 = User("John", 20)
# print(user1)
#
# movie = Fantasy("movie", 1990, user1, 20)
# print(movie.take_details())

