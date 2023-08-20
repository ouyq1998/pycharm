import pandas as pd


def generate_create_table_statement(table_name, excel_file_path):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path, dtype={'Length': str, 'Nullable': str})

    # Initialize the create table statement
    create_table_stmt = f"CREATE TABLE {table_name} (\n"

    # Identify the primary key column (where "Primary Key" column has value "1" or "Y")
    primary_key_column = df[df["Primary Key"].astype(str).str.lower().isin(['1', 'y'])]['Column Name'].tolist()

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        column_name = row['Column Name']
        data_type = row['Data Type']
        length = row['Length'] if not pd.isnull(row['Length']) else ''
        nullable = row['Nullable'] if not pd.isnull(row['Nullable']) else 'True'

        # Construct the column definition
        column_def = f"{column_name} {data_type}"

        if length:
            column_def += f"({length})"

        if nullable == 'False':
            column_def += " NOT NULL"

        # Add the column definition to the create table statement
        create_table_stmt += f"    {column_def},\n"

    # Add the primary key constraint to the create table statement
    if primary_key_column:
        create_table_stmt += f"    PRIMARY KEY ({', '.join(primary_key_column)}),\n"

    # Remove the trailing comma and newline
    create_table_stmt = create_table_stmt.rstrip(",\n")

    # Add the closing parenthesis to complete the create table statement
    create_table_stmt += "\n);"

    return create_table_stmt


# Example usage
excel_file_path = 'sample.xlsx'
table_name = 'example_table'
create_table_statement = generate_create_table_statement(table_name, excel_file_path)
print(create_table_statement)
