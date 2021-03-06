#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class MagicDrawingBoard:
    def __init__(self, x: int, y: int):
        """
            Magic Drawing Board 를 생성하는 생성자
        :param x: 보드의 X(가로) 크기
        :param y: 볻의 Y(세로)의 크기
        """
        ##################################################################################
        ### 경고 메세지                                                                 ###
        ### You implementation should handle invalid situations by raising a Warning  ###
        ### 라고 적혀있는데 예외 사항 발생시 어떤식으로 처리하라는 가이드가 없어서 우선은        ###
        ### print(error_message) 로 처리                                              ###
        ################################################################################
        self.__warning_message = "Warning"

        ################################
        ### 생성시 예외사항            ###
        ### x, y 크기가 0보다 작을 경우 ###
        ##############################
        if x < 0 or y < 0:
            print(self.__warning_message)
        else:
            # Board 의 크기를 맴버 변수로 저장, 후에 reset,  rect 등에서 보드 크기 확인할때 필요
            self.__size = (x, y)
            # board 를 배열의 형태로 저장
            # 접근은 __board[y][x] 로 접근
            self.__board = [[0 for xx in range(x)] for yy in range(y)]

    def reset(self):
        ##############################################
        ### board에 저작된 pixels를 제거(0으로 만듬)  ###
        ##############################################

        self.__board = [
            [0 for x in range(self.__size[0])] for y in range(self.__size[1])
        ]

    def pixel(self, xy: tuple = (1, 1)):
        """
            x, y 에 해당하는 위치에 pixel 을 그림(0 -> 1)
        :param xy: tuple, x = xy[0], y = xy[1]
        """
        x, y = xy[0], xy[1]
        ####################################################
        ### pixel 을 그릴 때 예외 사항                      ###
        ###     1. x 혹은  y 가 0 보다 작을 경우            ###
        ###     2. x 혹은 y 가 board 의 크기 보다 클 경우    ###
        ### 위 두가지 사항을 예외로 두고 에러 message 발생    ###
        ### 배열의 크기가 x = 3, y = 6 일 경우              ###
        ### x index 는 0,1,2이고 y index 는 1,2,3,4,5 임  ###
        ### 따라서 최대 크기 설정시 size - 1 을 해야함       ###
        ###################################################
        if x < 0 or y < 0:
            print(self.__warning_message)
        elif x > self.__size[0] - 1 or y > self.__size[1] - 1:
            print(self.__warning_message)
        else:
            self.__board[y][x] = 1

    def rect(self, start_xy: tuple, end_xy: tuple):
        """
            start_xy 와 end_xy 로 직사각형을 그리는 함수
            좌표상 예외 발생시 Warning을 print
        :param start_xy: (x, y)
        :param end_xy:   (x, y)
        """
        x1, y1 = start_xy[0], start_xy[1]
        ############################
        ### exclusive 해야하므로   ###
        ############################
        x2, y2 = end_xy[0], end_xy[1]

        if x1 < 0 or y1 < 0 or x1 >= x2 or y1 >= y2:
            print(self.__warning_message)
        elif x2 > self.__size[0] or y2 > self.__size[1]:
            print(self.__warning_message)
        ##############################################
        ###  무조건 우하단에 존재하려면 밑의 주석을 지움 ###
        #############################################
        # elif x1 == x2-1 or y1 == y2-1:
        #     print(self.__warning_message)
        else:
            for y in range(y1, y2):
                for x in range(x1, x2):
                    self.pixel((x, y))

    def img(self):
        # board 에 저장된 pixel 을 문자열로 바꿔서 출력
        img = ""
        for y in self.__board:
            for x in y:
                img += str(x)
            img += "\n"
        return img.strip()


# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6, 4)
    db.pixel((1, 1))
    db.rect((2, 2), (5, 4))
    print("After drawing:")
    print(db.img())
    db.reset()
    print("After resetting:")
    print(db.img())


class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    def get_authors(self):
        return self.__authors

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __hash__(self):
        keys = self.__authors
        keys.append(self.__title)
        keys.append(self.__year)
        return hash(tuple(keys))

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        else:
            return self.__authors == other.__authors \
                   and self.__title == other.__title \
                   and self.__year == other.__year

    def __lt__(self, other):
        if type(other) != Publication:
            return NotImplemented
        if self.__authors < other.__authors:
            return True
        elif self.__authors == other.__authors:
            if self.__title < other.__title:
                return True
            elif self.__title == other.__title:
                return self.__year < other.__year
        return False

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return other < self


4
번


class MagicDrawingBoard:
    def __init__(self, x, y):
        if x <= 0 or y <= 0:
            raise Warning("Board is too small, positive dimensions required.")
        self.__x = x
        self.__y = y
        self.reset()

    def reset(self):
        self.__board = self.__x * self.__y * [0]

    def _idx(self, xy):
        x, y = xy
        return y * self.__x + x

    def _assert_coords(self, xy, is_end=False):
        x, y = xy
        if x < 0 or y < 0 or x > self.__x or y > self.__y:
            raise Warning("Coordinates point outside of the board.")
        if not is_end:
            if x == self.__x or y == self.__y:
                raise Warning("Only the endpoint of a rectangle can use coordinates that are outside the board.")

    def pixel(self, xy):
        self._assert_coords(xy)
        idx = self._idx(xy)
        self.__board[idx] = 1

    def rect(self, start_xy, end_xy):
        self._assert_coords(start_xy)
        self._assert_coords(end_xy, True)

        width = end_xy[0] - start_xy[0]
        height = end_xy[1] - start_xy[1]
        if width < 1 or height < 1:
            raise Warning("Width and height of a rectangle must be greater than 0.")

        idx = self._idx(start_xy)
        for delta_x in range(width):
            for delta_y in range(height):
                cur = idx + delta_x + delta_y * self.__x
                self.__board[cur] = 1

    def img(self):
        s = ""
        for idx, v in enumerate(self.__board):
            if idx > 0 and idx % self.__x == 0:
                s += "\n"
            s += "1" if v else "0"
        return s
