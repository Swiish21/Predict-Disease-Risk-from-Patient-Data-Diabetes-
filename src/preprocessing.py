# Functions to clean and preprocess data
import pandas as pd

def clean_data(df):
    """
    Replaces 0s in specific columns with NaN, then fills with median values.
    
    Parameters:
        df (pd.DataFrame): Raw diabetes data.
    
    Returns:
        pd.DataFrame: Cleaned data.
    """
    cols_with_zeroes = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols_with_zeroes] = df[cols_with_zeroes].replace(0, pd.NA)
    df.fillna(df.median(numeric_only=True), inplace=True)
    return df
