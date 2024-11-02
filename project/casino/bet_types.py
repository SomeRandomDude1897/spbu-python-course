import random
from typing import List
from enum import Enum


class HalfBets(Enum):
    """
    Enumeration for half-bets in a roulette game.
    Defines betting options: RED, BLACK, ODD, EVEN, HIGH, and LOW.
    """

    RED = "red"
    BLACK = "black"
    ODD = "odd"
    EVEN = "even"
    HIGH = "high"
    LOW = "low"


RED_NUMBERS: set[int] = {
    1,
    3,
    5,
    7,
    9,
    12,
    14,
    16,
    18,
    19,
    21,
    23,
    25,
    27,
    30,
    32,
    34,
    36,
}
BLACK_NUMBERS: set[int] = {
    2,
    4,
    6,
    8,
    10,
    11,
    13,
    15,
    17,
    20,
    22,
    24,
    26,
    28,
    29,
    31,
    33,
    35,
}
ODD_NUMBERS: set[int] = {n for n in range(1, 37) if n % 2 != 0}
EVEN_NUMBERS: set[int] = {n for n in range(1, 37) if n % 2 == 0}


class Bet:
    """
    Abstract base class for a roulette bet.
    The get_positions method should be implemented by subclasses to return
    a list of positions involved in the bet.
    """

    def get_positions(self) -> List[int]:
        raise NotImplementedError("Method must be implemented in subclass")


class AtypeBet(Bet):
    """
    Represents a single-number bet in roulette.
    Returns a single random position on the roulette wheel.
    """

    def get_positions(self) -> List[int]:
        return [random.randint(0, 36)]


class BtypeBet(Bet):
    """
    Represents a two-number bet on adjacent numbers.
    Returns the chosen position and its adjacent number based on layout.
    """

    def get_positions(self) -> List[int]:
        position: int = random.randint(0, 36)
        return (
            [position, position + 1] if position % 3 != 0 else [position - 1, position]
        )


class CtypeBet(Bet):
    """
    Represents a three-number bet in a row.
    Returns three consecutive numbers starting from a random position.
    """

    def get_positions(self) -> List[int]:
        row_start: int = random.randint(0, 36)
        return [row_start, row_start + 1, row_start + 2]


class DtypeBet(Bet):
    """
    Represents a four-number bet on a 2x2 square.
    Returns four adjacent positions if the starting position is valid.
    """

    def get_positions(self) -> List[int]:
        position: int = random.randint(0, 36)
        if position % 3 != 0 and position <= 33:
            return [position, position + 1, position + 3, position + 4]
        else:
            return self.get_positions()  # Retry if position is invalid


class EtypeBet(Bet):
    """
    Represents a six-number bet across two rows.
    Returns six consecutive numbers in two adjacent rows if starting position is valid.
    """

    def get_positions(self) -> List[int]:
        position: int = random.randint(0, 36)
        row_start: int = position // 3 * 3 + 1
        if row_start <= 31:
            return [
                row_start,
                row_start + 1,
                row_start + 2,
                row_start + 3,
                row_start + 4,
                row_start + 5,
            ]
        else:
            return self.get_positions()  # Retry if starting row is invalid


class FtypeBet(Bet):
    """
    Represents a bet on a specific column.
    Accepts a column number (1, 2, or 3) and returns positions in that column.
    """

    def __init__(self, bet_type: int) -> None:
        self.bet_type: int = bet_type

    def get_positions(self) -> List[int]:
        match self.bet_type:
            case 1:
                return [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
            case 2:
                return [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
            case 3:
                return [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
            case _:
                return []


class GtypeBet(Bet):
    """
    Represents a bet on a dozen (1-12, 13-24, 25-36).
    Accepts a dozen number (1, 2, or 3) and returns positions in that range.
    """

    def __init__(self, bet_type: int) -> None:
        self.bet_type: int = bet_type

    def get_positions(self) -> List[int]:
        match self.bet_type:
            case 1:
                return list(range(1, 13))
            case 2:
                return list(range(13, 25))
            case 3:
                return list(range(25, 37))
            case _:
                return []


class HtypeBet(Bet):
    """
    Represents a half-bet (red, black, odd, even, low, high).
    Accepts a HalfBets enum value and returns positions that match the specified type.
    """

    def __init__(self, bet_type: HalfBets) -> None:
        self.bet_type: HalfBets = bet_type

    def get_positions(self) -> List[int]:
        match self.bet_type:
            case HalfBets.RED:
                return list(RED_NUMBERS)
            case HalfBets.BLACK:
                return list(BLACK_NUMBERS)
            case HalfBets.ODD:
                return list(ODD_NUMBERS)
            case HalfBets.EVEN:
                return list(EVEN_NUMBERS)
            case HalfBets.LOW:
                return list(range(1, 19))
            case HalfBets.HIGH:
                return list(range(19, 37))
            case _:
                return []
