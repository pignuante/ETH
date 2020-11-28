#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:
    def __init__(self, title: str, actors: list, duration: int):
        ##############################
        ### type check 철저히  #######
        #############################
        assert isinstance(title, str)
        assert len(title) > 0
        assert isinstance(actors, list)
        for actor in actors:
            assert isinstance(actor, str)
        assert len(actors) > 1
        assert duration > 1

        self.__title = title
        self.__actors = actors
        self.__duration = duration
        self.hash = hash((self.__title, *self.__actors, self.__duration))

    def __repr__(self) -> str:
        #####################################
        ### 'Movie("T", ["A", "B"], 123)' ###
        #####################################
        name = f'Movie("{self.__title}", {str(self.__actors)}, {self.__duration})'.replace(
            "\'", "\"").strip()
        return name

    def __key(self) -> tuple:
        #####################################
        ### 타이틀 & 배우들 & 시간의 조합으로 ###
        ### 유일 값을 만들기 위한 리스트 생성 ###
        ####################################
        return (self.__title, *self.__actors, self.__duration)

    def __hash__(self) -> int:
        ##########################
        ### 객체의 고유 번호 생성 ###
        ##########################
        return hash(self.__key())

    def __eq__(self, other) -> bool:
        ##################################
        ### __hash__() 로 생성한 고유번호 ###
        ### 같은 객체인지 아닌지 비교      ###
        ##################################
        assert isinstance(other, Movie)
        return self.__hash__() == other.__hash__()

    def get_title(self) -> str:
        return self.__title

    def get_actors(self) -> list:
        ##########################################
        ### copy 함수로 다른 리스트를 생성해서 반납 ###
        ### 이유는                              ###
        ###     a = [1,2,3,4,5]                ###
        ###     b = a                          ###
        ###     b[0] = 999                     ###
        ###     print(a,b)                     ###
        ### 의 결과를 보시길                     ###
        ##########################################

        return self.__actors.copy()

    def get_duration(self) -> int:
        return self.__duration

    # also implement the required special functions
