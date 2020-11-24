#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.

import re


class ProfanityFilter:
    def __init__(self, keywords: list = ["duck", "shot", "batch", "mastard"], template: str = "?#$"):
        ####################################################################################
        # 긴 단어부터 filtering 하기 위해서 단어의 길이로 정렬                                 ###
        # sorted      -> list 형의 데이터를 정렬하고 정렬된 리스트를 반환하는 함수               ###
        # sorted(key) -> key 에 리스트의 인자들을 key 함수에 넣고, 그 결과로 정렬하게 해주는 인자 ###
        #             -> 여기서는 duck, shot, batch 그리고 mastard 각각의 길이를 정렬한다      ###
        # sorted(reverse=True) -> reverse 에 True 를 주면 역순으로 정렬                     ###
        ####################################################################################
        self._keywords = sorted(keywords, key=len, reverse=True)
        self._template = template

    def filter(self, msg: str = "abc defghi mastard jklmno"):
        for keyword in self._keywords:
            ###################################################################
            ### 편하게 가는 길은 아래 코드                                      ###
            ### 단, 대소문자 구분은 아직 추가하지 않음                           ###
            ### 이유는 문자의 출력이 마스킹된 원본이랑 같은 문자를 출력해야하는지    ###
            ### 아니면 대소문자 구분없이 출력해도 괜찮은지에 대한 지침을 아직 몰라서 ###
            ##################################################################
            #             msg = msg.replace(keyword, self.make_mask(keyword=keyword))

            ########################################################################
            ### 정규표현식을 이용한 문자열 치환                                       ###
            ### 이론적으로는 이런식으로 하는것이 best 임                                ###
            ### compiled.sub(a, b) -> compiled 된 규칙으로, b를 a로 바꿈 이라는 의미   ###
            ########################################################################
            compiled = self.compile_regex(keyword=keyword)
            msg = compiled.sub(self.make_mask(keyword=keyword), msg)

        return msg

    def compile_regex(self, keyword: str = "duck"):
        ###############################################################
        ### 대소문자 구분을 위한 편한 길을 위해서 정규표현식(regex)를 사용  ###
        ### https://devanix.tistory.com/296 요기에 정리 잘 되어 있음   ###
        ### re.I로 대소문자 구분하지 않고 문자 치환하도록 설정            ###
        ##############################################################
        com = re.compile(keyword, re.I)
        return com

    def make_mask(self, keyword: str = "mastard"):
        ###################################################################
        ### masking 할 단어 생성                                          ###
        ### masking 을 "?#$"으로 해야하고 masking 할 단어가 "mastard"일 경우 ###
        ### mastard -> ?#$     이 아니고                                  ###
        ### mastard -> ?#$?#$? 로 변환하여야하므로                          ###
        ### masking 할 단어를 생성하는 함수                                 ###
        ###################################################################

        # 단어의 길이로 masking 을 생성
        keyword_len = len(keyword)
        template_len = len(self._template)
        mask = self._template * (keyword_len // template_len) + \
               self._template[:keyword_len % template_len]
        return mask


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
