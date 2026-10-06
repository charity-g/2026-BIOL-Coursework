import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "./BIOL 363 Mussel MR Lab 09262026 Class data.xlsx"

df = pd.read_excel(filepath, sheet_name="Standardized", header=[0], skiprows=4)
print(df.columns, df.shape)
# print(df.head)

df.loc[df['Exposure'] == '12 Degrees control', 'Exposure'] = '12 Degrees Control' 
value_counts = df[['Exposure']].value_counts()

# ============================
# Figure 1. processed data 

def figure1():
    treatment_order = [
    "30 Degrees Air Exposed"
    "12 Degrees Air Exposed"
    "12 Degrees Control"
    ]
    df_heatmap = df.copy()

    # Make Treatment categorical so the DataFrame sorts in the desired order
    df_heatmap["Exposure"] = pd.Categorical(
        df_heatmap["Exposure"],
        categories=treatment_order,
        ordered=True
    )

    # 2. Sort by treatment
    df_sorted = df_heatmap.sort_values("Exposure").reset_index(drop=True)

    # 3. Select variables for heatmap
    heatmap_data = df_sorted[
        [
            # "Change in DO2",
            # "Total experiment duration (min)",
            # "Volume of water (L)",
            # "Mussel weight (g)",
            # "Mussel length (mm)",
            "Change in DO2 per minute per L"
        ]
    ]


    # 4. Create heatmap
    plt.figure(figsize=(10, 8))

    sns.heatmap(
        heatmap_data,
        cmap="viridis",
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        cbar_kws={"label": "Value"}
    )

    # 5. Add treatment labels
    plt.yticks(
        ticks=[i + 0.5 for i in range(len(df_sorted))],
        labels=df_sorted["Exposure"],
        rotation=0
    )


    xlabels = [
        # "Change in DO2",
        # "Total experiment \n duration (min)",
        # "Volume of water (L)",
        # "Mussel weight (g)",
        # "Mussel length (mm)",
        "Change in DO2 \n per minute per L"
    ]
    plt.xticks(
        ticks=[i + 0.5 for i in range(len(xlabels))],
        labels=xlabels,
        rotation=0, ha="center")

    plt.xlabel("Variables")
    plt.ylabel("Exposure")
    plt.title("Heatmap of Experiment Measurements Ordered by Exposure")

    plt.tight_layout()
    plt.show()


# ======================
# Figure 2 - bar chart

def figure2():
    sns.barplot(
        data=df,
        x="Exposure",
        y="Change in DO2 per minute per L",
        hue="Exposure",
        errorbar=('ci', 90)
    )
    plt.title("Change in DO2 per minute per L For different Exposure treatments")
    plt.show()



# ======================
# Figure 3 - scatter plot
# sns.scatterplot(
#     data=df,
#     x="Exposure",
#     y="Change in DO2 per minute per L",
#     hue="Exposure",
#     # errorbar=('ci', 95)
#                 )
# plt.title("Scatterplot of Change in DO2 per minute per L for Mussel weight, Colored by exposure")
# plt.show()

# ==================
# ACTUALLY RUN CODE
# figure1()
figure2()