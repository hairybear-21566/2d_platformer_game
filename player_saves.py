import pickle


def save_game(player_name: str, score: int, player_position: list, 
              player_velocity: int, platform_positions: list, background_1_positions: list, 
              background_2_positions: list, background_upper1_positions: list, background_upper2_positions: list, 
              platform_scroll_speed: int, birds_array: list)->None:
    """
    Saves a player's game data to a binary file.

    Args:
        player_name (str): The player's name.
        score (int): The player's score.
        player_position (list): The player's position on the screen.
        player_velocity (int): The player's vertical velocity.
        platform_positions (list): The positions of all the platforms.
        background_1_positions (list): The positions of the first background.
        background_2_positions (list): The positions of the second background.
        background_upper1_positions (list): The positions of the first upper background.
        background_upper2_positions (list): The positions of the second upper background.
        platform_scroll_speed (int): The speed at which the platforms move.
        birds_array (list): The positions and velocities of all the birds.
    """
    
    save_data = {
        'player_name': player_name,
        'score': score,
        'player_position': player_position,
        'player_velocity': player_velocity,
        'platform_positions': platform_positions,
        'background_1_positions': background_1_positions,
        'background_2_positions': background_2_positions,
        'background_upper1_positions': background_upper1_positions,
        'background_upper2_positions': background_upper2_positions,
        'platform_scroll_speed': platform_scroll_speed,
        'birds_array': birds_array
    }

    # Load existing saves or create an empty list
    saves = read_saves_binary_file()

    # Check if the player already has a save
    # if yes existing save index saved to variable otherwise the variable remains as None
    # existing_save_index = next((index for index, save in enumerate(saves) if save['player_name'] == player_name), None)
    existing_save_index = None
    for d in range(len(saves)):
        if saves[d]["player_name"] == player_name:
            existing_save_index = d
            break

    # Update existing save or append a new one
    if existing_save_index is not None:
        saves[existing_save_index] = save_data
    else:
        saves.append(save_data)

    if len(saves) >= 6:
        saves = saves[1:6]

    # Save the updated list back to the file
    with open('Player_saves.dat', 'wb') as file:
        pickle.dump(saves, file)
        # print(saves)


def read_saves_binary_file() -> list:
    """
    Reads a list of player saves from a binary file.

    Returns:
        list: A list of player saves, where each save is a dictionary containing the player's name, score, position, velocity, platform positions, background positions, and bird positions.
    """
    try:
        with open('Player_saves.dat', 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        # Return an empty list if the file doesn't exist or is empty
        return []
