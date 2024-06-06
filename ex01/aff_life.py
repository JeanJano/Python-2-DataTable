from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def aff_life(data: pd.DataFrame) -> None:
    """
    Plot the life expectancy projections for France.

    This function takes a pandas DataFrame, sets the 'country' column as the
    index, transposes the DataFrame,
    and then plots the life expectancy projections for France (which is
    assumed to be the 59th column in the transposed DataFrame).

    The plot is a line plot with the years on the x-axis and the life
    expectancy on the y-axis. The x-axis ticks are set to be every 40 years.

    Parameters:
    data (pd.DataFrame): The input data as a pandas DataFrame. This
    DataFrame should have a 'country' column and a column for each year.

    Returns:
    None
    """
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
    data = load("../life_expectancy_years.csv")
    if data is not None:
        aff_life(data)


if __name__ == "__main__":
    main()
