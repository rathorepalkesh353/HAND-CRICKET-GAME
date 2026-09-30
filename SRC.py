"""
Hand Cricket Game Core Engine.
"""


def play_turn(batter_val: int, bowler_val: int) -> tuple[bool, int]:
    """
    Evaluates a single ball in Hand Cricket.

    :param batter_val: Runs chosen by the batting player.
    :param bowler_val: Number chosen by the bowling player.
    :return: Tuple (is_out, runs_scored). If out, runs_scored is 0.
    """
    if batter_val == bowler_val:
        return True, 0
    return False, batter_val


def play_innings(batter_name: str, bowler_name: str) -> int:
    """
    Runs an innings for the batting player until they get out.

    :param batter_name: Name of the player batting.
    :param bowler_name: Name of the player bowling.
    :return: Total runs accumulated in the innings.
    """
    runs = 0
    print(f"\n{batter_name} is batting! ({bowler_name} is bowling)")
    print("-" * 35)

    while True:
        try:
            p1_input = int(input(f"{batter_name} fingers: "))
            p2_input = int(input(f"{bowler_name} fingers: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if batter_name == "Player 1":
            batter_val, bowler_val = p1_input, p2_input
        else:
            batter_val, bowler_val = p2_input, p1_input

        is_out, scored = play_turn(batter_val, bowler_val)

        if is_out:
            print(f"OUT! {batter_name} is out!")
            break

        runs += scored
        print(f"{batter_name} Score: {runs}")

    print("-" * 35)
    return runs


def determine_winner(player1_runs: int, player2_runs: int) -> str:
    """
    Determines the final outcome based on scores.

    :param player1_runs: Total runs of Player 1.
    :param player2_runs: Total runs of Player 2.
    :return: Result string message.
    """
    if player1_runs > player2_runs:
        return "Player 1 WINS!"
    elif player2_runs > player1_runs:
        return "Player 2 WINS!"
    return "It's a TIE!"


def main():
    """Main execution entry point."""
    print("====================================")
    print("      WELCOME TO HAND CRICKET       ")
    print("====================================")

    player1_runs = play_innings("Player 1", "Player 2")
    player2_runs = play_innings("Player 2", "Player 1")

    print("\nFINAL SCORES:")
    print(f"Player 1: {player1_runs} runs")
    print(f"Player 2: {player2_runs} runs")
    print("-" * 35)
    print(determine_winner(player1_runs, player2_runs))


if __name__ == "__main__":
    main()