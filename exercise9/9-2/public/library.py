#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.movie import Movie
from public.moviebox import MovieBox


class Library(Movie):
    def __init__(self):
        self.__movies = []
        self.__movieBoxes = []
        self.__duration = 0

    def add_movie(self, movie):
        ################################################
        ### 정말 좋은 방법이 아닌 함수                  ###
        ### 타 객체지향 언어는 overloading 이라는 걸로   ###
        ### 한 함수에 다양한 자료형 input 을 받는데      ###
        ### 파이썬은 그게 안되서 수동으로                ###
        ### 들어오는 자료형에 따라서 구현해야함           ###
        ### The add_movie methods has to ensure that ###
        ### the same movie is not added multiple times ###
        ###  설명은 있는데 box에 설명은 없어서 우선
        ### box 중복도 제거
        ###############################################
        if isinstance(movie, MovieBox):
            # input 이 MovieBox 일 경우
            assert movie not in self.__movieBoxes
            self.__movieBoxes.append(movie)
            self.__duration += movie.get_duration()
        elif isinstance(movie, Movie):
            # input 이 Movie 일 경우
            assert movie not in self.__movies
            self.__movies.append(movie)
            self.__duration += movie.get_duration()
        else:
            # 그 외의 경우는 에러
            # 기분상 raise warning 안하면 감점일 기분
            assert isinstance(movie, Movie)

    def get_actors(self):
        actors = []
        for movie in self.get_movies():
            actors.extend(movie.get_actors())
        return sorted(set(actors))

    def get_movies(self):
        """
         Library should also provide a get_movies method that (recursively) lists all actual movies (ordered by title)
         and omits the boxes
        """
        #################################################################
        ### omits the boxes 라서 그냥 movie 로 들어온 영화만 출력하도록 함 ###
        ### set 자료형으로 중복 제거 후 영화 제목 순으로 정렬 함            ###
        ################################################################

        return sorted(set(self.__movies.copy()), key=lambda x: x.get_title())

    def get_total_duration(self):
        return self.__duration
