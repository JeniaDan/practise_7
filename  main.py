from app.io.input import input_text, read_file, read_file_pandas
from app.io.output import output_text, write_file, write_file_pandas

def main():
    text_from_console = input_text()
    text_from_file_builtin = read_file('example.txt')
    df_from_file_pandas = read_file_pandas('example.csv')

    # Output the results to the console
    output_text(f"Text from console: {text_from_console}")
    output_text(f"Text from built-in file reading: {text_from_file_builtin}")
    output_text(f"Text from pandas file reading:\n{df_from_file_pandas}")

    # Write the results to a file using Python's built-in functionality
    content_to_write = f"Text from console: {text_from_console}\n"
    content_to_write += f"Text from built-in file reading: {text_from_file_builtin}\n"
    content_to_write += f"Text from pandas file reading:\n{df_from_file_pandas}"

    write_file('output.txt', content_to_write)

    # Write the pandas DataFrame result to a CSV file
    write_file_pandas('output_pandas.csv', df_from_file_pandas)

if __name__ == "__main__":
    main()