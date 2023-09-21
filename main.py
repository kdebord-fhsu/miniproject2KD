# INF601 - Advanced Programming in Python
# Kelton DeBord
# Mini Project 2
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
#What League of Legends class has the highest win rate?

# Create our /charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

#Converts League of Legends csv to readable file
data = pd.read_csv('LoL12.1.csv', delimiter=';')

#Removes the % sign from csv columns and replaces with a numeric value
data['Win %'] = data['Win %'].str.rstrip('%').astype(float)

#Groups data by their classes and calculates the mean win rate for each class
class_win_rates = data.groupby('Class')['Win %'].mean()

# Define custom colors for bars
colors = ['skyblue', 'lightcoral', 'lightgreen', 'orange', 'lightblue', 'pink', 'yellow', 'purple', 'lightgray', 'gold']

# Create a bar chart with custom colors and bar width
plt.figure(figsize=(10, 6))
class_win_rates.plot(kind='bar', color=colors, width=0.7)

#Groups data by their classes and calculates the mean win rate for each class
class_win_rates = data.groupby('Class')['Win %'].mean()

# Add a title and labels to the chart
plt.title('League of Legends Win Rates by Class')
plt.xlabel('Class')
plt.ylabel('Win Rate')
plt.xticks(rotation=45)
plt.tight_layout()

# Add data labels above each bar
for i, v in enumerate(class_win_rates):
    plt.text(i, v + 1, f'{v:.2f}%', ha='center', va='bottom', fontsize=10, color='black')

# Save the chart as an image
plt.savefig('charts/league_of_legends_class_win_rates.png')

# Displays the created chart
plt.show()

