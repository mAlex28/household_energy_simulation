from mesa import Agent
import numpy as np

class Household(Agent):
    def __init__(self, unique_id, model, house_type, num_people):
        super().__init__(unique_id, model)
        self.house_type = house_type
        self.num_people = num_people
        self.energy_saving = np.random.choice(['Yes', 'No'], p=[0.3, 0.7])
        self.season = model.season
        self.electricity_usage = self.calculate_energy_usage('electricity')
        self.gas_usage = self.calculate_energy_usage('gas')

    def calculate_energy_usage(self, energy_type):
        mean, std = self.model.energy_usage_params[self.house_type][energy_type]
        usage = np.random.normal(mean, std)
        if self.season == 'winter':
            usage *= 1.36
        if self.energy_saving == 'Yes':
            usage *= 0.9
        return max(usage, 0)

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        self.electricity_usage = self.calculate_energy_usage('electricity')
        self.gas_usage = self.calculate_energy_usage('gas')
