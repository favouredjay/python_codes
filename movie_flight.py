class Movie_flight(object):

    def user_can_only_watch_different_movies(flight_length, movie_length) -> int:
        # movie_length = [60, 20, 40, 50, 50]
        for x in movie_length:
            for y in range(x):
                if x + y == flight_length:
                    print(x, y)
            return True
        else:
            return False


if __name__ == '__main__':
    Movie_flight.user_can_only_watch_different_movies(movie_length=[20, 34, 13, 10, 50, 80, 50, 50, 40],
                                                      flight_length=100)
