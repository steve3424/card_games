from menu import RunMenu
from war import War

def main():
    games = [War()]
    game_index = RunMenu("Game Menu", games)
    current_game_obj = games[game_index]
    current_game_obj.GameLoop()

if __name__ == "__main__":
    main()
