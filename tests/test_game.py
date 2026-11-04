import game
import unittest
from unittest.mock import patch
from game import new_game, move_player, search_location, restore_beacon, cave_guardian


class TestNewGame(unittest.TestCase):

    def test_new_game_defaults(self):
        player = new_game("Faith")

        self.assertEqual(player["name"], "Faith")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertFalse(player["game_over"])
        self.assertFalse(player["won"])


class TestSearchLocation(unittest.TestCase):

    def test_collect_rope(self):
        player = new_game("Faith")
        player["location"] = "Jungle"

        search_location(player)

        self.assertIn("rope", player["inventory"])

    def test_collect_lantern(self):
        player = new_game("Faith")
        player["location"] = "Cave"

        search_location(player)

        self.assertIn("lantern", player["inventory"])

    def test_cannot_collect_rope_twice(self):
        player = new_game("Faith")
        player["location"] = "Jungle"

        search_location(player)
        search_location(player)

        self.assertEqual(player["inventory"].count("rope"), 1)

    def test_treasure_increases_energy(self):
        player = new_game("Faith")
        player["location"] = "Cave"
        player["energy"] = 3

        search_location(player)

        self.assertEqual(player["energy"], 5)
        self.assertTrue(player["treasure"])

    def test_cannot_collect_treasure_twice(self):
        player = new_game("Faith")
        player["location"] = "Cave"
        player["energy"] = 3

        search_location(player)
        search_location(player)

        self.assertEqual(player["energy"], 5)

    def test_treasure_does_not_exceed_max_energy(self):
        player = new_game("Faith")
        player["location"] = "Cave"
        player["energy"] = 6

        search_location(player)

        self.assertEqual(player["energy"], 7)


class TestMovePlayer(unittest.TestCase):

    def test_successful_movement(self):
        player = new_game("Faith")

        with patch("game.random_encounter"):
            move_player(player, "Jungle")
        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)

    def test_can_cross_bridge_with_rope(self):
        player = new_game("Faith")
        player["location"] = "Cave"
        player["inventory"].append("rope")

        with patch("game.random_encounter"):
            move_player(player, "Old Bridge")

        self.assertEqual(player["location"], "Old Bridge")
        self.assertEqual(player["energy"], 4)

    def test_invalid_destination(self):
        player = new_game("Faith")

        move_player(player, "Airport")

        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_energy_zero_ends_game(self):
        player = new_game("Faith")
        player["energy"] = 1

        with patch("game.random_encounter"):
            move_player(player, "Jungle")

        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])

    @patch("game.random.choice", return_value="Abandoned food")
    @patch("game.random.random", return_value=0.2)
    def test_player_cannot_be_rescued_after_energy_reaches_zero(self, mock_random, mock_choice):
        player = new_game("Faith")
        player["energy"] = 1

        move_player(player, "Jungle")

        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])

class TestRestoreBeacon(unittest.TestCase):

    def test_player_wins_with_lantern(self):
        player = new_game("Faith")
        player["location"] = "Lighthouse"
        player["inventory"].append("lantern")

        restore_beacon(player)

        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])

    def test_player_cannot_win_without_lantern(self):
        player = new_game("Faith")
        player["location"] = "Lighthouse"

        restore_beacon(player)

        self.assertFalse(player["won"])
        self.assertFalse(player["game_over"])

    def test_player_cannot_restore_beacon_outside_lighthouse(self):
        player = new_game("Faith")
        player["inventory"].append("lantern")

        restore_beacon(player)

        self.assertFalse(player["won"])
        self.assertFalse(player["game_over"])

class TestCaveGuardian(unittest.TestCase):

    @patch("builtins.input", return_value="clock")
    def test_correct_answer_unlocks_cave(self, mock_input):
        player = new_game("Faith")

        cave_guardian(player)

        self.assertTrue(player["cave_unlocked"])

    @patch("builtins.input", side_effect=["wrong", "clock"])
    def test_wrong_answer_reduces_energy(self, mock_input):
        player = new_game("Faith")

        cave_guardian(player)

        self.assertEqual(player["energy"], 4)
        self.assertTrue(player["cave_unlocked"])

    @patch("builtins.input", return_value="wrong")
    def test_wrong_answer_can_end_game(self, mock_input):
        player = new_game("Faith")
        player["energy"] = 1

        cave_guardian(player)

        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])
        self.assertFalse(player["cave_unlocked"])

class TestRandomEncounter(unittest.TestCase):

    @patch("game.random.choice", return_value="Abandoned food")
    @patch("game.random.random", return_value=0.2)
    def test_abandoned_food_increases_energy(self, mock_random, mock_choice):
        player = new_game("Faith")

        game.random_encounter(player)

        self.assertEqual(player["energy"], 6)

    @patch("game.random.choice", return_value="Wild animal")
    @patch("game.random.random", return_value=0.2)
    def test_wild_animal_reduces_energy(self, mock_random, mock_choice):
        player = new_game("Faith")

        game.random_encounter(player)

        self.assertEqual(player["energy"], 4)
        self.assertFalse(player["game_over"])

    @patch("game.random.choice", return_value="Sudden storm")
    @patch("game.random.random", return_value=0.2)
    def test_sudden_storm_reduces_energy(self, mock_random, mock_choice):
        player = new_game("Faith")

        game.random_encounter(player)

        self.assertEqual(player["energy"], 4)
        self.assertFalse(player["game_over"])

    @patch("game.random.choice", return_value="Helpful stranger")
    @patch("game.random.random", return_value=0.2)
    def test_helpful_stranger_does_not_change_energy(self, mock_random, mock_choice):
        player = new_game("Faith")

        game.random_encounter(player)

        self.assertEqual(player["energy"], 5)
        self.assertFalse(player["game_over"])

    @patch("game.random.choice", return_value="Quiet journey")
    @patch("game.random.random", return_value=0.2)
    def test_quiet_journey_does_not_change_energy(self, mock_random, mock_choice):
        player = new_game("Faith")

        game.random_encounter(player)

        self.assertEqual(player["energy"], 5)
        self.assertFalse(player["game_over"])

    @patch("game.random.choice", return_value="Wild animal")
    @patch("game.random.random", return_value=0.2)
    def test_wild_animal_can_end_game(self, mock_random, mock_choice):
        player = new_game("Faith")
        player["energy"] = 1

        game.random_encounter(player)

        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])

    @patch("game.random.random", return_value=0.8)
    def test_no_encounter_happens(self, mock_random):
        player = new_game("Faith")

        game.random_encounter(player)

        self.assertEqual(player["energy"], 5)
        self.assertFalse(player["game_over"])

    @patch("game.random.choice", return_value="Abandoned food")
    @patch("game.random.random", return_value=0.2)
    def test_abandoned_food_does_not_exceed_max_energy(self, mock_random, mock_choice):
        player = new_game("Faith")
        player["energy"] = 7

        game.random_encounter(player)

        self.assertEqual(player["energy"], 7)

if __name__ == "__main__":
    unittest.main()