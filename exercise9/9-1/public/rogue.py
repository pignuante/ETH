#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from public.character import Character

"""
A ***Rogue*** is a balanced class that performs physical damage. 
They have medium armor and can hit hard, both follows the rules defined before.
"""


class Rogue(Character):
    def __init__(self, *kwargs):
        super(Rogue, self).__init__(*kwargs)
