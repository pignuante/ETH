#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from public.character import Character

"""
 **A *Mage*** has weak armor, so the damage they take from all kinds of sources is increased by 50%, 
 however, their damage is increased by 25% and the attacks are magical
 """


class Mage(Character):
    def __init__(self, *kwargs):
        super(Mage, self).__init__(*kwargs)
        self.__reduce_dmg = (1 - (-0.5))
        self.__reduce_atk = (1 - (-0.25))

    def attack(self, other):
        assert isinstance(other, Character)

        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")
        # 나중에 여기를 _take_magical_damage 로 변경하면..
        # 그래서 미리 Overriding 해둠
        other._take_physical_damage(self._get_caused_dmg(other))

    def _get_caused_dmg(self, other):
        assert isinstance(other, Character)
        assert self is not other

        return max(1, int(((self._lvl * 10) - other._lvl) * self.__reduce_atk))

    def _take_physical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur -
                               int(round(amount * self.__reduce_dmg)))
