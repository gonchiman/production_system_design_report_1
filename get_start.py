from get_df import get_df
from constants import SteamChartsColumns


def get_start(game_title) -> str:
    df = get_df(game_title)

    return df.iloc[-1][SteamChartsColumns.MONTH]