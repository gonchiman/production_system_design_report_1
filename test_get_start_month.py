from get_start_month import get_start_month
from constants import GameTitle


for game_title in GameTitle:
    print(f"{game_title.value}: {get_start_month(game_title.value)}")