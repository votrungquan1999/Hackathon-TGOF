# Hackathon-TGOF
## Whispers of War
A RPG/strategy game developed in 24 hours and won at Platts-Hackathon. Team members: Naz Islam, Sida Zhang, Hung Nguyen and Quan Vo.

![Game Title](/resources/description/game_logo_shadow.png "Game Title")

### Game Concept
- A player can choose from four types of *Whispers*:
![Whispers](/resources/description/whispers_shadow.png "Four kinds of Whispers")
- Players begin at a low level, and then gain experience over the course of the game to achieve upper levels.
- The game will generate 8 cards for each player. These cards include different capabilities such as attack, speed, HP, range, and defense.
![Cards](/resources/description/cards_shadow.png "Cards")
- Players attack if an enemy exists within the range of his attack zone.
- The map has different terrain such as river, mountain, swamp, grass, where if the player goes, his range of movement will decrease. The weapon boxes and player position are generated randomly.
![Random Maps](/resources/description/map_shadow.png "Maps generated randomly")
- Each player has a randomly generated luck which represents the probability of dodging an enemy’s attack.
- Objects like weapons, cards, and potions are spread all over the map, and players can grab them by moving to the block occupying the object.
- Gaining new weapons and potions, and killing enemies will increase player’s level.
- Players will keep hitting each other until the enemy is dead.
- Once the player kills the enemy, the game will end.


### Installation:
The game is written in Python 3.7 and the graphical interface is developed using [Pygame](https://en.wikipedia.org/wiki/Pygame).
To install and play the game:

1. Clone the repository.

```
git clone https://github.com/nazislam/Hackathon-TGOF.git
```

2. Install Pygame.  

```
python3 -m pip install -U pygame --user
```

3. Run the game:  

```
python3 main_gui.py
```
