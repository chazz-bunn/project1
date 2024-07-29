import pandas as pd
from tabulate import tabulate

def make_table(table, cols) -> str:
    df = pd.DataFrame(
        table, 
        columns = cols,
    )
    return tabulate(df, showindex=False, headers=df.columns)