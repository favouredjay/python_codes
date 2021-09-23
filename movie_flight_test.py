import unittest
from movie_flight import Movie_flight


class Movie_flightTest(unittest.TestCase):
    def test_that_user_can_watch_two_different_movies(self):
        movie_length = [20, 30, 40, 60, 50, 50]
        self.assertTrue(Movie_flight.user_can_only_watch_different_movies(100, movie_length))


