#%%
import pandas as pd
import numpy as np

# %%
#
df = pd.read_csv("/Users/thomascamminady/Dev/letsrun/data/reactiontimes.csv")
# df["year"] = [int(x.split("/")[5]) for x in df.url.values]
df["year"] = [int(x.split(" ")[-1]) for x in df.date.values]


df.loc[df["Reaction Time"] == "0.-91", "Reaction Time"] = ""
# df = df.drop(index=3865)
df["reaction_time_float"] = pd.to_numeric(df["Reaction Time"])  # , errors="ignore")
df["Sex"] = df.sex
df = df[df.year >= 1999]
df = df[df.reaction_time_float >= 0]
df = df[df.reaction_time_float > 0]
df.loc[df.Sex == "men", "Sex"] = "M"
df.loc[df.Sex == "women", "Sex"] = "F"

# %%
df["BIB"] = df["BIB"].astype("int", errors="ignore")

# drop unnamed column
df.drop(columns=["Unnamed: 0"])
df["date_from"] = pd.to_datetime([x.split("-")[0] for x in df.date.values])
df["date_to"] = pd.to_datetime([x.split("-")[1] for x in df.date.values])


def convert(x):
    if x == "DQ" or x == "DNF" or x.split(" ")[0] == "DNF" or x.split(" ")[0] == "DQ":
        return np.nan
    else:
        t = x.split(" ")[0]
        try:
            return float(t)

        except Exception as e:
            print(t)
            minutes = t.split(":")[0]
            seconds = t.split(":")[1]
            return 60 * float(minutes) + float(seconds)


times = [convert(x) for x in df.MARK.values]
df["time"] = times
event = []
for x in df.name.values:
    if "oly" in x.lower():
        event.append("OLY")
    elif "world" in x.lower() or "ships" in x.lower():
        event.append("WC")
    else:
        print(x)

df["type"] = event
# %%
df
# %%
neworder = [
    "name",
    "type",
    "year",
    "venue",
    "date_from",
    "date_to",
    "ATHLETE",
    "BIB",
    "COUNTRY",
    "Sex",
    "event",
    "round",
    "reaction_time_float",
    "time",
    "MARK",
    "POS",
    # "url",
]

newdf = df[neworder]
newdf.columns = map(str.lower, newdf.columns)
newdf.rename(
    columns={
        "event": "discipline",
        "reaction_time_float": "reaction_time",
        "mark": "time_string",
    },
    inplace=True,
)


# %%
newdf.to_csv(
    "/Users/thomascamminady/Dev/letsrun/data/reactiontimes_preprocessed.csv",
    index=False,
)
