from travel_mode import TravelMode
from constants import Fares, Modes
from travel_station import TravelStation
from tube_travel import TubeTravel


class OysterCard():

    def __init__(self, amount) -> None:
        self.start_station = None
        self.exit_station = None
        self.balance = amount

    def getBaseFare(self, travelmode: TravelMode) -> float:
        """
        Gets the base fare for a travel mode

        Args:
            travelmode (TravelMode): The mode of travel, tube or bus
        Return:
            float: The base fare of the travel mode.
        """
        base_fares = {
            Modes.BUS: Fares.ANY_BUS_TRIP.value,
            Modes.TUBE: Fares.MAX_FARE.value
        }
        fare_value = base_fares.get(travelmode.type)
        if fare_value == None:
            raise ValueError("Invalid Travel Mode")
        return fare_value

    def swipeIn(self, station: TravelStation, travelmode: TravelMode) -> str:
        """
        Handles the "Swipe In" event at the station barriers

        Args:
            station (TravelStation): The station where the event is taking place
            travelmode (TravelMode): The mode of travel, tube or bus
        Return:
            str: The outcome of the swipe in event.
        """
        self.fare_value = self.getBaseFare(travelmode)

        if (self.balance < self.fare_value):
            return "You don't have enough balance for the trip"

        self.balance = self.balance - self.fare_value
        self.start_station = station

        return f"Welcome to {station.name} station! Enjoy your trip."

    def swipeOut(self, station: TravelStation, travelmode: TravelMode) -> str:
        """
        Handles the "Swipe Out" event at the station barriers

        Args:
            station (TravelStation): The station where the event is taking place
            travelmode (TravelMode): The mode of travel, tube or bus
        Return:
            str: The outcome of the swipe out event.
        """
        self.exit_station = station
        base_fare = self.getBaseFare(travelmode)

        if (travelmode.type == Modes.TUBE):
            if self.start_station:
                tube_travel = TubeTravel(self.start_station, self.exit_station)
                self.fare_value = tube_travel.getCost()
                self.balance = (
                    self.balance + base_fare) - self.fare_value
            else:
                self.balance = self.balance - base_fare

        if (travelmode.type == Modes.BUS):
            if not self.start_station:
                self.balance = self.balance - base_fare

        return f"Goodbye! Exit at {station.name} station."

    def getBalance(self) -> float:
        """
        Returns the balance in an Oyster Card

        Return:
            float: The Oyster Card balance.
        """
        return self.balance

    def topUpCard(self, amount: float) -> float:
        """
        Loads money into the Oyster Card

        Args:
            amount (float): The amount to load in the card
        Return:
            float: The Oyster Card balance.
        """
        self.balance = self.balance + amount
        return self.balance
