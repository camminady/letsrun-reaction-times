# %%
import pandas as pd
from rich import print

# %%


list_event = ["100-metres", "200-metres", "100-metres-hurdles", "110-metres-hurdles"]
list_sex = ["women", "men"]
list_category = ["preliminary-round", "heats", "semi-final", "final"]


all_df = []
for event in list_event:
    for sex in list_sex:
        for category in list_category:
            try:
                url = f"https://www.worldathletics.org/results/olympic-games/2021/the-xxxii-olympic-games-athletics-7132391/{sex}/{event}/{category}/result"
                df_list = pd.read_html(url)

                df = pd.concat(df_list)
                df["event"] = event
                df["sex"] = sex
                df["category"] = category
                all_df.append(df)
            except Exception as e:
                pass
df = pd.concat(all_df)

# %%
df.to_csv("Tokyo.csv")
# %%
