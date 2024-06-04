from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def aff_life(data: pd.DataFrame) -> None:
    data = data.set_index('country').T

    sns.set_theme(style="ticks")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=data.index, y=data.columns[58])

    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(40))

    plt.show()


def main():
    data = load("../population_total.csv")
    aff_life(data)


if __name__ == "__main__":
    main()