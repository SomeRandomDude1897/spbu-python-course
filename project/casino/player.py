from typing import List, Union, Dict
from bet_types import *
import random
from bet_data_enum import bet_types


class Player:
    """
    Base class representing a player with capital and general methods for handling balance.
    """

    def __init__(self, capital: int) -> None:
        """
        Initializes the Player with a specified amount of capital.

        Args:
            capital (int): Initial capital for the player.
        """
        self.capital: int = capital

    def change_balance(self, change: int) -> None:
        """
        Modifies the player's capital by a given amount, ensuring it does not drop below zero.

        Args:
            change (int): Amount to change in the player's balance (positive or negative).
        """
        self.capital = max(0, self.capital + change)

    def is_bankrupt(self) -> bool:
        """
        Checks if the player is bankrupt.

        Returns:
            bool: True if the player's capital is zero, otherwise False.
        """
        return self.capital == 0

    def make_turn(self, turn_number: int) -> Dict[str, Union[List[int], int]]:
        """
        Abstract method to be implemented by subclasses, defining how the player makes a bet.

        Args:
            turn_number (int): The current turn number in the game.

        Returns:
            Dict[str, Union[List[int], int]]: Dictionary with "numbers" (positions bet on) and "bet" (amount).
        """
        raise NotImplementedError("Method must be created in subclass")


class RiskyPlayer(Player):
    """
    A type of player who makes riskier bets with a strategy of increasing bet amounts.
    """

    def __init__(self, capital: int):
        """
        Initializes the RiskyPlayer with specific bet types.

        Args:
            capital (int): Initial capital for the player.
        """
        super().__init__(capital)
        self.possible_bets = [
            AtypeBet(),
            BtypeBet(),
            CtypeBet(),
            EtypeBet(),
            DtypeBet(),
        ]

    def _get_current_bet(self, turn_number: int) -> int:
        """
        Determines the current bet amount based on the turn number, scaling it by 2 each turn.

        Args:
            turn_number (int): The current turn number.

        Returns:
            int: The bet amount, constrained by the player's remaining capital.
        """
        return min(turn_number * 2, self.capital)

    def make_turn(self, turn_number: int) -> Dict[str, Union[List[int], int]]:
        """
        Places a bet by selecting a random bet type and deducting the bet amount from capital.

        Args:
            turn_number (int): The current turn number.

        Returns:
            Dict[str, Union[List[int], int]]: Bet details, including chosen numbers and bet amount.
        """
        self.capital -= self._get_current_bet(turn_number)
        return {
            bet_types.NUMBERS: self.possible_bets[
                random.randint(0, len(self.possible_bets) - 1)
            ].get_positions(),
            bet_types.BET: self._get_current_bet(turn_number),
        }


class RandomPlayer(Player):
    """
    A player who bets on random numbers and amounts in a wider range of betting options.
    """

    def __init__(self, capital: int):
        """
        Initializes the RandomPlayer with various bet types.

        Args:
            capital (int): Initial capital for the player.
        """
        super().__init__(capital)
        self.possible_bets = [
            AtypeBet(),
            AtypeBet(),
            BtypeBet(),
            CtypeBet(),
            EtypeBet(),
            DtypeBet(),
            FtypeBet(1),
            FtypeBet(2),
            FtypeBet(3),
            GtypeBet(1),
            GtypeBet(2),
            GtypeBet(3),
            HtypeBet(HalfBets.RED),
            HtypeBet(HalfBets.BLACK),
            HtypeBet(HalfBets.ODD),
            HtypeBet(HalfBets.EVEN),
            HtypeBet(HalfBets.LOW),
            HtypeBet(HalfBets.HIGH),
        ]

    def _get_current_bet(self, turn_number: int) -> int:
        """
        Calculates the current bet amount, doubling each turn, constrained by capital.

        Args:
            turn_number (int): The current turn number.

        Returns:
            int: The bet amount for this turn.
        """
        return min(turn_number * 2, self.capital)

    def make_turn(self, turn_number: int) -> Dict[str, Union[List[int], int]]:
        """
        Randomly selects a bet type and deducts the bet amount from capital.

        Args:
            turn_number (int): The current turn number.

        Returns:
            Dict[str, Union[List[int], int]]: Dictionary containing chosen numbers and bet amount.
        """
        self.capital -= self._get_current_bet(turn_number)
        return {
            bet_types.NUMBERS: self.possible_bets[
                random.randint(0, len(self.possible_bets) - 1)
            ].get_positions(),
            bet_types.BET: self._get_current_bet(turn_number),
        }


class CautiousPlayer(Player):
    """
    A player who makes more conservative bets, betting smaller amounts over time.
    """

    def __init__(self, capital: int):
        """
        Initializes the CautiousPlayer with a selection of safe bet types.

        Args:
            capital (int): Initial capital for the player.
        """
        super().__init__(capital)
        self.possible_bets = [
            FtypeBet(1),
            FtypeBet(2),
            FtypeBet(3),
            GtypeBet(1),
            GtypeBet(2),
            GtypeBet(3),
            HtypeBet(HalfBets.RED),
            HtypeBet(HalfBets.BLACK),
            HtypeBet(HalfBets.ODD),
            HtypeBet(HalfBets.EVEN),
            HtypeBet(HalfBets.LOW),
            HtypeBet(HalfBets.HIGH),
        ]

    def _get_current_bet(self, turn_number: int) -> int:
        """
        Sets a cautious betting amount, increasing more slowly than other player types.

        Args:
            turn_number (int): The current turn number.

        Returns:
            int: The bet amount for this turn.
        """
        return min(turn_number, self.capital)

    def make_turn(self, turn_number: int) -> Dict[str, Union[List[int], int]]:
        """
        Selects a bet type and deducts the bet amount from capital.

        Args:
            turn_number (int): The current turn number.

        Returns:
            Dict[str, Union[List[int], int]]: Dictionary containing chosen numbers and bet amount.
        """
        output: Dict[str, Union[List[int], int]] = {
            bet_types.NUMBERS: self.possible_bets[
                random.randint(0, len(self.possible_bets) - 1)
            ].get_positions(),
            bet_types.BET: self._get_current_bet(turn_number),
        }
        self.capital -= self._get_current_bet(turn_number)
        return output
