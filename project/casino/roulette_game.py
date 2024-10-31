from typing import List, Union, Dict
from project.casino.player import Player
from project.casino.roulette import Roulette
from project.casino.casino import Casino


class Game:
    """
    A class to manage a game session between players, the roulette, and the casino.
    Handles the rounds, players' bets, and results tracking.
    """

    def __init__(
        self, players: List[Player], roulette: Roulette, casino: Casino
    ) -> None:
        """
        Initializes the Game with players, a roulette, and a casino.

        Args:
            players (List[Player]): A list of Player instances participating in the game.
            roulette (Roulette): The roulette used in the game for generating results.
            casino (Casino): The casino managing payouts and odds.
        """
        self.players: List[Player] = players
        self.roulette: Roulette = roulette
        self._current_round: int = 1
        self.round_results: List[str] = []
        self.casino: Casino = casino
        self._over: bool = False

    def get_round_data(self, round: int) -> str:
        """
        Retrieves the result of a specific round.

        Args:
            round (int): The round number.

        Returns:
            str: The result of the specified round, or an empty string if the round is not available.
        """
        if round < len(self.round_results):
            return self.round_results[round]
        else:
            return ""

    def _remove_bankrupt_players(self) -> None:
        """
        Removes players who have gone bankrupt from the game.
        """
        self.players = [player for player in self.players if not player.is_bankrupt()]

    def make_round(self) -> None:
        """
        Executes a single round of the game. Spins the roulette, collects bets, and calculates payouts.
        Updates players' balances based on the results and tracks the round outcome.
        """
        if self._over:
            return

        if len(self.players) == 0:
            self.round_results.append(
                "ROUND RESULTS "
                + str(self._current_round)
                + "\nFORTUNE WAS UNKIND TO THE PLAYERS, THE CASINO WINS!!"
            )
            self._over = True
            return

        bets: List[Dict[str, Union[List[int], int]]] = [
            player.make_turn(self._current_round) for player in self.players
        ]
        spin_result: int = self.roulette.spin()
        pays: List[int] = self.casino.match_bets(bets, spin_result)

        self.round_results.append(
            "ROUND RESULTS "
            + str(self._current_round)
            + ":\n"
            + "LANDED ON "
            + str(spin_result)
            + "\n"
        )

        for i in range(len(self.players)):
            self.players[i].change_balance(pays[i])
            self.round_results[-1] += (
                "\nPLAYER "
                + str(i + 1)
                + " BET "
                + str((bets[i]["bet"]))
                + " DOLLARS ON "
                + str((bets[i]["numbers"])).replace("[", "").replace("]", "")
                + (
                    " AND WON " + str(pays[i]) + " DOLLARS!!"
                    if pays[i] > 0
                    else " AND LOST!!"
                )
                + (
                    " THEIR BALANCE IS NOW "
                    + str(self.players[i].capital)
                    + " DOLLARS!!"
                    if self.players[i].capital > 0
                    else " THEY ARE NOW BANKRUPT!!!"
                )
            )

        self._remove_bankrupt_players()
        self._current_round += 1
