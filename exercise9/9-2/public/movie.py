#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:
    def __init__(self, title: str, actors: list, duration: int):
        if isinstance(title, str) is False:
            raise Warning("[WARNING] Title must be Str")
        if not title:
            raise Warning("[WARNING] Title length must be bigger than 1")
        if isinstance(actors, list) is False:
            raise Warning("[WARNING] Actors must be List")
        if not actors:
            raise Warning("[WARNING] Actors len must be bigger than 1")
        for actor in actors:
            if isinstance(actor, str) is False:
                raise Warning("[WARNING] Actor must be Str")
        if isinstance(duration, int) is False:
            raise Warning("[WARNING] Duration must be Int")
        if duration < 1:
            raise Warning("[WARNING] Duration must be bigger than 1")

        self.__title = title
        self.__actors = actors
        self.__duration = duration

    def __repr__(self) -> str:
        name = f'Movie("{self.__title}", {str(self.__actors)}, {self.__duration})'.replace(
            "\'", "\"").strip()
        return name

    def __key(self) -> tuple:
        return self.__title, *self.__actors, self.__duration

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other) -> bool:
        if isinstance(other, Movie) is False:
            raise Warning("[WARNING] Other Obj must be Movie Obj")
        return self.__hash__() == other.__hash__()

    def get_title(self) -> str:
        return self.__title

    def get_actors(self) -> list:
        return self.__actors.copy()

    def get_duration(self) -> int:
        return self.__duration
    # also implement the required special functions
