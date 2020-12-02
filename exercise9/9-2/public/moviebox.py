#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.movie import Movie


class MovieBox(Movie):
    def __init__(self, title: str, movies: list):
        if isinstance(title, str) is False:
            pass
        if isinstance(movies, list) is False:
            pass
        for movie in movies:
            if isinstance(movie, Movie) is False:
                pass
        self.__title = title
        self.__movies = movies

    def __repr__(self):
        movies = str([x for x in self.get_movies()])
        rep = f'MovieBox("{self.__title}", {movies})'.replace("\'", "\"")
        return rep

    def __keys(self) -> tuple:
        keys_of_movies = [movie.__hash__() for movie in self.__movies]
        return self.get_title, *keys_of_movies

    def __hash__(self) -> int:
        return hash(self.__keys())

    def get_title(self) -> str:
        return self.__title

    def get_actors(self) -> list:
        """
        The same is true for the list of actors.
        The list of actors for a MovieBox is the combination of all lists of every contained Movie.
        Make sure that, for MovieBox, this list gets sorted alphabetically
        and that it does not contain duplicates.
        """
        actors = []
        for movie in self.get_movies():
            actors.extend(movie.get_actors())
        actors = sorted(set(actors))
        return actors

    def get_duration(self) -> int:
        duration = 0
        for movie in self.get_movies():
            duration += movie.get_duration()
        return duration

    def get_movies(self) -> list:
        return self.__movies.copy()

    # also, implement the required special functions
