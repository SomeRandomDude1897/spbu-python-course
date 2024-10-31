import pytest
from project.casino.roulette_game import Game
from project.casino.player import *
from project.casino.roulette import *
from project.casino.casino import *


@pytest.fixture
def setup_game():
    """Фикстура для инициализации игры с игроками, рулеткой и казино."""
    players = [CautiousPlayer(100), RiskyPlayer(100), RandomPlayer(100)]
    roulette = CheaterRoulette()
    casino = GoodCasino()
    game = Game(players, roulette, casino)
    return game


def test_initial_player_capital():
    """Проверка начального капитала игрока."""
    player = Player(100)
    assert player.capital == 100


def test_player_balance_change():
    """Проверка изменения баланса игрока."""
    player = Player(100)
    player.change_balance(50)
    assert player.capital == 150
    player.change_balance(-200)
    assert player.capital == 0  # Баланс не может быть отрицательным


def test_risky_player_bet():
    """Проверка ставок игрока с высоким риском."""
    player = RiskyPlayer(100)
    bet_info = player.make_turn(1)
    assert bet_info["bet"] <= 2  # Максимальная ставка в первый раунд
    assert bet_info["numbers"] is not None


def test_random_player_bet():
    """Проверка ставок случайного игрока."""
    player = RandomPlayer(100)
    bet_info = player.make_turn(1)
    assert bet_info["bet"] <= 2  # Максимальная ставка в первый раунд
    assert bet_info["numbers"] is not None


def test_cautious_player_bet():
    """Проверка ставок осторожного игрока."""
    player = CautiousPlayer(100)
    bet_info = player.make_turn(1)
    assert bet_info["bet"] <= 1  # Максимальная ставка в первый раунд
    assert bet_info["numbers"] is not None


# хорошее казино приводит к банкротству игроков
def test_game_end_condition(setup_game):
    """Проверка условия окончания игры."""
    game = setup_game
    for _ in range(1000):  # Имитируем 10 раундов
        game.make_round()
    # Уменьшаем капитал игроков, чтобы завершить игру
    assert len(game.players) == 0  # Проверяем, что все игроки банкроты


def test_roulette_spin_result(setup_game):
    """Проверка результата вращения рулетки."""
    roulette = setup_game.roulette
    results = [roulette.spin() for _ in range(100)]  # Проверка 100 вращений
    assert all(
        result in range(37) for result in results
    )  # Все результаты должны быть в диапазоне от 0 до 36


def test_casino_payout(setup_game):
    """Проверка выплат казино."""
    casino = setup_game.casino
    bets = [{"numbers": [0], "bet": 10}, {"numbers": [1], "bet": 20}]
    results = casino.match_bets(bets, 0)  # Проверяем выплату за выигрыш
    assert results == [
        10 * casino.pay_table[len(bets[0]["numbers"])],
        0,
    ]  # Проверяем выплату для первой ставки


@pytest.mark.parametrize(
    "bet_class, expected_count",
    [
        (AtypeBet, 1),
        (BtypeBet, 2),
        (CtypeBet, 3),
        (DtypeBet, 4),
        (EtypeBet, 6),
    ],
)
def test_bet_numbers_count(bet_class, expected_count):
    """Проверка количества чисел в ставках различных типов."""
    bet_instance = bet_class()  # Создаем экземпляр класса ставки
    bet_numbers = (
        bet_instance.get_positions()
    )  # Получаем список позиций для этой ставки
    assert len(bet_numbers) == expected_count
