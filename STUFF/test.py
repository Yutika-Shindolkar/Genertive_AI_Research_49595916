This is a python script for data cleaning
import pandas as pd
import numpy as np
# Load the dataset
data = pd.read_csv('dataset.csv')
# Check for missing values
print(data.isnull().sum())