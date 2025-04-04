import pandas as pd

# 1
def output_text(text: str):
    """
    Outputs text to the console or another output destination.

    This function prints the given text to the console.

    Args:
        text (str): The text to output.
    """
    print(text)


# 2
def write_file(path: str, text: str):
    """
    Writes data to a file at the given path.

    This function writes the provided text to a file at the specified path.

    Args:
        path (str): The file path where data will be written.
        text (str): The text to write.
    """
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        return f"Error writing to file '{path}': {e}"


# 3
def write_file_pandas(path: str, text: pd.DataFrame):
    """
    Writes a pandas DataFrame to a file at the given path.

    This function saves the provided DataFrame as a CSV file at the specified path.

    Args:
        path (str): The file path where data will be written.
        text (pd.DataFrame): The DataFrame to write.
    """
    try:
        text.to_csv(path, index=False)
    except Exception as e:
        return f"Error writing DataFrame to file '{path}': {e}"