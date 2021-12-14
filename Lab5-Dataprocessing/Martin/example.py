import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('electricity.csv')

# Convert the column to datetime
df['Tidsperiod'] = pd.to_datetime(df['Tidsperiod'])

# Sort values by the time column
df.sort_values(by='Tidsperiod', axis=0, inplace=True)

# Extract the respective area
a1 = df[df['Elomr'] == '1. Norra'].copy()
a2 = df[df['Elomr'] == '2. Norra Mellan'].copy()
a3 = df[df['Elomr'] == '3. Södra Mellan'].copy()
a4 = df[df['Elomr'] == '4. Södra'].copy()

# Set the index, drop the unnecessary column and rename the price column
a1.set_index('Tidsperiod', inplace=True) 
a1.drop(['Elomr'], axis=1, inplace=True)
a1.rename(columns={'Pris': 'Pris Norra'}, inplace=True)

a2.set_index('Tidsperiod', inplace=True) 
a2.drop(['Elomr'], axis=1, inplace=True)
a2.rename(columns={'Pris': 'Pris Norra Mellan'}, inplace=True)

a3.set_index('Tidsperiod', inplace=True) 
a3.drop(['Elomr'], axis=1, inplace=True)
a3.rename(columns={'Pris': 'Pris Södra Mellan'}, inplace=True)

a4.set_index('Tidsperiod', inplace=True) 
a4.drop(['Elomr'], axis=1, inplace=True)
a4.rename(columns={'Pris': 'Pris Södra'}, inplace=True)

# Concatenate all frames
df = pd.concat([a1, a2, a3, a4], axis=1)

# Plot
df.plot()
plt.show()
