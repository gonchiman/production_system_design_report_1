from io import StringIO

import pandas as pd
from playwright.sync_api import sync_playwright


url = "https://steamcharts.com/app/1364780"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(url, wait_until="domcontentloaded", timeout=30000)

    html = page.content()

    tables = pd.read_html(StringIO(html))

    print(f"tables count: {len(tables)}")

    df = tables[0]

    print(df)
    print(df.columns)

    browser.close()