# Functions to load and return data
import pandas as pd

def load_diabetes_data(url=None):
    """
    Loads the Pima Indians Diabetes Dataset from a specified URL or path.
    
    Parameters:
        url (str): Optional URL or path to the dataset.
        
    Returns:
        pd.DataFrame: Loaded DataFrame with appropriate column names.
    """
    if url is None:
        url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    
    columns = [
        'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
        'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
    ]
    df = pd.read_csv(url, names=columns)
    return df
