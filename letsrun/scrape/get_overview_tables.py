# %%
import pandas as pd
from rich import print
from bs4 import BeautifulSoup
import requests

# %%
def get_summary_table(url):
    # %% Get displayed table with events
    df = pd.read_html(url)[0]

    # %% Extract the hidden href links to the data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    links = []
    for tr in table.findAll("tr"):
        trs = tr.findAll("td")
        for each in trs:
            try:
                link = each.find("a")["href"]
                links.append(link)
            except Exception as e:
                pass
                # print(e)

    # %% Combine and save
    df["links"] = links
    return df.iloc[:-1]


# %%


url = "https://www.worldathletics.org/results/world-athletics-championships"
df = get_summary_table(url)
df.to_csv("../../data/sources-wc.csv")

url = "https://www.worldathletics.org/results/olympic-games"
df = get_summary_table(url)
df.to_csv("../../data/sources-oly.csv")

# %%
