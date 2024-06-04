from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def aff_life(data: pd.DataFrame) -> None:
    data = data.set_index('country').T
    data = data.iloc[:-50]
    print(data.columns[58])
    print(data.index)

    sns.set_theme(style="ticks")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=data.index, y=data.columns[12], label=data.columns[12])
    sns.lineplot(data=data, x=data.index, y=data.columns[58], label=data.columns[58], color='green')

    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(40))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(200))

    plt.gca().invert_yaxis()

    plt.show()


def main():
    data = load("../population_total.csv")
    if data is not None:
        aff_life(data)


if __name__ == "__main__":
    main()