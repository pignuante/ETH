#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):
    def __init__(self, gas_capacity: float, gas_per_100km: float, battery_size: float, battery_range_km: float):
        """
        After initializing a car,
        gas tanks and batteries are full,
        and a HybridCar should operate in electrical mode
        """
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__drive_mode = True  # True = 전기차, False = 내연기관

    def switch_to_combustion(self):
        self.__drive_mode = False

    def switch_to_electric(self):
        self.__drive_mode = True

    def get_remaining_range(self) -> float:
        # 상속받은 ElectricCar & CombustionCar 의 함수를 활요
        remaining_range = ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)
        return remaining_range

    def drive(self, dist: float):
        e = ElectricCar.get_remaining_range(self)
        c = CombustionCar.get_remaining_range(self)
        assert isinstance(dist, float)
        assert dist > 0
        assert dist <= e + c

        # 보기는 안좋지만 수동으로 모드 드라이빙 구현
        if self.__drive_mode:
            ed = dist if dist <= e else e
            dist -= e
            ElectricCar.drive(self, ed)
            if dist > 0:
                CombustionCar.drive(self, dist)
        else:
            cd = dist if dist <= c else c
            dist -= c
            CombustionCar.drive(self, cd)
            if dist > 0:
                ElectricCar.drive(self, dist)
