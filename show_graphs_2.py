from enum import Enum, auto

from constants import SAVE_DIR, GameTitle, SteamChartsColumns
from get_df import get_df
import matplotlib.pyplot as plt

from get_start import get_start

class GraphOperationMode(Enum):
    SHOW = auto()
    SAVE = auto()

class ShowGraphs2:
    GRAPH_OPERATION_MODE = {
        "show": GraphOperationMode.SHOW,
        "save": GraphOperationMode.SAVE,
    }

    @staticmethod
    def show_plot(column: SteamChartsColumns, 
                  duration: int = None, 
                  mode: GraphOperationMode = GraphOperationMode.SHOW
        ) -> None:
        plt.figure(figsize=(12, 6))

        for game_title in GameTitle:
            game_title = game_title.value

            df = get_df(game_title)

            # "Last 30 Days" は月データではないので除外
            df = df[df[SteamChartsColumns.MONTH] != "Last 30 Days"]

            # 古い月 → 新しい月 の順にする
            df = df.iloc[::-1].reset_index(drop=True)

            # 発売月を取得
            start_month = get_start(game_title)

            # 発売月の行番号を探す
            matched_indexes = df.index[df[SteamChartsColumns.MONTH] == start_month]

            if len(matched_indexes) == 0:
                print(f"{game_title}: 発売月 {start_month} が見つかりません")
                continue

            start_index = matched_indexes[0]

            # 発売月から duration か月分を取得
            if duration is not None:
                df = df.iloc[start_index:start_index + duration].reset_index(drop=True)
            else:
                df = df.iloc[start_index:].reset_index(drop=True)

            values = df[column]

            # x軸は「発売から何か月目」
            x = range(len(df))

            plt.plot(x, values, marker="o", label=game_title)

        plt.xlabel("Months Since Release")
        plt.ylabel(column)
        plt.title(f"{column} After Release")

        if duration is not None:
            plt.xticks(
                ticks=range(duration),
                labels=range(1, duration + 1)
            )

        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        if mode == GraphOperationMode.SHOW:
            plt.show()
        elif mode == GraphOperationMode.SAVE:
            plt.savefig(SAVE_DIR / f"{column}_after_release.png")
            plt.close()
        else:
            raise ValueError("Invalid GraphOperationMode")

    @staticmethod
    def show_cumulative_plot(column: SteamChartsColumns, 
                             duration: int = None, 
                             mode: GraphOperationMode = GraphOperationMode.SHOW
        ) -> None:
        plt.figure(figsize=(12, 6))

        for game_title in GameTitle:
            game_title = game_title.value

            df = get_df(game_title)

            # "Last 30 Days" は月データではないので除外
            df = df[df[SteamChartsColumns.MONTH] != "Last 30 Days"]

            # 古い月 → 新しい月 の順にする
            df = df.iloc[::-1].reset_index(drop=True)

            # 発売月を取得
            start_month = get_start(game_title)

            # 発売月の行番号を探す
            matched_indexes = df.index[df[SteamChartsColumns.MONTH] == start_month]

            if len(matched_indexes) == 0:
                print(f"{game_title}: 発売月 {start_month} が見つかりません")
                continue

            start_index = matched_indexes[0]

            # 発売月から duration か月分を取得
            if duration is not None:
                df = df.iloc[start_index:start_index + duration].reset_index(drop=True)
            else:
                df = df.iloc[start_index:].reset_index(drop=True)

            values = df[column].cumsum()

            # x軸は「発売から何か月目」
            x = range(len(df))

            plt.plot(x, values, marker="o", label=game_title)

        plt.xlabel("Months Since Release")
        plt.ylabel(column)
        plt.title(f"{column} After Release")

        if duration is not None:
            plt.xticks(
                ticks=range(duration),
                labels=range(1, duration + 1)
            )

        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        if mode == GraphOperationMode.SHOW:
            plt.show()
        elif mode == GraphOperationMode.SAVE:
            plt.savefig(SAVE_DIR / f"{column}_after_release.png")
            plt.close()
        else:
            raise ValueError("Invalid GraphOperationMode")