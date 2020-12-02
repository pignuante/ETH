#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):
    def __init__(self, gas_capacity: float, gas_per_100km: float, battery_size: float, battery_range_km: float):
        """
        `HybridCar` inherits all properties and functionalities of the other two cars types and,
        as such, needs all parameters for the initialization.
        The two methods `switch_to_combustion` and `switch_to_electric` can be used to change the operation mode
        `HybridCar` inherits two conflicting definitions of the methods `get_remaining_range` and `drive`,
        adapt the implementations to make them work.
        The implementations of the different cars should handle invalid parameters
        like capacities, fuel/charge amounts, or distances that are negative or that do have a different type
        than expected. Raise a `Warning` in all these cases.
        Make sure that gas tank/battery are set to `0` when you raise a `Warning`.
        """
        CombustionCar.__init__(
            self, gas_capacity=gas_capacity, gas_per_100km=gas_per_100km)
        ElectricCar.__init__(self, battery_size=battery_size,
                             battery_range_km=battery_range_km)
        self.__drive_mode = True  # True Elec, False Comb

    def __switch_to_mode(self):
        self.__drive_mode = not self.__drive_mode

    def switch_to_combustion(self):
        if not self.__drive_mode:
            raise Warning("[WARNING] Drive mode is already Comb mode.")
        self.__drive_mode = False

    def switch_to_electric(self):
        if self.__drive_mode:
            raise Warning("[WARNING] Drive mode is already Elec mode.")
        self.__drive_mode = True

    def get_remaining_range(self) -> float:
        remaining_range = ElectricCar.get_remaining_range(
            self) + CombustionCar.get_remaining_range(self)
        return remaining_range

    def drive(self, dist: float):
        """
        Should the car run out of fuel or battery during a tour, it should automatically switch the mode.
        If both modes are fully depleted, the car should raise a `Warning`.
        """
        if self.__drive_mode:  # 전기차면
            elec_remained = ElectricCar.get_remaining_range(self)
            remain_dist = dist - elec_remained
            ElectricCar.drive(
                self, elec_remained if remain_dist > 0 else dist)
            print(remain_dist)
            if remain_dist > 0:
                self.__switch_to_mode()
                CombustionCar.drive(self, remain_dist)
        else:
            comb_remained = CombustionCar.get_remaining_range(self)
            remain_dist = dist - comb_remained
            CombustionCar.drive(
                self, comb_remained if remain_dist > 0 else dist)
            if remain_dist > 0:
                self.__switch_to_mode()
                ElectricCar.drive(self, remain_dist)
