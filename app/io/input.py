import pandas as pd

# 1
def input_text():
    """
    Function to input text from the console.

    This function allows the user to input text via the console. The entered
    text will be returned as a string.
    """
    return input("Enter text: ")

# 2
def read_file(path: str):
    """
    Reads the content of a file and returns it as a string.
    Args:
        path (str): The file path where data will be read.
    Returns:
        str: The contents of the file.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file '{path}': {e}"

# 3
def read_file_pandas(path: str):
    """
    Reads data from a file and returns it as a DataFrame.
    Args:
        path (str): The file path where data will be read.
    Returns:
        pandas.DataFrame: The data from the file as a DataFrame.
    """
    try:
        return pd.read_csv(path)
    except Exception as e:
        return f"Error reading file '{path}': {e}"