from get_start import get_start
from constants import GameTitle


for game_title in GameTitle:
    print(f"{game_title.value}: {get_start(game_title.value)}")