from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def aff_life(data: pd.DataFrame) -> None:
    data = data.set_index('country').T
    data = data.iloc[:-50]
    print(data)

    data_long = data[['Belgium', 'France']]
    print(data_long)
    data_long = data_long.assign(France = pd.to_numeric(data_long['France'].str.replace('M', '')))
    data_long = data_long.assign(Belgium = pd.to_numeric(data_long['Belgium'].str.replace('M', '')))
    print(data_long)
    sns.lineplot(data=data_long[['Belgium', 'France']], palette=['blue', 'green'])

    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(40))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(20))

    plt.show()


def main():
    data = load("../population_total.csv")
    if data is not None:
        aff_life(data)


if __name__ == "__main__":
    main()