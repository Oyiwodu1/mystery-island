import unittest
from game import new_game, move_player, search_location, restore_beacon


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


class TestMovePlayer(unittest.TestCase):

    def test_successful_movement(self):
        player = new_game("Faith")

        move_player(player, "Jungle")

        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)

    def test_cannot_cross_bridge_without_rope(self):
        player = new_game("Faith")
        player["location"] = "Cave"

        move_player(player, "Old Bridge")

        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 5)

    def test_can_cross_bridge_with_rope(self):
        player = new_game("Faith")
        player["location"] = "Cave"
        player["inventory"].append("rope")

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


if __name__ == "__main__":
    unittest.main()