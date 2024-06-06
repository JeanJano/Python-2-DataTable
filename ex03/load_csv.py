import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    This function reads a CSV file from the specified path and returns it as a
    pandas DataFrame.
    If the file is not found, is empty, or cannot be parsed, an error message
    is printed.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data as a pandas DataFrame.

    Raises:
    FileNotFoundError: If the file at the specified path is not found.
    pd.errors.EmptyDataError: If the file is empty.
    pd.errors.ParserError: If there is a problem parsing the file.
    Exception: If any other unexpected error occurs.
    """
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
