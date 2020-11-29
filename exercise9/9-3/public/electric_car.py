#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car


class ElectricCar(Car):
    def __init__(self, battery_size: float, battery_range_km: float):
        """
        ElectricCars are initiated with a battery_size in kilo-watt hours,
        and the range of a fully charged battery in kilometers
        """
        assert isinstance(battery_size, float)
        assert battery_size > 0
        assert isinstance(battery_range_km, float)
        assert battery_range_km > 0

        self.__battery_size = battery_size
        self.__battery_level = battery_size
        self.__battery_range_km = battery_range_km  # 완충시 갈수있는 km?
        self.__battery_mileage_per_size = battery_range_km / battery_size
        self.__battery_mileage_per_dist = battery_size / battery_range_km

    def charge(self, kwh: float):
        assert isinstance(kwh, float)
        assert kwh > 0.0
        assert self.__battery_level + kwh <= self.__battery_size
        self.__battery_level += kwh

    def get_battery_status(self) -> tuple:
        return self.__battery_level, self.__battery_size

    def get_remaining_range(self) -> float:
        return self.__battery_level * self.__battery_mileage_per_size

    def drive(self, dist: float):
        assert isinstance(dist, float)
        assert dist > 0
        battery_level = self.__battery_level - \
                        (self.__battery_mileage_per_dist * dist)
        assert battery_level >= 0
        self.__battery_level = battery_level
