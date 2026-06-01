from constants import SteamChartsColumns
from get_df import get_df
import matplotlib.pyplot as plt


class ShowGraphs:
    @staticmethod
    def show_plot(game_title: str, column: str) -> None:
        df = get_df(game_title)

        # "Last 30 Days" は月データではないので除外
        df = df[df[SteamChartsColumns.MONTH] != "Last 30 Days"]

        # 古い月 → 新しい月 の順にする
        df = df.iloc[::-1].reset_index(drop=True)

        months = df[SteamChartsColumns.MONTH]
        values = df[column]

        x = range(len(df))

        plt.figure(figsize=(12, 6))
        plt.plot(x, values, marker="o")

        # 表示したい月だけ指定
        display_months = [
            "June 2023",
            "January 2024",
            "June 2024",
            "January 2025",
            "June 2025",
            "January 2026",
            "May 2026",
        ]

        tick_positions = [
            i for i, month in enumerate(months)
            if month in display_months
        ]

        tick_labels = [
            months[i] for i in tick_positions
        ]

        plt.xticks(
            ticks=tick_positions,
            labels=tick_labels,
            rotation=45
        )

        plt.xlabel("Month")
        plt.ylabel(column)
        plt.title(f"{game_title} - {column}")
        plt.tight_layout()
        plt.show()