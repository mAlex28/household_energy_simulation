from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import numpy as np
from models.agent import Household



class HouseholdEnergyModel(Model):
    def __init__(self, num_households, season):
        self.num_agents = num_households
        self.season = season
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width=10, height=10, torus=False)

        # Energy usage parameters annually (kWh)
        self.energy_usage_params = {
            'Flat/1-bedroom': {'electricity': (1800, 270), 'gas': (7500, 1125)},
            'Medium 2-3 bedroom': {'electricity': (2700, 405), 'gas': (11500, 1725)},
            '4+ bedroom': {'electricity': (4100, 615), 'gas': (17000, 2550)}
        }

        household_sizes = [1]*29 + [2]*47 + [3]*26 + [4]*23 + [5]*9 + [6]*3
        np.random.shuffle(household_sizes)

        for i in range(self.num_agents):
            house_type = self.house_type(household_sizes[i])
            num_people = household_sizes[i]
            a = Household(i, self, house_type, num_people)
            self.schedule.add(a)

            # Add agent to a random grid cell
            x = self.random.randint(0, self.grid.width - 1)
            y = self.random.randint(0, self.grid.height - 1)
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
            agent_reporters={"Electricity Usage": "electricity_usage",
                             "Gas Usage": "gas_usage"}
        )
# test
    def house_type(self, num_people):
        if num_people == 1:
            return 'Flat/1-bedroom'
        elif num_people == 2 or num_people == 3:
            return 'Medium 2-3 bedroom'
        else:
            return '4+ bedroom'

    #TODO: model agent behaviour

    def step(self):
        self.schedule.step()
        # Collect data at each step
        self.datacollector.collect(self)

    def collect_data(self):
        data = []
        for agent in self.schedule.agents:
            data.append([
                agent.house_type, agent.num_people, np.round(agent.electricity_usage, 2),
                np.round(agent.gas_usage, 2), agent.energy_saving
            ])
        return data
