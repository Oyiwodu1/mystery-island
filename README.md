# Mystery Island — The Lost Lighthouse

An interactive Python command-line text adventure where players explore a mysterious island, collect useful objects, overcome obstacles, and restore a lighthouse beacon to escape.

## Project Status

Core gameplay implemented. 26 automated tests passing. Final documentation and review in progress.

## Game Objective

You wake up on Mystery Island after a storm. The lighthouse beacon is dark, and a rescue boat will only arrive when you restore it.

Explore the island, find the objects you need, solve obstacles, manage your energy, and restore the lighthouse before you run out of energy.

## Game Rules

- You start with **5 energy points**.
- Moving between connected locations costs 1 energy point.
- Searching a location does not cost energy.
- You can collect each object only once.
- The rope is found in the Jungle and is required to cross the Old Bridge.
- The Cave Guardian requires you to solve a riddle before entering the Cave.
- A wrong answer to the Cave Guardian's riddle costs 1 energy point.
- The lantern is found in the Cave and is required to restore the lighthouse beacon.
- The hidden treasure is also found in the Cave and rewards you with 2 extra energy points.
- Treasure can only be collected once.
- Your energy cannot exceed **7 points**.
- Random encounters may happen while travelling. There is a 60% chance of an encounter after successful movement.
- Random encounters have five possible outcomes:
  - **Wild animal:** Lose 1 energy point.
  - **Abandoned food:** Gain 1 energy point.
  - **Helpful stranger:** Receive a useful clue.
  - **Sudden storm:** Lose 1 energy point.
  - **Quiet journey:** No effect.
- You can revisit previous locations.
- If your energy reaches zero before restoring the lighthouse beacon, you lose.
- After winning or losing, you can choose to play again.

## Island Locations

The island has five connected locations:

1. **Beach** — Starting location.
2. **Jungle** — Contains the rope.
3. **Cave** — Contains the Cave Guardian, lantern, and hidden treasure.
4. **Old Bridge** — Requires the rope to cross.
5. **Lighthouse** — Requires the lantern to restore the beacon and win the game.

## Technologies

- Python 3.12
- Python standard library
- `unittest` for automated testing

No third-party packages are required.

## Project Structure

```text
mystery-island/
├── tests/
│   └── test_game.py
├── main.py
├── game.py
├── README.md
└── .gitignore
```

- `main.py` — Game entry point, menu, player interaction, map display, and replay functionality.
- `game.py` — Core game logic, player state, movement, item collection, Cave Guardian, random encounters, and beacon restoration.
- `tests/test_game.py` — Automated tests for the game logic.
- `.gitignore` — Files and directories Git should ignore.

## Requirements

- Python 3.12 or a compatible Python 3 version.
- A terminal or command-line interface.

Check your Python version:

```bash
python3 --version
```

## How to Run

1. Clone the repository or download the project.
2. Open a terminal in the project directory.
3. Start the game:

```bash
python3 main.py
```

Follow the on-screen instructions and menu options to play.

## How to Run Tests

From the project root directory, run:

```bash
python3 -m unittest discover -s tests -v
```

The automated tests cover:

- Player initialization and default values.
- Successful and invalid movement.
- Bridge access requirements.
- Energy deduction and game-over conditions.
- Item collection and duplicate prevention.
- Hidden treasure rewards and maximum energy limits.
- Cave Guardian answers and energy penalties.
- Random encounter outcomes and probability.
- Random encounter energy limits.
- Lighthouse restoration and winning conditions.

## Project Limitations

- The game runs entirely in the command line.
- The island uses a fixed map and predefined locations.
- Player progress is not saved between game sessions.
- The game uses simple text-based interactions.
- Random encounters use predefined outcomes.

## Author

Created as a Python programming project to practice functions, dictionaries, conditionals, loops, modular programming, randomization, and automated testing.