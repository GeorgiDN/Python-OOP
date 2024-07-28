from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list = []
        self.users_collection: list = []

    def register_user(self, username: str, age: int):
        user_ = self._get_object_by_username(self.users_collection, username)
        if user_:
            raise Exception(f"User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user_ = self._get_object_by_username(self.users_collection, username)
        if not user_:
            raise Exception(f"This user does not exist!")

        if movie.owner != user_:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception(f"Movie already added to the collection!")

        user_.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user_ = self._get_object_by_username(self.users_collection, username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user_:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user_ = self._get_object_by_username(self.users_collection, username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user_:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user_.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user_ = self._get_object_by_username(self.users_collection, username)

        if movie.owner == user_:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user_.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user_.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user_ = self._get_object_by_username(self.users_collection, username)

        if movie not in user_.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user_.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))
        result = [curr_movie.details() for curr_movie in sorted_movies]

        return "\n".join(result)

    def __str__(self):
        result = []

        if self.users_collection:
            all_users = ', '.join(u.username for u in self.users_collection)
            result.append(f"All users: {all_users}")
        else:
            result.append("All users: No users.")

        if self.movies_collection:
            all_movies = ', '.join(m.title for m in self.movies_collection)
            result.append(f"All movies: {all_movies}")
        else:
            result.append("All movies: No movies.")

        return "\n".join(result)

    ###
    @staticmethod
    def _get_object_by_username(object_list, username):
        found_object = next((obj for obj in object_list if obj.username == username), None)
        return found_object



# movie_app = MovieApp()
# print(movie_app.register_user('Martin', 24))
# user = movie_app.users_collection[0]
# movie = Action('Die Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie))
# print(movie_app.movies_collection[0].title)
# print(movie_app.register_user('Alexandra', 25))
# user2 = movie_app.users_collection[1]
# movie2 = Action('Free Guy', 2021, user2, 16)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.like_movie('Alexandra', movie))
# print(movie_app.dislike_movie('Martin', movie2))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.display_movies())
# print(movie_app)



"""
Martin registered successfully.
Martin successfully added Die Hard movie.
Die Hard
Alexandra registered successfully.
Alexandra successfully added Free Guy movie.
Alexandra successfully edited Free Guy 2 movie.
Martin liked Free Guy 2 movie.
Alexandra liked Die Hard movie.
Martin disliked Free Guy 2 movie.
Martin liked Free Guy 2 movie.
Alexandra successfully deleted Free Guy 2 movie.
Alexandra successfully added The Lord of the Rings movie.
Fantasy - Title:The Lord of the Rings, Year:2003, Age restriction:14, Likes:0, Owned by:Alexandra
Action - Title:Die Hard, Year:1988, Age restriction:18, Likes:1, Owned by:Martin
All users: Martin, Alexandra
All movies: Die Hard, The Lord of the Rings
"""
