#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Publication:
    def __init__(self,
                 authors: list = ["Gamma", "Helm", "Johnson", "Vlissides"],
                 title: str = "Design Patterns",
                 year: int = 1994):
        # 여기를  tuple 로 바꿔서 immutable 로 하거나
        # get_authors ()의 return 에 self.__authors.copy()  로 다른 객체로 반환하거나
        self.__authors = tuple(authors)
        self.__title = title
        self.__year = year

    def __str__(self):
        ##############################################################
        ### 우리가 만든 Publication 객체를                            ###
        ### b = Publication() 으로 생성후                            ###
        ### print(b) 로 출력 할 때, 객체의 설명이 나오도록 만드는 함수    ###
        ##############################################################

        publication = "Publication"
        authors = str(list(self.__authors)).replace("'", "\"")
        title = self.__title
        year = str(self.__year)
        result = f"{publication}({authors}, \"{title}\", {year})"
        return result

    def __repr__(self):
        ################################################
        ### __str__ 과 비슷하지만 좀 다름.. 설명은 생략!  ###
        ################################################
        publication = "Publication"
        # 요구 사항이 ' 가 아닌 " 이어서 replace 함수로 변경
        authors = str(self.__authors).replace("'", "\"")
        title = self.__title
        year = str(self.__year)
        ####################################################
        ### python fstring 으로 문자열 표현                 ###
        ###  name = "초코빵"                               ###
        ### strings = f"My name is {name}"                ###
        ###     -> My name is 초코빵                       ###
        ### 의 형태로 {} 안에 들어간 변수명으로 문자열 변경     ###
        #####################################################
        result = f"{publication}({authors}, \"{title}\", {year})"
        return result

    def __hash__(self):
        #####################################################################
        ### 만들어진 객체만의 unique id 를 만드는 함수                        ###
        ### 파이썬 내장함수인  hash 함수를 사용                               ###
        ###     authors, title 그리고 year 의 조합으로 겹치지 않는 숫자 생성   ###
        # 함수의 인자로 들어가는 list 자료형(밑의 self.__authors)의 경우
        # 변수이름 앞에 '*'을 붙이면 하나씩 풀어서 들어간다
        ###         self.__authors = [a, b, c]
        # -> hash(*self.__authors)
        # -> hash(a, b, c)
        ####################################################################
        hashes = hash((*self.__authors, self.__title, self.__year))
        return hashes

    def __lt__(self, other):
        ################################################
        ### less than 을 구현                         ###
        ###     -> self < other 가 가능하도록          ###
        ### 과제에 주어진 비교는                        ###
        ###     1. author 의 수가 적을 수록            ###
        ###     2. author 의 수가 같으면               ###
        ###         2.1 title 의 알파벳 순이 작으면     ###
        ###         2.2 title 의 알파벳 순이 같으면     ###
        ###             2.2.1 출판된  year 가 작으면   ###
        ###     더 작은 객체가 된다                     ###
        ################################################
        self_authors = sorted(self.__authors)
        other_authors = sorted(other.get_authors())

        if len(self_authors) < len(other_authors):
            return True
        elif len(self_authors) == len(other_authors):
            if self_authors < other_authors:
                return True
            elif self_authors == other_authors:
                self_title = self.__title
                other_title = other.get_title()
                if self_title < other_title:
                    return True
                elif self_title == other_title:
                    self_year = self.__year
                    other_year = other.get_year()
                    ##############################
                    ### self_year < other_year  ###
                    ### 이 부분이 lt를 만듬       ###
                    ### 이 부분을 <= 로 만들면 le ###
                    ##############################
                    return self_year < other_year
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, other):
        self_authors = sorted(self.__authors)
        other_authors = sorted(other.get_authors())

        if len(self_authors) < len(other_authors):
            return True
        elif len(self_authors) == len(other_authors):
            if self_authors < other_authors:
                return True
            elif self_authors == other_authors:
                self_title = self.__title
                other_title = other.get_title()
                if self_title < other_title:
                    return True
                elif self_title == other_title:
                    self_year = self.__year
                    other_year = other.get_year()
                    return self_year <= other_year
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        ###########################################################################
        # 이미 객체의 구성 author, title, year 로 unique 한 hash 값을 생성하였으므로  ###
        #  hash 값을 비교하면 같은지 다른지 비교가 됨                                ###
        # 수동으로 비교 하고 싶을 경우엔 아래의 주석을 제거한 비교 연산을 사용           ###
        ##########################################################################
        #         return self.__authors == other.get_authors() and self.__title == other.get_title() and self.__year == other.get_year()
        return self.__hash__() == other.__hash__()

    def __ge__(self, other):
        # greater equal >=
        self_authors = sorted(self.__authors)
        other_authors = sorted(other.get_authors())

        if len(self_authors) > len(other_authors):
            return True
        elif len(self_authors) == len(other_authors):
            if self_authors > other_authors:
                return True
            elif self_authors == other_authors:
                self_title = self.__title
                other_title = other.get_title()
                if self_title > other_title:
                    return True
                elif self_title == other_title:
                    self_year = self.__year
                    other_year = other.get_year()
                    return self_year >= other_year
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        #  greater than >
        self_authors = sorted(self.__authors)
        other_authors = sorted(other.get_authors())

        if len(self_authors) > len(other_authors):
            return True
        elif len(self_authors) == len(other_authors):
            if self_authors > other_authors:
                return True
            elif self_authors == other_authors:
                self_title = self.__title
                other_title = other.get_title()
                if self_title > other_title:
                    return True
                elif self_title == other_title:
                    self_year = self.__year
                    other_year = other.get_year()
                    return self_year > other_year
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        # not equal !=
        self_authors = sorted(self.__authors)
        other_authors = sorted(other.get_authors())
        if self_authors == other_authors:
            self_title = self.__title
            other_title = other.get_title()
            if self_title == other_title:
                self_year = self.__year
                other_year = other.get_year()
                return self_year != other_year
            else:
                return True
        else:
            return True

    def get_authors(self):
        return self.__authors

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.

if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    assert str(p) == s

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    #############################################################
    ### 이 상황의 경우 p1 과 p2 가 같은 내용물로 만들어진 객체이므로  ###
    ### 완전히 같은 hash 값을 가지므로,                           ###
    ### sales[p1]과 sale[p2]는 같은 값을 가지게 됨                ###
    #############################################################
    sales = {
        p1: 273,
        p2: 398,
    }
