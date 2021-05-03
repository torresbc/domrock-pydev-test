""" Challenge

Python Developer test for DomRock company.

"""
import pandas as pd


def read_excel_file(path):
    """Read excel file from a specific path.

    Parameters
    ----------
    path : str
          File path.

    Returns
    -------
    df : pd.DataFrame
         Raw data.
    """
    df = pd.read_excel(path)
    return df


def group_daily(df, columns, sum):
    """Group dataframe by specific columns and aggregate it by sum.

    Parameters
    ----------
    df : pd.DataFrame
         Input data.
    columns : list
              List of columns to group by.
    sum : list
          List of columns to aggregate.

    Returns
    -------
    df : pd.DataFrame
         Grouped data.
    """
    df = df.groupby(columns)[sum].sum()
    return df.reset_index()


def normalize_columns_index(df):
    """Normalize multiIndex columns and join both columns name with underscore (_).

    Parameters
    ----------
    df : pd.DataFrame
         Input data.

    Returns
    -------
    df : pd.DataFrame
         Normalized columns data.
    """
    df.columns = ["_".join(col) for col in df.columns]
    return df


def pivot_tables(df, index, columns, values, aggfunc):
    """Pivot table by specific parameters.

    Parameters
    ----------
    df : pd.DataFrame
         Input data.
    index: list
           List of index columns.
    columns: str
             Name of pivoted column.
    values: list
            List of values columns.
    aggfunc: str
             Type of aggregated function.

    Returns
    -------
    df : pd.DataFrame
         Pivoted data.
    """
    df = df.pivot_table(index=index, columns=columns, values=values, aggfunc=aggfunc).fillna(0)
    df = normalize_columns_index(df)
    return df.reset_index()


def filter_columns(df, columns):
    """Filter and reorder columns.

    Parameters
    ----------
    df : pd.DataFrame
         Input data.

    Returns
    -------
    df : pd.DataFrame
         Filtered data.
    """
    return df[columns]


def merge_tables(df_left, df_right, left_on, right_on, how="left",):
    """Merge two different dataframes.

    Parameters
    ----------
    df_left : pd.DataFrame
              Input data.
    df_right : pd.DataFrame
               Input data.
    left_on: str
             Key column name from df_left dataframe.
    right_on: str
             Key column name from df_right dataframe.
    how: str
         Merge type.

    Returns
    -------
    df : pd.DataFrame
         Merged data.
    """
    df = df_left.merge(df_right, how=how, left_on=left_on, right_on=right_on)
    return df


def normalize_date_column(df, column):
    """Normalize date column to dd/mm/YYYY standard.

    Parameters
    ----------
    df : pd.DataFrame
         Input data.
    column: str
            Date column name.

    Returns
    -------
    df : pd.DataFrame
         Normalized data.
    """
    df[column] = df[column].dt.strftime("%d/%m/%Y")
    return df


def export_excel_file(df, path):
    """Merge two different dataframes.

    Parameters
    ----------
    df : pd.DataFrame
         Input data.
    path : pd.DataFrame
           Path to export the final dataframe.
    """
    df.to_excel(path)


def main():
    print(f"LOG: LOADING AND TRANSFORMING MovtoITEM DATAFRAME")
    path = f"../data/MovtoITEM.xlsx"
    df_mov = read_excel_file(path)

    group = {
        "columns": ["item", "tipo_movimento", "data_lancamento"],
        "sum": ["quantidade", "valor"]
    }
    df_mov = group_daily(df_mov, **group)

    pivot = {
        "index": ["item", "data_lancamento"],
        "columns": "tipo_movimento",
        "values": ["quantidade", "valor"],
        "aggfunc": "sum"
    }
    df_mov = pivot_tables(df_mov, **pivot)

    print(f"LOG: LOADING SaldoITEM DATAFRAME")
    path = f"../data/SaldoITEM.xlsx"
    df_balance = read_excel_file(path)

    print(f"LOG: MERGING SaldoITEM AND MovtoITEM DATAFRAMES")
    df = merge_tables(df_mov, df_balance, "item", "item")

    print(f"LOG: TRANSFORMING FINAL DATAFRAME")
    columns = ["item", "data_lancamento", "quantidade_Ent", "valor_Ent", "quantidade_Sai", "valor_Sai",
               "qtd_inicio", "valor_inicio", "qtd_final", "valor_final"]
    df = filter_columns(df, columns)

    df = normalize_date_column(df, "data_lancamento")

    print(f"LOG: EXPORTING FINAL DATAFRAME")
    path = f"../data/output/output_file.xlsx"
    export_excel_file(df, path)


if __name__ == "__main__":
    main()