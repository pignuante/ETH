#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car


class CombustionCar(Car):

    def __init__(self, gas_capacity: float, gas_per_100km: float):
        self.__gas_capacity = gas_capacity
        self.__gas_per_100km = gas_per_100km
        self.__gas_quantity = gas_capacity
        self.__gas_mileage_dist = self.__gas_per_100km / 100  # 1km 가는데 소비되는 연료
        self.__gas_mileage_liter = 100 / self.__gas_per_100km  # 1l 당 갈수 있는 km

    def fuel(self, f: float):
        """
        The car can be refueled using fuel, which adds f liters of fuel to the gas tank
        The method should raise a `Warning`, if the gas tank gets overfilled
        """
        assert isinstance(f, float)
        assert f > 0.0
        assert self.__gas_quantity + f <= self.__gas_capacity

        self.__gas_quantity += f

    def get_gas_tank_status(self) -> tuple:
        """
         A call to get_gas_tank_status returns the current gas tank capacity c,
         and the maximum capacity _max as a tuple (c, c_max)
        """
        return self.__gas_quantity, self.__gas_capacity

    def get_remaining_range(self) -> float:
        """
            갈수있는 거리 = 남은 연료 L 량 * 1L 당 갈 수 있는 거리
        """
        return self.__gas_quantity * self.__gas_mileage_liter

    def drive(self, dist: float):
        """
         On use, drive should remove the correct amount of gas from the gas tank,
         and it should raise a Warning if the gas tank is fully depleted through driving
        """
        assert isinstance(dist, float)
        assert dist > 0
        assert dist * self.__gas_mileage_dist <= self.__gas_quantity
        self.__gas_quantity -= dist * self.__gas_mileage_dist
