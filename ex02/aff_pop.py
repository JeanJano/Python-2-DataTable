from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def aff_life(data: pd.DataFrame) -> None:
    """
    Plot the population projections for Belgium and France.

    This function takes a pandas DataFrame, sets the 'country' column as the
    index, transposes the DataFrame,
    and then plots the population projections for Belgium and France.

    The plot is a line plot with the years on the x-axis and the population on
    the y-axis. The x-axis ticks are set to be every 40 years and the y-axis
    ticks are set to be every 20 units.

    Parameters:
    data (pd.DataFrame): The input data as a pandas DataFrame. This DataFrame
    should have a 'country' column and a column for each year.

    Returns:
    None
    """
    data = data.set_index('country').T
    data = data.iloc[:-50]

    data_long = data[['Belgium', 'France']]
    data_long = data_long.assign(
        France=pd.to_numeric(data_long['France'].str.replace('M', '')))
    data_long = data_long.assign(
        Belgium=pd.to_numeric(data_long['Belgium'].str.replace('M', '')))
    sns.lineplot(data=data_long[['Belgium', 'France']],
                 palette=['blue', 'green'], linestyle='solid', dashes=False)

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(40))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(20))

    plt.show()


def main():
    data = load("../population_total.csv")
    if data is not None:
        aff_life(data)


if __name__ == "__main__":
    main()
