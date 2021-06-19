class Movie_flight(object):

    def user_can_only_watch_different_movies(flight_length: int) -> int:
        movie_length = [60, 20, 40, 50, 50]
        for x in movie_length:
            for y in range(x):
                if x + y == flight_length:
                    print(x, y)
                return True
            else:
                return False
