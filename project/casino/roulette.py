from typing import List
import random


class Roulette:
    """
    A standard roulette wheel class that allows spinning to get a random number between 0 and 36.
    """

    def __init__(self) -> None:
        """
        Initializes the roulette with numbers from 0 to 36.
        """
        self.allowed_variables: List[int] = list(range(37))

    def spin(self) -> int:
        """
        Spins the roulette to return a random number.

        Returns:
            int: A randomly selected number from the roulette (0-36).
        """
        return self.allowed_variables[
            random.randint(0, len(self.allowed_variables) - 1)
        ]


class CheaterRoulette(Roulette):
    """
    A roulette class that excludes 0, only allowing results from 1 to 36.
    """

    def __init__(self) -> None:
        """
        Initializes the CheaterRoulette with numbers from 1 to 36, excluding 0.
        """
        super().__init__()
        self.allowed_variables = list(range(1, 37))
