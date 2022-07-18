# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#%%
df = pd.read_csv("../letsrun/ReactionTimes.csv")
# %%
sns.set_theme(style="darkgrid")
sns.set_context("poster")
# Initialize the figure with a logarithmic x axis
f, ax = plt.subplots(figsize=(20, 10))


# Plot the orbital period with horizontal boxes
sns.boxplot(
    x="Reaction Time",
    y="location",
    data=df,
    color="grey",
    whis=[0, 100],
    width=0.6,
)

# Add in points to show each observation
sns.stripplot(
    x="Reaction Time",
    y="location",
    data=df,
    hue="sex",
    size=8,
    # linewidth=0,
    alpha=0.7,
    # palette="Set2"
)

# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)
# %%
df[df["Reaction Time"] <= 0.1]
