# Mystery Island — The Lost Lighthouse

An interactive Python command-line text adventure where players explore a mysterious island, collect useful objects, overcome obstacles, and restore a lighthouse beacon to escape.

## Project Status

Core gameplay implemented. Automated tests passing. Documentation and final review in progress.

## Game Objective

You wake up on Mystery Island after a storm. The lighthouse beacon is dark, and a rescue boat will only arrive when you restore it.

Explore the island, find the objects you need, manage your energy, and restore the lighthouse before you run out of energy.

## Game Rules

- You start with **5 energy points**.
- Moving between connected locations costs 1 energy point.
- Searching a location does not cost energy.
- You can collect each object only once.
- The rope is found in the Jungle and is required to cross the Old Bridge.
- The lantern is found in the Cave and is required to restore the lighthouse beacon.
- You can revisit previous locations.
- If your energy reaches zero before restoring the lighthouse beacon, you lose.
- After winning or losing, you can choose to play again.

## Island Locations

The island has five connected locations:

1. Beach
2. Jungle — contains the rope.
3. Cave — contains the lantern.
4. Old Bridge — requires the rope.
5. Lighthouse — requires the lantern to restore the beacon.

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

- `main.py` — Game entry point, menu, player interaction, and replay functionality.
- `game.py` — Core game logic, player state, movement, item collection, and beacon restoration.
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

The tests cover:

- Player initialization.
- Successful and invalid movement.
- Bridge access requirements.
- Energy management.
- Item collection and duplicate prevention.
- Lighthouse restoration and winning conditions.

## Project Limitations

- The game runs entirely in the command line.
- The island uses a fixed map and predefined locations.
- Player progress is not saved between game sessions.
- The game uses simple text-based interactions.

## Author

Created as a Python programming project to practice functions, dictionaries, conditionals, loops, modular programming, and automated testing.
