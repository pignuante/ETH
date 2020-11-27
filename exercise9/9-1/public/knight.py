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

        return max(1, int(((self._lvl * 10) - other._lvl) * self.__reduce_atk))

    def _take_physical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur -
                               int(round(amount * self.__reduce_dmg)))
