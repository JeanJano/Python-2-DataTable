import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")

        return df
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: The file at path '{path}' was not found.")
    except pd.errors.EmptyDataError:
        # Handle the case where the file is empty
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        # Handle the case where there is a parsing error in the file
        print("Error: There was a problem parsing the file.")
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")


def main():
    print(load("../life_expectancy_years.csv"))


if __name__ == "__main__":
    main()