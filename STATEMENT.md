# Problem Statement: Hand Cricket Console Game

## Objective
Design and implement a two-player command-line game simulating the rules of classical **Hand Cricket**.

## Game Mechanics & Rules
1. **First Innings (Player 1 Batting):**
   - Player 1 inputs a number representing their score choice per ball.
   - Player 2 inputs a number representing their bowling choice per ball.
   - If Player 1's choice equals Player 2's choice, Player 1 is **OUT**, ending the first innings.
   - Otherwise, Player 1 adds their chosen number to their total score.

2. **Second Innings (Player 2 Batting):**
   - Player 2 now bats, entering their score per ball, while Player 1 bowls.
   - If Player 2's choice equals Player 1's choice, Player 2 is **OUT**, ending the game.
   - Otherwise, Player 2 adds their chosen number to their total score.

3. **Winning Conditions:**
   - **Player 1 Wins:** If Player 1's score > Player 2's score.
   - **Player 2 Wins:** If Player 2's score > Player 1's score.
   - **Tie:** If both players finish with equal runs.

## Technical Specifications
- Built with standard Python 3.x.
- Modular functional architecture allowing core game logic to be unit tested without requiring interactive user inputs.
- Continuous input validation to handle integers cleanly during gameplay.