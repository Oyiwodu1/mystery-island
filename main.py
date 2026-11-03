from game import new_game, move_player, search_location, restore_beacon

def show_instructions():
    print("===== WELCOME TO MYSTERY ISLAND =====\n")

    print("""Your mission: Explore the island, find useful objects, solve obstacles, and restore the lighthouse beacon before your energy runs out.

        How to play:
        - You start with 5 energy points.
        - Moving between locations costs 1 energy point.
        - Searching locations does not cost energy.
        - Find the rope in the Jungle.
        - Find the lantern in the Cave.
        - You need the rope to cross the Old Bridge.
        - You need the lantern to restore the lighthouse beacon.
        - You can revisit previous locations.
        - If your energy reaches zero before you win, you lose.\n""")

def show_map():
     print("""
        ===== MYSTERY ISLAND MAP =====

          [BEACH]
             |
             |
          [JUNGLE]  - Find Rope
             |
             |
           [CAVE]   - Find Lantern
             |
             |
       [OLD BRIDGE] - Rope required
             |
             |
       [LIGHTHOUSE] - Lantern required

    =============================
    """)

def show_menu():
    print("1. Move")
    print("2. Search location")
    print("3. Check inventory")
    print("4. Check status")
    print("5. Quit game")
    print("6. Restore lighthouse beacon")

    choice = input("Enter your choice: ")
    return choice

def main():
    show_instructions()
    name = input("Welcome player, what is your name? ").title()
    while True:
        player = new_game(name)
        quit_game = False
        print(f"Nice to meet you {name}, kindly choose an option from the menu.")

        while player["game_over"] is False:
            print(f"\nYour current location is: {player['location']}")
            show_map()
            print(f"Remaining energy: {player['energy']}")
            choice = show_menu()

            if choice == "1":
                destination = input("where is your next stop? ").strip().title()
                move_player(player, destination)

            elif choice == "2":
                search_location(player)

            elif choice == "3":
                if player["inventory"] == []:
                    print("Your inventory is empty")
                else:
                    print(f"You have {player['inventory']} in your player inventory")

            elif choice == "4":
                print(f"Player: {player['name']}")
                print(f'Your current location is : {player["location"]}')
                print(f"You have {player['energy']} energy left")
                print(f"You have {player['inventory']} in your inventory list")

            elif choice == "5":
                quit_game = True
                player["game_over"] = True

            elif choice == "6":
                restore_beacon(player)

            else:
                print("Invalid option!!!! Please choose between 1-6")
        if player["won"]:
            print("Congratulations! You escaped Mystery Island!")
        elif quit_game:
            print("Thanks for playing. See you next time!")
        else:
            print("GAME OVER! You have exhausted your energy.")


        play_again = input("Would you love to play again? (yes/no): ").strip().lower()
        while play_again not in ["yes", "no"]:
            print("Invalid response. Please enter yes or no.")
            play_again = input("Would you love to play again? (yes/no): ").strip().lower()

        if play_again == "yes":
            continue
        else:
            print("Goodbye!")
            break
if __name__ == "__main__":
    main() 
