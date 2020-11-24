#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Fridge:
    def __init__(self):
        # 냉장고에 저장 될 item 을 list 에 저장
        self.__stored_item = []
        # 지금 어디를 가르키고 있는지를 인지하기 위한 변수
        self.__current = 0

    def __next__(self):
        ################################################################################
        ### 우리가 list 자료형에서 iteration 이 되는 것처럼                              ###
        ###     ex) a = [1,2,3,4,5] -> for x in a 가 가능한것 처럼                     ###
        ### 우리가 만든 객체도 f = Fridge(); for item in f  가 가능하도록 만들어주는 함수   ###
        ################################################################################
        if self.__current < len(self):
            value = self.__stored_item[self.__current]
            self.__current += 1
            return value
        else:
            ###########################################################################
            ### 저장된 아이템수 보다 더 많이 순회 할 경우 멈추기 위한 error 발생            ###
            ### raise 는 python 에서 error 를 고의로 일으키는 함수                       ###
            ### StopIteration 은 파이썬에 내장된 iteration 에 문제가 생격다는 error 이름   ###
            ############################################################################
            raise StopIteration

    def __iter__(self):
        ######################################################
        ### 위 __next__ 함수를 이용하여 iteration 을 하는 함수  ###
        ######################################################
        return self

    def __len__(self):
        ########################################
        ### 객체의 길이를 표시하게 해주는 함수    ###
        ### f = Fridge(), len(f) 를 가능케    ###
        ########################################
        return len(self.__stored_item)

    def store(self, item: tuple = (191127, "Butter")):
        self.__stored_item.append(item)
        self.__stored_item = sorted(self.__stored_item, key=lambda x: x[0])

    def take(self, item):
        if item in self.__stored_item:
            idx = self.__stored_item.index(item)
            # 나중에 쓸일이 있을까해서 뺀 item 을 우선은 변수에 저장
            removed_item = self.__stored_item.pop(idx)
            # 출력 성공과 실패를 그냥 문자열  ok, fail 하면 되는지 모르겠어서 우선은...
            return removed_item
        return

    def find(self, name):
        item = sorted(
            [x for x in self.__stored_item if name in x[1]],
            key=lambda x: x[0]
        )
        ##############################################################################
        ### error message 를 문자열  "None"으로 해야하는지 그냥 None 인지 모르겠어서 우선은..
        ##############################################################################

        return item if len(item) else []

    def take_before(self, date):
        removed = [x for x in self.__stored_item if date >= x[0]]

        [self.__stored_item.remove(x) for x in removed]
        return removed


# To implement the required functionality, you will also have to implement several
# of the special functions that typically include a double underscore.

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    l = ["a", "b", "c"]
    for i in l:
        l.remove(i)

    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    i = f.take((191127, "Butter"))
    print("Removed {}, {} items left".format(i, len(f)))
