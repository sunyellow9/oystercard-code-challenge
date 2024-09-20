from oystercard import OysterCard
from travel_mode import TravelMode
from constants import Modes, Stations, Fares
from travel_station import TravelStation


class TestOysterCard:

    def test_inadequate_balance(self):
        # Load card with £1
        oysetercard = OysterCard(1)
        assert oysetercard.getBalance() == 1

        # Swipe in at HOLBORN for a TUBE ride
        message = oysetercard.swipeIn(
            Stations.HOLBORN.value, TravelMode(Modes.TUBE))
        assert message == "You don't have enough balance for the trip"

        # Swipe in at EARL'S COURT for a BUS ride
        message = oysetercard.swipeIn(
            Stations.EARLS_COURT.value, TravelMode(Modes.BUS))
        assert message == "You don't have enough balance for the trip"

    def test_swipein_only_tube(self):
        # Load card with £30
        oysetercard = OysterCard(30)
        assert oysetercard.getBalance() == 30

        # Swipe in at HOLBORN, without swiping out
        oysetercard.swipeIn(Stations.HOLBORN.value, TravelMode(Modes.TUBE))

        # Expected balance £30 - £3.20 = £26.80
        expected_balance = 30 - Fares.MAX_FARE.value
        assert oysetercard.getBalance() == expected_balance

    def test_swipein_only_bus(self):
        # Load card with £30
        oysetercard = OysterCard(30)
        assert oysetercard.getBalance() == 30

        # Swipe in at EARL'S COURT for BUS trip, without swiping out
        oysetercard.swipeIn(Stations.HOLBORN.value, TravelMode(Modes.BUS))

        # Expected balance £30 - £1.80 = £28.20
        expected_balance = 30 - Fares.ANY_BUS_TRIP.value
        assert oysetercard.getBalance() == expected_balance

    def test_swipeout_only_tube(self):
        # Load card with £30
        oysetercard = OysterCard(30)
        assert oysetercard.getBalance() == 30

        # Swipe out at EARL'S COURT
        oysetercard.swipeOut(Stations.EARLS_COURT.value,
                             TravelMode(Modes.TUBE))

        # Expected balance £30 - £3.20 = £26.80
        expected_balance = 30 - Fares.MAX_FARE.value
        assert oysetercard.getBalance() == expected_balance

    def test_swipeout_only_bus(self):
        # Load card with £30
        oysetercard = OysterCard(30)
        assert oysetercard.getBalance() == 30

        # Swipe out at Chelsea after a BUS trip, without swiping in
        oysetercard.swipeOut(Stations.EARLS_COURT.value,
                             TravelMode(Modes.BUS))

        # Expected balance £30 - £1.80 = £28.20
        expected_balance = 30 - Fares.ANY_BUS_TRIP.value
        assert oysetercard.getBalance() == expected_balance

    def test_holborn_to_hammersmith(self):
        # Load card with £30
        oysetercard = OysterCard(30)
        assert oysetercard.getBalance() == 30

        # Swipe in at HOLBORN and out at EARL'S COURT
        oysetercard.swipeIn(Stations.HOLBORN.value, TravelMode(Modes.TUBE))
        oysetercard.swipeOut(Stations.EARLS_COURT.value,
                             TravelMode(Modes.TUBE))

        # Expected balance £30 - £2.50 = £27.50
        expected_balance = 30 - Fares.ANYWHERE_IN_ZONE1.value
        assert oysetercard.getBalance() == expected_balance

        # Swipe in at EARL'S COURT for a bus trip to Chelsea
        oysetercard.swipeIn(Stations.EARLS_COURT.value, TravelMode(Modes.BUS))
        oysetercard.swipeOut(TravelStation(
            "Chelsea", []), TravelMode(Modes.BUS))

        # Expected balance £30 - (£2.50 - £1.80) = £25.70
        expected_balance = 30 - Fares.ANYWHERE_IN_ZONE1.value - \
            Fares.ANY_BUS_TRIP.value
        assert oysetercard.getBalance() == expected_balance

        # Swipe in at EARL'S COURT and out at HAMMERSMITH
        oysetercard.swipeIn(Stations.EARLS_COURT.value, TravelMode(Modes.TUBE))
        oysetercard.swipeOut(Stations.HAMMERSMITH.value,
                             TravelMode(Modes.TUBE))

        # Expected balance £30 - (£2.50 - £1.80 - £2.00) = £23.70
        expected_balance = 30 - Fares.ANYWHERE_IN_ZONE1.value - \
            Fares.ANY_BUS_TRIP.value - Fares.ONE_ZONE_OUTSIDE_ZONE1.value
        assert oysetercard.getBalance() == expected_balance
