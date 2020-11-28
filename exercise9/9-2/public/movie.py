#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:
    def __init__(self, title: str, actors: list, duration: int):
        assert isinstance(title, str)
        assert len(title) > 0
        assert isinstance(actors, list)
        assert isinstance(actors[0], str)
        assert len(actors) > 1
        assert duration > 1

        self.__title = title
        self.__actors = actors
        self.__duration = duration

    def __repr__(self) -> str:
        name = f'Movie("{self.__title}", {str(self.__actors)}, {self.__duration})'.replace(
            "\'", "\"").strip()
        return name

    def __key(self) -> tuple:
        return (self.__title, *self.__actors, self.__duration)

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other) -> bool:
        assert isinstance(other, Movie)
        return self.__hash__() == other.__hash__()

    def get_title(self) -> str:
        return self.__title

    def get_actors(self) -> list:
        return self.__actors.copy()

    def get_duration(self) -> int:
        return self.__duration

    # also implement the required special functions
