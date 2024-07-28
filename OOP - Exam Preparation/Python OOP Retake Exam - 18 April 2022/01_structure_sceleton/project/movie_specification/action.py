from project.movie_specification.movie import Movie


class Action(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 12:
            raise ValueError(f"Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value

    def details(self):
        return (f"Action - Title:{self.title}, Year:{self.year}, "
                f"Age restriction:{self.age_restriction}, Likes:{self.likes}, "
                f"Owned by:{self.owner.username}")

# user1 = User("John", 20)
# print(user1)
#
# movie = Action("movie", 1990, user1, 20)
# print(movie.take_details())


