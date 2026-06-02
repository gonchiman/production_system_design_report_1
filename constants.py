from enum import Enum

from pathlib import Path


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

class Month:
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"

MONTH_NUMS = {
    Month.JANUALY: 1,
    Month.FEBRUARY: 2,
    Month.MARCH: 3,
    Month.APRIL: 4,
    Month.MAY: 5,
    Month.JUNE: 6,
    Month.JULY: 7,
    Month.AUGUST: 8,
    Month.SEPTEMBER: 9,
    Month.OCTOBER: 10,
    Month.NOVEMBER: 11,
    Month.DECEMBER: 12,
}

APP_IDS = {
    "Street Fighter 6": 1364780,
    "TEKKEN 8": 1778820,
    "GUILTY GEAR -STRIVE-": 1384160,
    "Granblue Fantasy Versus: Rising": 2157560,
    "THE KING OF FIGHTERS XV": 1498570,
}

BASE_URL = "https://steamcharts.com/app/"

BASE_DIR = Path(__file__).resolve().parent
SAVE_DIR = BASE_DIR / "plots"