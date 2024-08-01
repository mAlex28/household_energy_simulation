import numpy as np

# Define seasons
seasons = ['winter', 'spring', 'summer', 'autumn']

# Temperature thresholds for appliance control
temperature_thresholds = {
    'winter': {
        'hvac_on': 18, 'hvac_off': 22,
        'water_heater_on': 24, 'water_heater_off': 30,
        'dryer_on': None, 'dryer_off': None,
        'washing_machine_on': None, 'washing_machine_off': None,
        'dishwasher_on': None, 'dishwasher_off': None,
        'lights_on': None, 'lights_off': None
    },
    'spring': {
        'hvac_on': 15, 'hvac_off': 20,
        'water_heater_on': 24, 'water_heater_off': 30,
        'dryer_on': None, 'dryer_off': None,
        'washing_machine_on': None, 'washing_machine_off': None,
        'dishwasher_on': None, 'dishwasher_off': None,
        'lights_on': None, 'lights_off': None
    },
    'summer': {
        'hvac_on': 25, 'hvac_off': 22,
        'water_heater_on': 24, 'water_heater_off': 30,
        'dryer_on': None, 'dryer_off': None,
        'washing_machine_on': None, 'washing_machine_off': None,
        'dishwasher_on': None, 'dishwasher_off': None,
        'lights_on': None, 'lights_off': None
    },
    'autumn': {
        'hvac_on': 15, 'hvac_off': 20,
        'water_heater_on': 24, 'water_heater_off': 30,
        'dryer_on': None, 'dryer_off': None,
        'washing_machine_on': None, 'washing_machine_off': None,
        'dishwasher_on': None, 'dishwasher_off': None,
        'lights_on': None, 'lights_off': None
    }
}

# Define actions and their indices
actions = [
    'hvac_on', 'hvac_off',
    'water_heater_on', 'water_heater_off',
    'dryer_on', 'dryer_off',
    'dishwasher_on', 'dishwasher_off',
    'washing_machine_on', 'washing_machine_off',
    'lights_on', 'lights_off'
]
action_indices = {action: idx for idx, action in enumerate(actions)}

# Initialize Q-table with zeros
q_table = np.zeros((len(seasons), len(actions)))

# Define rewards based on temperature thresholds and appliance actions
# Rewards are based on factors like comfort, cost, and efficiency
rewards = {
    # HVAC rewards
    ('winter', 'hvac_on'): 1.0,   # Reward for heating during winter
    ('winter', 'hvac_off'): -0.5, # Penalty for turning off heating
    ('summer', 'hvac_on'): -0.5,  # Penalty for turning on heating
    ('summer', 'hvac_off'): 0.5,  # Reward for turning off heating
    # Water heater rewards
    ('winter', 'water_heater_on'): 0.5,  # Need more hot water
    ('winter', 'water_heater_off'): -0.3, # Penalty for lack of hot water
    ('summer', 'water_heater_on'): -0.3, # Less need for hot water
    ('summer', 'water_heater_off'): 0.3, # Saving energy in summer
    # Dryer rewards
    ('winter', 'dryer_on'): 0.3,  # Needed due to cold weather
    ('winter', 'dryer_off'): 0.1, # Minimal penalty for off
    ('summer', 'dryer_on'): -0.2, # Penalty for energy use
    ('summer', 'dryer_off'): 0.2, # Saving energy
    # Dishwasher rewards
    ('winter', 'dishwasher_on'): 0.2,  # Regular use
    ('winter', 'dishwasher_off'): 0.1, # Slight saving
    ('summer', 'dishwasher_on'): 0.2,  # Regular use
    ('summer', 'dishwasher_off'): 0.1, # Slight saving
    # Washing machine rewards
    ('winter', 'washing_machine_on'): 0.2,  # Regular use
    ('winter', 'washing_machine_off'): 0.1, # Slight saving
    ('summer', 'washing_machine_on'): 0.2,  # Regular use
    ('summer', 'washing_machine_off'): 0.1, # Slight saving
    # Lights rewards
    ('winter', 'lights_on'): 0.2,   # Need more lighting
    ('winter', 'lights_off'): -0.1, # Penalty for darkness
    ('summer', 'lights_on'): -0.1,  # Penalty for energy use
    ('summer', 'lights_off'): 0.1   # Reward for saving energy
}

# Q-learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

# Function to select the best action based on the current Q-table
def get_optimal_action(state):
    state_idx = seasons.index(state)
    return np.argmax(q_table[state_idx])

# Q-learning update function
def q_learning_step(current_state, action, reward, next_state):
    current_idx = seasons.index(current_state)
    action_idx = action_indices[action]
    next_idx = seasons.index(next_state)
    
    best_next_action = np.max(q_table[next_idx])
    q_table[current_idx, action_idx] += alpha * (reward + gamma * best_next_action - q_table[current_idx, action_idx])

# Simulation loop for Q-learning
for episode in range(1000):
    current_state = np.random.choice(seasons)
    action = actions[np.random.choice(len(actions))] if np.random.rand() < epsilon else actions[get_optimal_action(current_state)]
    
    # Simulate current temperature (for the example, we randomly assign temperatures)
    current_temp = np.random.uniform(-5, 35)  # Wide range covering all seasons

    # Determine next state and reward based on temperature and action
    thresholds = temperature_thresholds[current_state]
    if action in thresholds:
        if action.endswith('on') and (thresholds[action] is not None and current_temp < thresholds[action]):
            next_state = current_state
            reward = rewards.get((current_state, action), 0)
        elif action.endswith('off') and (thresholds[action] is not None and current_temp > thresholds[action]):
            next_state = current_state
            reward = rewards.get((current_state, action), 0)
        else:
            next_state = np.random.choice(seasons)
            reward = -1  # Penalty for inefficient action
    else:
        next_state = np.random.choice(seasons)
        reward = -1  # Penalty for non-optimal action
    
    q_learning_step(current_state, action, reward, next_state)

# Display the updated Q-table
print("Updated Q-table:")
print(q_table)
