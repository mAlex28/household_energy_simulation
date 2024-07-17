from models.model import HouseholdEnergyModel
import pandas as pd

# Initialize models for both seasons
winter_model = HouseholdEnergyModel(num_households=137, season='winter')
summer_model = HouseholdEnergyModel(num_households=137, season='summer')

# Run both models for the specified number of steps
for _ in range(10):
    winter_model.step()
    summer_model.step()

# Collect data from both models
winter_data = winter_model.collect_data()
summer_data = summer_model.collect_data()

# Combine data into a single DataFrame
combined_data = []
for winter, summer in zip(winter_data, summer_data):
    combined_data.append([
        winter[0],  # House Type
        winter[1],  # Number of People
        winter[2],  # Winter Electricity Usage
        summer[2],  # Summer Electricity Usage
        winter[3],  # Winter Gas Usage
        summer[3],  # Summer Gas Usage
        winter[4]   # Energy Saving Habits
    ])

# Create DataFrame
df = pd.DataFrame(combined_data, columns=[
    'House Type', 'Number of People', 'Winter Electricity Usage (kWh)',
    'Summer Electricity Usage (kWh)', 'Winter Gas Usage (kWh)',
    'Summer Gas Usage (kWh)', 'Energy Saving Habits'
])

# Save to CSV
df.to_csv('data/abm_household_energy_data.csv', index=False)

print(df.head())  # Display the first few rows of the DataFrame
