#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from public.character import Character

"""
***Knights*** also deal physical damage. 
They have strong armor and can wear a shield that reduces any physical damage by **25%**. 
Unfortunately, this comes at a price, their attacks deal **20% less damage than usual**
"""


class Knight(Character):
    def __init__(self, *kwargs):
        super(Knight, self).__init__(*kwargs)
        self.__reduce_dmg = (1 - 0.25)
        self.__reduce_atk = (1 - 0.2)

    def _get_caused_dmg(self, other):
        assert isinstance(other, Character)
        assert self is not other
        ###################################################################
        ### 나이트 공격력 원래 공격의 80%                                  ###
        ### 공격력 : round(((내 레벨 * 10) + (내 레벨 - 적 레벨)) * 0.8)   ###
        ##################################################################
        damage = int(round((self._lvl * 10 + (self._lvl - other._lvl)) * 0.8))
        return max(1, damage)

    def _take_physical_damage(self, amount):
        ########################################
        ### 나이트 방어력 +25%                 ###
        ###     상대방이 준 데미지 * (1 - 0.25)  ###
        ########################################
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur -
                               int(round(amount * self.__reduce_dmg)))
