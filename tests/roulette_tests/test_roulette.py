import pytest
from project.roulette import (
    Player,
    RiskyPlayer,
    RandomPlayer,
    CautiousPlayer,
    Roulette,
    Casino,
    Game,
    CheaterRoulette,
    GoodCasino,
)


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


def test_game_end_condition(setup_game):
    """Проверка условия окончания игры."""
    game = setup_game
    for _ in range(10):  # Имитируем 10 раундов
        game.make_round()
    # Уменьшаем капитал игроков, чтобы завершить игру
    for player in game.players:
        player.capital = 0
    game.kill_poor_people()  # Удаляем банкротов
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
    "bet_type, expected_count",
    [
        ("A", 1),
        ("B", 2),
        ("C", 3),
        ("D", 4),
        ("E", 6),
    ],
)
def test_bet_numbers_count(bet_type, expected_count):
    """Проверка количества чисел в ставках."""
    player = Player(100)
    bet_numbers = player._get_bet_numbers(bet_type)
    assert len(bet_numbers) == expected_count
