from io import StringIO
from urllib.parse import urljoin

import pandas as pd
from playwright.sync_api import sync_playwright

from constants import BASE_URL, APP_IDS


def get_df(game_title: str) -> pd.DataFrame:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        try:
            page = browser.new_page()

            page.goto(urljoin(BASE_URL, str(APP_IDS[game_title])), 
                      wait_until="domcontentloaded", 
                      timeout=30000
            )

            html = page.content()

            tables = pd.read_html(StringIO(html))

            return tables[0]

        finally:
            browser.close()