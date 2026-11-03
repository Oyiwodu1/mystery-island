import random

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
        "treasure": False,
        "cave_unlocked": False,
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
                random_encounter(player)
            else:
                print("You need a Rope to cross the old bridge")
        else:
            player["location"] = destination
            player["energy"] -= 1
            random_encounter(player)
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
        if player["treasure"] is False:
            player["energy"] = min(7, player["energy"] + 2)
            player["treasure"] = True
            print(f"Amazing job {player['name']}! You found the hidden treasure. You gained 2 energy!")
        else:
            print("You have already collected the hidden treasure.")
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

def cave_guardian(player):
    while player["energy"] > 0 and player["cave_unlocked"] is False:
        print("\n---------------------")
        print("You have a cave guardian and you need to pass the riddle to have access to the cave.")
        answer = input("Guardian: What has hand but cannot clap? ").strip().lower()
        if answer == "clock":
            print(f"Correct, {player['name']}! The guardian opens the Cave entrance!")
            player["cave_unlocked"] = True
            
        elif answer == "watch":
            print(f"Thats a nice guess {player['name']}. Think about something that hangs on the wall")
            player["energy"] -= 1
        else:
            print("opppsss! you failed")
            player["energy"] -= 1

        if player["energy"] == 0:
            player["game_over"] = True


def random_encounter(player):
    chance = random.random()

    if chance < 0.6:
        print("An encounter has happened!")
        encounters = ["Wild animal", "Abandoned food", "Helpful stranger", "Sudden storm", "Quiet journey"]
        encounter = random.choice(encounters)
        print(encounter)
        if encounter == "Wild animal":
            player["energy"] -= 1
            print("A wild animal attacks you! You lose 1 energy.")
        elif  encounter == "Abandoned food":
            player["energy"] = min(7, player["energy"] + 1)
            print("You found an abandoned food! You gained 1 energy")
        elif encounter == "Helpful stranger":
            print("""A helpful stranger is here to give you a clue: 
            Stranger: Always prepare before crossing the Old Bridge.""")
        elif encounter == "Sudden storm":
            player["energy"] -= 1
            print("A sudden storm hits the island! You lose 1 energy.")
        elif encounter == "Quiet journey":
            print("The journey is peaceful. Nothing happens!")
    else:
        print("You continue your journey peacefully.")

    if player["energy"] <= 0:
        player["energy"] = 0
        player["game_over"] = True
        print("You have run out of energy!")
        