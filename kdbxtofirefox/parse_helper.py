import pandas as pd
import numpy as np
import kdbxtofirefox.csv_types as types
import time
"""
Parse kdbs and or firefox password databases
"""

#format defining column variables
#keepass csv 1.x
kdbx_col = np.array(["Account","Login Name","Password","Web Site","Comments"])
#firefox browser 90.0 
firefox_col = np.array(["url","username","password","httpRealm","formActionOrigin","guid","timeCreated","timeLastUsed","timePasswordChanged"])

def checkIfKdbx(file_in: str) -> types.Types:
    """
    Checks if csv is kdbx or firefox format

    Args:
        file (string) : csv file location 

    Returns:
        type (csv_types.Types) : this types are used to identify the csv format
    """
    if not file_in.endswith(".csv"):
        raise Exception("filename should end with .csv")
    df = pd.read_csv(file_in,nrows=1)
    cols = df.columns.to_numpy()
    print("cols ",cols)
    if np.array_equal(firefox_col,cols):
        return types.Types.FIREFOX
    elif np.array_equal(kdbx_col,cols):
        return types.Types.KDBX
    return types.Types.ERROR

def convertToKdbx(file_in: str) -> str:
    """
    Convert firefox csv to kdbx csv.
    Argument must be firefox csv formal file path 

    Args:
        file (str) : input csv path

    Returns: 
        csv (np.array) : csv np.array ready to write to a file
    """
    if not file_in.endswith(".csv"):
        raise Exception("filename should end with .csv")
    df = pd.read_csv(file_in)
    head_file = np.empty(shape=(0,5),dtype=str)
    #append header
    head_file = np.vstack((kdbx_col.reshape((1,len(kdbx_col))),head_file))
    comment = np.array([firefox_col[6]+" : "+str(i) for i in df[firefox_col[6]]])
    body_file = np.vstack((df[firefox_col[0]],df[firefox_col[1]],df[firefox_col[2]],df[firefox_col[0]],comment))
    conv_file = np.vstack((head_file,body_file.T))
    #write to file
    return conv_file
def convertToFirefox(file_in: str) -> str:
    """
    Convert kdbx csv to firefox csv.
    Argument must be kdbx csv formal file path 

    Args:
        file (str) : input csv file path

    Returns: 
        csv (str) : csv file string ready to write to a file
    """
    if not file_in.endswith(".csv"):
        raise Exception("filename should end with .csv")
    df = pd.read_csv(file_in)
    head_file = np.empty(shape=(0,len(firefox_col)),dtype=str)
    #append header
    empty = np.empty(shape=(1,len(df)),dtype=str)
    timeNow = np.array([int(time.time()*1000) for i in range(len(df))])
    head_file = np.vstack((firefox_col.reshape((1,len(firefox_col))),head_file))
    body_file = np.vstack((df[kdbx_col[3]],df[kdbx_col[1]],df[kdbx_col[2]],df[kdbx_col[3]],
        empty,empty,timeNow,timeNow,empty))
    conv_file = np.vstack((head_file,body_file.T))
    #write to file
    return conv_file