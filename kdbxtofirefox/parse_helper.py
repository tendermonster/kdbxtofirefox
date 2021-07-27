import pandas as pd
import numpy as np
import csv_types as types
"""
Parse kdbs and or firefox password databases
"""

#format defining column variables
#keepass csv 1.x
kdbx_col = np.array(["Account","Login Name","Password","Web Site","Comments"])
#firefox browser 90.0 
firefox_col = np.array(["url","username","password","httpRealm","formActionOrigin","guid","timeCreated","timeLastUsed","timePasswordChanged"])

def checkIfKdbx(file: str) -> types.Types:
    """
    Checks if csv is kdbx or firefox format

    Args:
        file (string) : csv file location 

    Returns:
        type (csv_types.Types) : this types are used to identify the csv format
    """
    if not file.endswith(".csv"):
        raise Exception("filename should end with .csv")
    df = pd.read_csv(file)
    cols = df.columns.to_numpy()
    print("cols ",cols)
    if np.array_equal(firefox_col,cols):
        return types.Types.FIREFOX
    elif np.array_equal(kdbx_col,cols):
        return types.Types.KDBX
    return types.Types.ERROR

def convertToKdbx(file : str):
    pass

def convertToFirefox(file : str):
    pass