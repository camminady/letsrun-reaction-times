# %%
import pandas as pd
from rich import print

# %%


list_event = ["100-metres", "100-metres-hurdles", "110-metres-hurdles"]
list_sex = ["women", "men"]
list_category = ["preliminary-round", "heats", "semi-final", "final"]

sources = [
    "/Users/thomascamminady/Dev/letsrun/data/sources-oly.csv",
    "/Users/thomascamminady/Dev/letsrun/data/sources-wc.csv",
]

d = []
for source in sources:
    sourcedf = pd.read_csv(source)
    for (i, row) in sourcedf.iterrows():
        for event in list_event:
            for sex in list_sex:
                if sex == "women" and event == "110-metres-hurdles":
                    continue
                if sex == "men" and event == "100-metres-hurdles":
                    continue
                for category in list_category:

                    try:
                        url = f"https://www.worldathletics.org{row.links}/{sex}/{event}/{category}/result"
                        d.append(
                            {
                                "name": row["MEETING NAME"],
                                "venue": row["VENUE"],
                                "date": row["DATE"],
                                "country": row["COUNTRY"],
                                "event": event,
                                "sex": sex,
                                "round": category,
                                "url": url,
                            }
                        )
                    except Exception as e:
                        print(e)
                        pass


# %%
combineddf = pd.DataFrame(d)
combineddf.to_csv("../../data/sources-combined.csv", index=False)
# %%
