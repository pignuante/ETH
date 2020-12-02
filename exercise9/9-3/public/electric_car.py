#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car


class ElectricCar(Car):
    def __init__(self, battery_size: float, battery_range_km: float):
        """
        `ElectricCar`s are initiated with a `battery_size` in kilo-watt hours,
         and the range of a fully charged battery in kilometers.
         `drive` and `get_remaining_range` need to be implemented
          as well and should affect/be affected by the battery charge level.
        """
        if isinstance(battery_size, float) is False:
            raise Warning("[WARNING]battery_size must be Float type.")
        if battery_size <= 0:
            raise Warning("[WARNING]battery_size must be bigger than 0.")
        if isinstance(battery_range_km, float) is False:
            raise Warning("[WARNING]battery_range_km must be Float type.")
        if battery_range_km <= 0:
            raise Warning("[WARNING]battery_range_km must be bigger than 0.")

        self.__battery_remained = battery_size
        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km

    def get_battery_spent_per_km(self) -> float:
        # 1km 당 소비되는 배터리
        return self.__battery_size / self.__battery_range_km

    @property
    def get_dist_per_battery(self) -> float:
        # getter 괜히 한번 써봄
        # 배터리 단위용량당 갈수 있는 거리
        return self.__battery_range_km / self.__battery_size

    def get_remaining_range(self) -> float:
        return self.__battery_remained * self.get_dist_per_battery

    def drive(self, dist: float):
        if isinstance(dist, float) is False:
            raise Warning("[WARNING]Dist must be Float type.")
        if dist < 0:
            raise Warning("[WARNING]Dist must be bigger than 0.")
        spent_battery = dist * self.get_battery_spent_per_km()
        self.__battery_remained -= spent_battery
        if self.__battery_remained < 0:
            self.__battery_remained = 0
            raise Warning("[WARNING]Battery is fully depleted.")

    def charge(self, kwh: float):
        """
        The battery can be recharged with `kwh` kilo-watt hours by calling `charge`.
        Like for `CombustionCar`, over-charging should raise a `Warning`.
        """
        if isinstance(kwh, float) is False:
            raise Warning("[WARNING]KWH is not Float type.")
        if kwh < 0:  # <= ?
            raise Warning("[WARNING]KWH have to Positive.")
        self.__battery_remained += kwh
        if self.__battery_remained > self.__battery_size:
            # 최대 용량까지는 채우고, 넘친건 안채우고
            self.__battery_remained = self.__battery_size
            raise Warning("[WARNING]KWH is overfilled.")

    def get_battery_status(self) -> tuple:
        """
        Also, `get_battery_status` is very similar to the `CombustionCar` equivalent,
        and should return the current and the maximum capacity in a tuple `(c, c_max)`
        """
        return self.__battery_remained, self.__battery_size
