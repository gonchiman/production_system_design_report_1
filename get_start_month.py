from get_df import get_df
from constants import SteamChartsColumns


def get_start_month(game_title):
    df = get_df(game_title)

    return df.iloc[-1][SteamChartsColumns.MONTH]