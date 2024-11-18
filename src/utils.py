def print_dataframe_summary(df):
    """
    Print a comprehensive summary of a Pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to summarize.
    """
    # Basic info
    print(f"Shape: {df.shape}")
    print(f"Number of Rows: {df.shape[0]}")
    print(f"Number of Columns: {df.shape[1]}")

    # Duplicate and null information
    print(f"Total Duplicates: {df.duplicated().sum()}")
    print(f"Total Null Values: {df.isnull().sum().sum()}")

    # Null values per column
    print("\nNull Values per Column:")
    print(df.isnull().sum().to_dict())

    # Columns with nulls
    null_columns = df.columns[df.isnull().any()].tolist()
    print("\nColumns with Nulls:")
    print(null_columns if null_columns else "None")

    # Data types and unique counts
    print("\nColumn Data Types:")
    print(df.dtypes.to_dict())

    print("\nUnique Values per Column:")
    print(df.nunique().to_dict())
