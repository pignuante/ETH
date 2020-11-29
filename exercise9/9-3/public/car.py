#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from abc import ABC, abstractmethod


# ABC 라는 추상 class 상속
class Car(ABC):
    @abstractmethod # 추상 함수라고 명시적으로 표시
    def get_remaining_range(self) -> float:
        """
        returns the remaining distance in kilometers (float)
        """
        pass

    @abstractmethod
    def drive(self, dist: float):
        """
         drive can be used to drive the car for `dist` kilometers
        """
        pass
