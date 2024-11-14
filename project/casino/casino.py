from typing import List, Union, Dict
from bet_data_enum import BetParams


class Casino:
    """
    Base class representing a casino with a payout table for different types of bets.
    """

    def __init__(self):
        # Payouts based on the number of numbers bet on.
        self.pay_table: Dict[int, int] = {18: 2, 12: 3, 6: 6, 4: 9, 3: 11, 2: 18, 1: 36}
        # тут коэффициент выигрыша + 1,
        # потому что это изначальное число денег умножить на коэффициент,
        # могу переписать чтобы отнимала единичку, но зачем
        # еще в пулл реквес те в комменте указать

    def match_bets(
        self, bets: List[Dict[str, Union[List[int], int]]], result: int
    ) -> List[int]:
        """
        Evaluates each bet in the list to determine payouts based on the result number.

        Args:
            bets (List[Dict[str, Union[List[int], int]]]): List of bets. Each bet dictionary
                contains "numbers" (list of bet numbers) and "bet" (amount bet).
            result (int): The winning number to match against the bet numbers.

        Returns:
            List[int]: A list of payouts for each bet.
        """
        pays: List[int] = []
        for bet in bets:
            print(bet)
            if (
                isinstance(bet[BetParams.NUMBERS], list)
                and isinstance(bet[BetParams.BET], int)
                and result in bet[BetParams.NUMBERS]
            ):
                modified_bet: int = (
                    bet[BetParams.BET] * self.pay_table[len(bet[BetParams.NUMBERS])]
                )
                pays.append(modified_bet)
            else:
                pays.append(0)
        return pays


class BadCasino(Casino):
    """
    Represents a casino with a higher payout table than the base Casino class.
    """

    def __init__(self):
        super().__init__()
        # Higher payouts than standard Casino for each set of numbers.
        self.pay_table: Dict[int, int] = {
            18: 4,
            12: 6,
            6: 12,
            4: 18,
            3: 22,
            2: 36,
            1: 72,
        }


class GoodCasino(Casino):
    """
    Represents a casino with a lower payout table than the base Casino class.
    """

    def __init__(self):
        super().__init__()
        # Lower payouts than standard Casino for each set of numbers.
        self.pay_table: Dict[int, float] = {
            18: 1.5,
            12: 2,
            6: 4,
            4: 5,
            3: 7,
            2: 9,
            1: 11,
        }
