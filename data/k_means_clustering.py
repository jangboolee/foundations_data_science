import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Read data
df = pd.read_csv(os.path.join('.', 'data', 
                              'banknote-authentication-dataset-.csv'))

# Calculate statistical measures
# print(df.describe())

