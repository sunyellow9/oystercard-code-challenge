from enum import Enum

from travel_station import TravelStation


class Stations(Enum):
    HOLBORN = TravelStation("Holborn", [1])
    EARLS_COURT = TravelStation("Earl's Court", [1, 2])
    HAMMERSMITH = TravelStation("Hammersmith", [2])
    WIMBLEDON = TravelStation("Wimbledon", [3])


class Fares(Enum):
    MAX_FARE = 3.20
    ANYWHERE_IN_ZONE1 = 2.50
    ONE_ZONE_OUTSIDE_ZONE1 = 2.00
    TWO_ZONES_INCLUDING_ZONE1 = 3.00
    TWO_ZONES_EXCLUDING_ZONE1 = 2.25
    THREE_ZONES = 3.20
    ANY_BUS_TRIP = 1.80


class Modes(Enum):
    BUS = "BUS"
    TUBE = "TUBE"


class Zone(Enum):
    ONE = 1
