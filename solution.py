import pandas as pd

def is_valid_label(label: str) -> bool:
    if not label.strip(): return False
    return all(c.isalpha() or c == '_' for c in label)

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    df_result = df.copy()

    operations = {
        "*": "mul",
        "-": "sub",
        "+": "add"
    }

    if not is_valid_label(new_column): return pd.DataFrame([])
    
    for operator in operations:
        columns = role.replace(" ", "").split(operator)

        if len(columns) == 2:
            for column in columns:
                if not is_valid_label(column) or column not in df.columns: return pd.DataFrame([])

            first_column = columns[0]
            second_column = columns[1]
            
            method_name = operations[operator]
            df_result[new_column] = getattr(df_result[first_column], method_name)(df_result[second_column])

            return df_result
            
    return pd.DataFrame([])