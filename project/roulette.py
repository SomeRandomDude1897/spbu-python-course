from typing import List, Union, Dict
import random

# Номера на рулетке (европейская рулетка)
NUMBERS: List[int] = list(range(37))  # Номера от 0 до 36

# Цвета и четность номеров
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


class Player:
    def __init__(self, capital: int) -> None:
        self.capital: int = capital

    def _get_bet_numbers(self, bet_type: str) -> List[int]:
        position: int = random.randint(0, 36)
        row_start: int = position
        match bet_type:
            case "A":
                return [position]
            case "B":
                return (
                    [position, position + 1]
                    if position % 3 != 0
                    else [position - 1, position]
                )
            case "C":
                return [row_start, row_start + 1, row_start + 2]
            case "D":
                if position % 3 != 0 and position <= 33:
                    return [position, position + 1, position + 3, position + 4]
                else:
                    return self._get_bet_numbers(bet_type)
            case "E":
                row_start = position // 3 * 3 + 1
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
                    return self._get_bet_numbers(bet_type)
            case "F 1":
                return [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
            case "F 2":
                return [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
            case "F 3":
                return [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
            case "G 1":
                return list(range(1, 13))
            case "G 2":
                return list(range(13, 25))
            case "G 3":
                return list(range(25, 37))
            case "H red":
                return list(RED_NUMBERS)
            case "H black":
                return list(BLACK_NUMBERS)
            case "H odd":
                return list(ODD_NUMBERS)
            case "H even":
                return list(EVEN_NUMBERS)
            case "H low":
                return list(range(1, 19))
            case "H high":
                return list(range(19, 37))
            case _:
                return []

    def change_balance(self, change: int) -> None:
        self.capital = max(0, self.capital + change)

    def is_bankrupt(self) -> bool:
        return self.capital == 0

    def make_turn(self, turn_number: int) -> Dict[str, Union[List[int], int]]:
        raise NotImplementedError("Этот метод должен быть реализован в подклассе")


class RiskyPlayer(Player):
    def __init__(self, capital: int):
        super().__init__(capital)
        self.possible_bets: List[str] = ["A", "B", "C", "D", "E"]

    def _get_current_bet(self, turn_number: int) -> int:
        return min(turn_number * 2, self.capital)

    def make_turn(self, turn_number: int) -> Dict[str, Union[List[int], int]]:
        self.capital -= self._get_current_bet(turn_number)
        return {
            "numbers": super()._get_bet_numbers(
                self.possible_bets[random.randint(0, len(self.possible_bets) - 1)]
            ),
            "bet": self._get_current_bet(turn_number),
        }


class RandomPlayer(Player):
    def __init__(self, capital: int):
        super().__init__(capital)
        self.possible_bets: List[str] = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "H even",
            "H odd",
            "H black",
            "H red",
            "H high",
            "H low",
            "G 1",
            "G 2",
            "G 3",
            "F 1",
            "F 2",
            "F 3",
        ]

    def _get_current_bet(self, turn_number: int) -> int:
        return min(turn_number * 2, self.capital)

    def make_turn(self, turn_number: int) -> Dict[str, Union[List[int], int]]:
        self.capital -= self._get_current_bet(turn_number)
        return {
            "numbers": super()._get_bet_numbers(
                self.possible_bets[random.randint(0, len(self.possible_bets) - 1)]
            ),
            "bet": self._get_current_bet(turn_number),
        }


class CautiousPlayer(Player):
    def __init__(self, capital: int):
        super().__init__(capital)
        self.possible_bets: List[str] = [
            "H even",
            "H odd",
            "H black",
            "H red",
            "H high",
            "H low",
            "G 1",
            "G 2",
            "G 3",
            "F 1",
            "F 2",
            "F 3",
        ]

    def _get_current_bet(self, turn_number: int) -> int:
        return min(turn_number, self.capital)

    def make_turn(self, turn_number: int) -> Dict[str, Union[List[int], int]]:
        output: Dict[str, Union[List[int], int]] = {
            "numbers": super()._get_bet_numbers(
                self.possible_bets[random.randint(0, len(self.possible_bets) - 1)]
            ),
            "bet": self._get_current_bet(turn_number),
        }
        self.capital -= self._get_current_bet(turn_number)
        return output


class Roulette:
    def __init__(self) -> None:
        self.allowed_variables: List[int] = list(range(37))

    def spin(self) -> int:
        return self.allowed_variables[
            random.randint(0, len(self.allowed_variables) - 1)
        ]


class CheaterRoulette(Roulette):
    def __init__(self) -> None:
        self.allowed_variables: List[int] = list(range(1, 37))


class Casino:
    def __init__(self):
        self.pay_table: Dict[int, int] = {18: 2, 12: 3, 6: 6, 4: 9, 3: 11, 2: 18, 1: 36}

    def match_bets(
        self, bets: List[Dict[str, Union[List[int], int]]], result: int
    ) -> List[int]:
        pays: List[int] = []
        for bet in bets:
            # Убедимся, что bet["bet"] - целое число, и numbers - список
            if (
                isinstance(bet["numbers"], list)
                and isinstance(bet["bet"], int)
                and result in bet["numbers"]
            ):
                modified_bet: int = bet["bet"] * self.pay_table[len(bet["numbers"])]
                pays.append(modified_bet)
            else:
                pays.append(0)
        return pays


class BadCasino(Casino):
    def __init__(self):
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
    def __init__(self):
        self.pay_table: Dict[int, float] = {
            18: 1.5,
            12: 2,
            6: 4,
            4: 5,
            3: 7,
            2: 9,
            1: 11,
        }


class Game:
    def __init__(
        self, players: List[Player], roulette: Roulette, casino: Casino
    ) -> None:
        self.players: List[Player] = players
        self.roulette: Roulette = roulette
        self.current_round: int = 1
        self.round_results: List[str] = []
        self.casino: Casino = casino
        self.over: bool = False

    def get_round_data(self, round: int) -> str:
        if round < len(self.round_results):
            return self.round_results[round]
        else:
            return "НЕТ ТАКОГО РАУНДА, ПРИЯТЕЛЬ"

    def kill_poor_people(self) -> None:
        self.players = [player for player in self.players if not player.is_bankrupt()]

    def make_round(self) -> None:
        if self.over:
            return
        if len(self.players) == 0:
            self.round_results.append(
                "РЕЗУЛЬТАТЫ РАУНДА "
                + str(self.current_round)
                + "\nФОРТУНА БЫЛА НЕБЛАГОСКЛОННА К ИГРОКАМ, ПОБЕДИЛО КАЗИНО!!"
            )
            self.over = True
            return
        bets: List[Dict[str, Union[List[int], int]]] = [
            player.make_turn(self.current_round) for player in self.players
        ]
        spin_result: int = self.roulette.spin()
        pays: List[int] = self.casino.match_bets(bets, spin_result)

        self.round_results.append(
            "РЕЗУЛЬТАТЫ РАУНДА "
            + str(self.current_round)
            + " : \n"
            + "ВЫПАЛО "
            + str(spin_result)
            + "\n"
        )

        for i in range(len(self.players)):
            self.players[i].change_balance(pays[i])
            self.round_results[-1] += (
                "\n ИГРОК "
                + str(i + 1)
                + " СТАВИЛ "
                + str((bets[i]["bet"]))
                + " ДОЛЛАРОВ НА "
                + str((bets[i]["numbers"])).replace("[", "").replace("]", "")
                + (
                    " И ВЫИГРАЛ " + str(pays[i]) + " ДОЛЛАРОВ!!"
                    if pays[i] > 0
                    else " И ПРОСЧИТАЛСЯ!!"
                )
                + (
                    " ТЕПЕРЬ ЕГО СОСТОЯНИЕ СОСТАВЛЯЕТ "
                    + str(self.players[i].capital)
                    + " ДОЛЛАРОВ!!"
                    if self.players[i].capital > 0
                    else " ТЕПЕРЬ ОН БАНКРОТ!!!"
                )
            )
        self.kill_poor_people()
        self.current_round += 1


game = Game(
    [
        CautiousPlayer(100),
        CautiousPlayer(100),
        CautiousPlayer(100),
        RiskyPlayer(100),
        RandomPlayer(100),
    ],
    CheaterRoulette(),
    GoodCasino(),
)
for i in range(100):
    game.make_round()
    print(game.get_round_data(i))
