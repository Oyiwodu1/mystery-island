locations = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse":["Old Bridge"]
}

def new_game(name):  #creates the player.
    player = {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }
    return player

def move_player(player, destination):   #handles movement.
    if destination in locations[player["location"]]:
        if destination == "Old Bridge":
            if "rope" in player["inventory"]:
                player["location"] =  destination
                player["energy"] -= 1
            else:
                print("You need a Rope to cross the old bridge")
        else:
            player["location"] = destination
            player["energy"] -= 1
    else:
        print("INVALID DESTINATION!")

    if player["energy"] == 0:
       player["game_over"] = True

def search_location(player):     #handles collecting objects.
    
    if player["location"] == "Jungle":
        if "rope" not in player["inventory"]:
            player["inventory"].append("rope")
            print("You found a rope!")
        else:
            print("You have already collected the rope!")
    elif player["location"] == "Cave":
        if "lantern" not in player["inventory"]:
            player["inventory"].append("lantern")
            print("Yayyy, You found the lantern!")
        else:
            print("opps! You have already collected the lantern")
    else:
        print("You found nothing useful here")


def restore_beacon(player):
    if player["location"] == "Lighthouse":
        if "lantern" in player["inventory"]:
            player["won"] = True
            player["game_over"] = True
            print("Congratulations, you won the game!!!!!")
        else:
            print("opps! Lantern is required to restore the beacon")
    else:
        print("Player's final destination must be lighthouse")