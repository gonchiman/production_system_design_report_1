from constants import SteamChartsColumns
from get_df import get_df
import matplotlib.pyplot as plt


class ShowGraphs:
    def show_plot(game_title: str, column: str) -> None:
        df = get_df(game_title)

        plt.plot(df[SteamChartsColumns.MONTH], df[column])
        plt.show()