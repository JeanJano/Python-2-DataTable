from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def aff_life(income: pd.DataFrame, life: pd.DataFrame) -> None:
    life = life['1900']
    income = income['1900']

    data = pd.concat([income, life], axis=1)
    sns.set_theme(style="ticks")
    g = sns.relplot(data=data, x=income.values, y=life.values, height=6, aspect=10/6)

    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

    g.set(xscale="log")
    labels = [f'{int(x/1000)}k' for x in g.ax.get_xticks()]
    g.ax.set_xticklabels(labels)

    plt.show()


def main():
    income = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("../life_expectancy_years.csv")
    if income is not None and life is not None:
        aff_life(income, life)


if __name__ == "__main__":
    main()
