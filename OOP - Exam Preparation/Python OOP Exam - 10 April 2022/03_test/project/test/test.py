from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Movie1", 2000, 10.0)

    def test_init(self):
        self.assertIsInstance(self.movie, Movie)
        self.assertEqual(self.movie.name, "Movie1")
        self.assertEqual(self.movie.year, 2000)
        self.assertEqual(self.movie.rating, 10.0)
        self.assertEqual(self.movie.actors, [])

    def test_name_with_empty_string_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        message = "Name cannot be an empty string!"
        self.assertEqual(str(ve.exception), message)

    def test_year_with_invalid_value_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        message = "Year is not valid!"
        self.assertEqual(str(ve.exception), message)

    def test_add_actor(self):
        self.movie.add_actor("Gosho")
        self.assertEqual(self.movie.actors, ["Gosho"])

    def test_add_actor_with_already_added_actor(self):
        self.movie.add_actor("Gosho")
        self.assertEqual(self.movie.actors, ["Gosho"])
        res = self.movie.add_actor("Gosho")
        message = "Gosho is already added in the list of actors!"
        self.assertEqual(res, message)

    def test_add_actor_with_already_added_actors(self):
        self.movie.add_actor("Gosho")
        self.movie.add_actor("Pesho")
        self.assertEqual(self.movie.actors, ["Gosho", "Pesho"])
        res = self.movie.add_actor("Gosho")
        message = "Gosho is already added in the list of actors!"
        self.assertEqual(res, message)

    def test_grater_than_method(self):
        self.other_movie = Movie("Movie2", 2000, 9.0)
        res = self.movie.__gt__(self.other_movie)
        message = f'"{self.movie.name}" is better than "{self.other_movie.name}"'
        self.assertEqual(res, message)

    def test_grater_than_method_other_movie_greater_rating(self):
        self.other_movie = Movie("Movie2", 2000, 11.0)
        res = self.movie.__gt__(self.other_movie)
        message = f'"{self.other_movie.name}" is better than "{self.movie.name}"'
        self.assertEqual(res, message)

    def test_repr_method(self):
        self.movie.add_actor("Gosho")
        self.movie.add_actor("Pesho")
        res = f"Name: {self.movie.name}\n" \
              f"Year of Release: {self.movie.year}\n" \
              f"Rating: {self.movie.rating:.2f}\n" \
              f"Cast: {', '.join(self.movie.actors)}"
        action = self.movie.__repr__()
        self.assertEqual(res, action)
