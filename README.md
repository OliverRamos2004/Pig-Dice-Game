# Pig Dice Game 🐷🎲

A Python-based implementation of the "Pig" dice game. In this game, players take turns to roll a die and accumulate points while avoiding rolling a 1. The first player to reach 50 points wins, but other players can finish their turns to keep the game fair.

## Table of Contents
- [Game Rules](#game-rules)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Future Enhancements](#future-enhancements)

## Game Rules
1. **Players:** 2 to 4 players.
2. **Objective:** Be the first player to reach 50 points.
3. **Gameplay:**
   - Each player rolls a die (1-6).
   - Rolling a number other than 1 adds the number to the player's turn score.
   - If the player rolls a 1, they lose all points for that turn, and the turn ends.
   - Players can choose to hold (not roll), adding their turn score to their overall score.
   - Once a player reaches 50 points, other players are allowed to finish their turns before declaring the winner.

## Features
- **Randomized Dice Rolls:** Simulated die rolls using Python’s `random` library.
- **Multiple Players:** Supports 2 to 4 players.
- **Fair Play:** After one player reaches the winning score, all others are allowed to finish their turns to prevent an unfair advantage.
- **Input Validation:** Ensures only valid inputs (player count, roll decisions) are accepted.

## Technologies Used
- **Python:** The game is entirely written in Python, utilizing core libraries.

## How to Play
1. **Clone this repository:**
    ```bash
    git clone https://github.com/OliverRamos2004/Pig-Dice-Game.git
    cd pig-dice-game
    ```

2. **Run the game:**
    ```bash
    python pig_dice_game.py
    ```

3. **Follow the prompts:**
   - Enter the number of players (2 to 4).
   - Players take turns rolling the dice by entering `y` to roll or holding to save their score for that round.

## Installation
1. Make sure you have [Python](https://www.python.org/downloads/) installed on your machine.
2. Clone this repository using Git.
3. Run the script to start playing.

## Future Enhancements
- Add a graphical user interface (GUI) to make the game more interactive.
- Allow customization of the target score and number of dice.
- Implement multiplayer support over the network.
