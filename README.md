# Snake Game 🐍

A simple Snake Game built in Python using the `turtle` graphics library.  
The snake moves around the screen, eats food to grow longer, and the score increases.  
The game ends if the snake collides with the wall or with its own tail.  

## Features
- Classic Snake mechanics (move, eat, grow, die).
- Scoreboard with live score tracking.
- Randomly spawning food items.
- Collision detection with walls and tail.
- Clean OOP structure (`Snake`, `Food`, `Scoreboard` classes).

## 🏆 Persistent High Score Storage

Nobody likes losing their bragging rights when they close the game. To fix that, this Snake implementation saves the highest score across sessions using a simple file-based system.

Here’s how it works under the hood:

When the game starts, it reads the previous high score from data.txt.

During gameplay, your score is compared against the stored high score.

If you beat it, the new high score is immediately saved back to data.txt — meaning your glory lives on even after you quit.

It’s lightweight, effective, and gives players that satisfying “my record is safe” feeling every time they come back.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/martialchess/Snake-Game-OOP.git

2. Navigate into the project folder:
   cd snake-game

3. Run the game
   python main.py
