#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.movie import Movie


class MovieBox(Movie):
    def __init__(self, title: str, movies: list):
        assert isinstance(title, str)
        assert len(title) > 0
        assert isinstance(movies, list)
        for movie in movies:
            assert isinstance(movie, Movie)

        self.__title = title
        self.__movies = movies

    def __repr__(self) -> str:
        name = f'MovieBox("{self.get_title()}", {self.get_movies()})'.replace(
            "\'", "\"").strip()
        return name

    def __key(self) -> tuple:
        return (self.get_title(), *self.get_movies())

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other: Movie) -> bool:
        assert isinstance(other, MovieBox)
        return self.__hash__() == other.__hash__()

    def get_title(self) -> str:
        return self.__title

    def get_actors(self) -> list:
        #########################################
        ### actor 는 한 영화에 여러명일수도 있으니 ###
        ### 반복문을 사용해서 list 에 넣는다      ###
        ### append 함수와 extend 함수의 차이는   ###
        ###     l = []                        ###
        ###     l.append([1,2,]) -> [[1,2]]   ###
        ###     l.extend([1,2,]) -> [1,2,]    ###
        ### 의 차이                            ###
        #########################################
        actors = []
        for movie in self.get_movies():
            actors.extend(movie.get_actors())
        return sorted(set(actors))

    def get_duration(self) -> int:
        sum_of_duration = 0
        for movie in self.get_movies():
            sum_of_duration += movie.get_duration()

        return sum_of_duration

    def get_movies(self) -> list:
        return self.__movies.copy()

    # also implement the required special functions
