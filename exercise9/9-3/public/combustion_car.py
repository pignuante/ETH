#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car


class CombustionCar(Car):
    def __init__(self, gas_capacity: float, gas_per_100km: float):
        """
        `CombustionCar`s are initiated with the `gas_capacity` in liters and `gas_per_100km`
        that describes the fuel consumption.
        To make a `CombustionCar` usable,
        the two abstract methods `get_remaining_range` and `drive` need to be implemented.
        """
        if isinstance(gas_capacity, float) is False:
            raise Warning("[WARNING]gas_capacity must be Float type.")
        if gas_capacity <= 0:
            raise Warning("[WARNING]gas_capacity must be bigger than 0.")
        if isinstance(gas_per_100km, float) is False:
            raise Warning("[WARNING]gas_per_100km must be Float type.")
        if gas_per_100km <= 0:
            raise Warning("[WARNING]gas_per_100km must be bigger than 0.")

        self.__gas_remained = gas_capacity
        self.__GAS_CAPACITY = gas_capacity  # const
        self.__GAS_PER_100KM = gas_per_100km  # 100km를 nL로 이동

    def get_gas_spent_per_km(self) -> float:
        """
        1km 가는데 필요한 연료량
        """
        return self.__GAS_PER_100KM / 100

    def get_dist_per_gas(self) -> float:
        """
        연료 1당 이동 가능한  km
        """
        return 100 / self.__GAS_PER_100KM

    def get_remaining_range(self) -> float:
        """
        지금 가진 연료로 이동 가능한 거리
            남은 연료 * get_dist_per_gas
        """
        return self.__gas_remained * self.get_dist_per_gas()

    def drive(self, dist: float):
        """
        On use, `drive` should remove the correct amount of gas from the gas tank,
        and it should raise a `Warning` if the gas tank is fully depleted through driving
        """
        if isinstance(dist, float) is False:
            raise Warning("[WARNING]Dist must be Float type.")
        if dist < 0:
            raise Warning("[WARNING]Dist must be bigger than 0.")
        remained_range = self.get_remaining_range()
        spent_fuel = dist * self.get_gas_spent_per_km()
        self.__gas_remained -= spent_fuel

        if self.__gas_remained < 0:
            # 갈 수 있는 거리보다 더 갔으면 최대한으로 가고 멈춘다
            self.__gas_remained = 0
            raise Warning("[WARNING]Gas tank is fully depleted.")

    def fuel(self, f: float):
        """
         The car can be refueled using `fuel`,
          which adds `f` liters of fuel to the gas tank.
          The method should raise a `Warning`, if the gas tank gets overfilled
        """
        if isinstance(f, float) is False:
            raise Warning("[WARNING]Fuel is not Float type.")
        if f < 0:  # <= ?
            raise Warning("[WARNING]Fuel have to Positive.")
        self.__gas_remained += f
        if self.__gas_remained > self.__GAS_CAPACITY:
            # 최대 용량까지는 채우고 넘친건 안채우고
            self.__gas_remained = self.__GAS_CAPACITY
            raise Warning("[WARNING]Fuel is overfilled.")

    def get_gas_tank_status(self) -> tuple:
        """
        A call to `get_gas_tank_status` returns the current gas tank capacity `c` and the maximum capacity `c_max`
        as a tuple `(c, c_max)`. It must always be that 0 <= c <= c_max
        """
        return self.__gas_remained, self.__GAS_CAPACITY
