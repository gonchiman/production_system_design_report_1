from enum import Enum


class GameTitle(Enum):
    STREET_FIGHTER_6 = "Street Fighter 6"
    TEKKEN_8 = "TEKKEN 8"
    GUILTY_GEAR_STRIVE = "GUILTY GEAR -STRIVE-"
    GRANBLUE_FANTASY_VERSUS_RISING = "Granblue Fantasy Versus: Rising"
    THE_KING_OF_FIGHTERS_XV = "THE KING OF FIGHTERS XV"

class SteamChartsColumns:
    MONTH = "Month"
    AVG_PLAYERS = "Avg. Players"
    GAIN = "Gain"
    GAIN_PERCENT = "% Gain"
    PEAK_PLAYERS = "Peak Players"

APP_IDS = {
    "Street Fighter 6": 1364780,
    "TEKKEN 8": 1778820,
    "GUILTY GEAR -STRIVE-": 1384160,
    "Granblue Fantasy Versus: Rising": 2157560,
    "THE KING OF FIGHTERS XV": 1498570,
}

BASE_URL = "https://steamcharts.com/app/"