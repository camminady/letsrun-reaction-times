# %%
import pandas as pd
import requests

# %%
sources = pd.read_csv(
    "/Users/thomascamminady/Dev/letsrun/data/sources/sources-combined.csv"
)
# %%
print(len(sources))
# %%
all_df = []
for (i, row) in sources.iterrows():
    print(i)
    try:
        df = pd.concat(pd.read_html(row.url))
        df["index"] = i
        for column in sources.columns:
            df[column] = row[column]

        all_df.append(df)
    except Exception as e:
        print(e)
df = pd.concat(all_df)
df.to_csv("../../data/reactiontimes.csv")

# %%
