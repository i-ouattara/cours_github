from fireducks import pandas as fpd
def upper(s):
    return s.upper()

def lower_case(input_string):
    return input_string.lower()

def show_dataframe_info(df: fpd.DataFrame)->None:
    print(f"Dataframe shape: {df.shape}")
    print(f"Dataframe columns: {df.columns}")
