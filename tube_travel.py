from itertools import product
from travel_station import TravelStation
from constants import Fares, Zone


class TubeTravel():
    def __init__(self, start_station: TravelStation, exit_station: TravelStation) -> None:
        self.start_zone = start_station.zone
        self.exit_zone = exit_station.zone

    def travelled_zones_count(self) -> int:
        """
        Counts the number of zones travelled between the start and end station

        Return:
            int: The number of zones travelled
        """
        zones_combinations = list(
            # Creates a combinations of the zones, e.g., [(1, 2), (2, 2)] for Earl’s Court to Hammersmith
            product(self.start_zone, self.exit_zone))

        zones_difference = [abs(x - y) for x, y in zones_combinations]
        zones_count = min(zones_difference) + 1
        return zones_count

    def zone_one_included(self) -> bool:
        """
        Checks if Zone 1 is in either the start or end zone.

        Return:
            bool: True or False
        """
        zone_one = Zone.ONE.value
        return zone_one in self.start_zone or zone_one in self.exit_zone

    def exit_zone_one(self) -> bool:
        """
        Checks if swipe out at Zone 1

        Return:
            bool: True or False
        """
        zone_one = Zone.ONE.value
        return zone_one in self.exit_zone

    def getCost(self) -> float:
        """
        Calculate the real cost of the fare between the start and end station.

        Return:
            float: The cost of the travel between the start and end station.
        """
        num_zones_travelled = self.travelled_zones_count()

        if num_zones_travelled == 3:
            return Fares.THREE_ZONES.value

        if num_zones_travelled == 2:
            if self.zone_one_included():
                return Fares.TWO_ZONES_INCLUDING_ZONE1.value
            else:
                return Fares.TWO_ZONES_EXCLUDING_ZONE1.value

        if num_zones_travelled == 1:
            if self.exit_zone_one():
                return Fares.ANYWHERE_IN_ZONE1.value
            else:
                return Fares.ONE_ZONE_OUTSIDE_ZONE1.value

        return Fares.MAX_FARE.value
