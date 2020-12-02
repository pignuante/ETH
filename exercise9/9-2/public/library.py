#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.movie import Movie
from public.moviebox import MovieBox


class Library():
    def __init__(self):
        self.__movies = []

    def add_movie(self, movie):
        if isinstance(movie, MovieBox) or isinstance(movie, Movie):
            if movie in self.__movies:
                raise Warning("[WARNING] Duplicated movie")
            self.__movies.append(movie)
        else:
            raise Warning("[WARNING] input Data Type")

    def get_actors(self):
        actors = []
        for movie in self.get_movies():
            actors.extend(movie.get_actors())
        return sorted(set(actors))

    def get_movies(self):
        movies = []
        for movie in self.__movies:
            if isinstance(movie, MovieBox):
                movies.extend(movie.get_movies())
            else:
                movies.append(movie)
        return sorted(set(movies), key=lambda x: x.get_title())

    def get_total_duration(self):
        duration = 0
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration
