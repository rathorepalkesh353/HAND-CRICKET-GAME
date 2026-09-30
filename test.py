"""
Unit tests for Hand Cricket game engine.
"""

from src.game import determine_winner, play_turn


def test_play_turn_not_out():
    is_out, runs = play_turn(batter_val=6, bowler_val=4)
    assert is_out is False
    assert runs == 6


def test_play_turn_out():
    is_out, runs = play_turn(batter_val=5, bowler_val=5)
    assert is_out is True
    assert runs == 0


def test_determine_winner_player1():
    result = determine_winner(player1_runs=25, player2_runs=18)
    assert result == "Player 1 WINS!"


def test_determine_winner_player2():
    result = determine_winner(player1_runs=12, player2_runs=19)
    assert result == "Player 2 WINS!"


def test_determine_winner_tie():
    result = determine_winner(player1_runs=15, player2_runs=15)
    assert result == "It's a TIE!"