from models.model import HouseholdEnergyModel
import pandas as pd

# Initialize the model
num_households = 100
season = 'winter'  # or 'summer'
model = HouseholdEnergyModel(num_households, season)

# Run the model for a certain number of steps
for i in range(100):  # or however many steps you want
    model.step()

# Collect the data
data = model.datacollector.get_agent_vars_dataframe()

# Save the data to a CSV file
data.to_csv('data/household_energy_data.csv')

# Display the first few rows of the DataFrame
print(data.head())
