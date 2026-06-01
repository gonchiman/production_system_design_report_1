from constants import GameTitle, SteamChartsColumns
from get_df import get_df
import matplotlib.pyplot as plt

from get_start_month import get_start
from period import Period


class ShowGraphs2:
    @staticmethod
    def show_plot(column: str, duration: int = None) -> None:
        plt.figure(figsize=(12, 6))        

        for game_title in GameTitle:
            game_title = game_title.value

            df = get_df(game_title)

            # "Last 30 Days" は月データではないので除外
            df = df[df[SteamChartsColumns.MONTH] != "Last 30 Days"]

            # 古い月 → 新しい月 の順にする
            df = df.iloc[::-1].reset_index(drop=True)

            start = get_start(game_title)
            start_month, start_year = start.split()
            period = Period(start_year=start_year, start_month=start_month, duration=duration)

            if period is not None:
                start_index = df.index[df[SteamChartsColumns.MONTH] == period.start][0]
                end_index = df.index[df[SteamChartsColumns.MONTH] == period.end][0]

                if start_index > end_index:
                    start_index, end_index = end_index, start_index

                df = df.iloc[start_index:end_index + 1].reset_index(drop=True)

            months = df[SteamChartsColumns.MONTH]
            values = df[column]

            x = range(len(df))


            plt.plot(x, values, marker="o", label=game_title)

        plt.xticks(
            ticks=x,
            labels=months,
            rotation=90
        )

        plt.xlabel("Month")
        plt.ylabel(column)
        plt.title(f"{column}")

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()