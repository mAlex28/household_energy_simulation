import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data/household_energy_data.csv')

# View the first few rows
print(data.head())

# Plot the average electricity usage over time
data.groupby('Step')['Electricity Usage'].mean().plot()
plt.xlabel('Step')
plt.ylabel('Average Electricity Usage')
plt.title('Average Electricity Usage Over Time')
plt.show()

# Compare electricity usage in winter vs. summer
winter_data = data[data['Season'] == 'winter']
summer_data = data[data['Season'] == 'summer']

print("Average Winter Electricity Usage:", winter_data['Electricity Usage'].mean())
print("Average Summer Electricity Usage:", summer_data['Electricity Usage'].mean())

# Compare energy-saving vs. non-energy-saving households
energy_saving_data = data[data['Energy Saving'] == 'Yes']
non_energy_saving_data = data[data['Energy Saving'] == 'No']

print("Average Electricity Usage (Energy Saving):", energy_saving_data['Electricity Usage'].mean())
print("Average Electricity Usage (Non-Energy Saving):", non_energy_saving_data['Electricity Usage'].mean())

# Plot the results
fig, ax = plt.subplots()
categories = ['Winter', 'Summer', 'Energy Saving', 'Non-Energy Saving']
values = [
    winter_data['Electricity Usage'].mean(),
    summer_data['Electricity Usage'].mean(),
    energy_saving_data['Electricity Usage'].mean(),
    non_energy_saving_data['Electricity Usage'].mean()
]

ax.bar(categories, values)
plt.xlabel('Category')
plt.ylabel('Average Electricity Usage')
plt.title('Energy Usage Analysis')
plt.show()
