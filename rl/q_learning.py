import numpy as np

# Define states (seasons)
states = ['winter', 'spring', 'summer', 'autumn']
state_indices = {state: idx for idx, state in enumerate(states)}

# Define actions (control appliances)
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
q_table = np.zeros((len(states), len(actions)))

# Average energy usage (kWh)
average_usage = {
    'winter': {'electricity': 300, 'gas': 1000},
    'spring': {'electricity': 200, 'gas': 500},
    'summer': {'electricity': 250, 'gas': 300},
    'autumn': {'electricity': 280, 'gas': 700}
}

# Example action impact on energy usage (dummy values for demonstration)
action_impact = {
    'hvac_on': {'electricity': 50, 'gas': 20},
    'hvac_off': {'electricity': -10, 'gas': -5},
    'water_heater_on': {'electricity': 30, 'gas': 15},
    'water_heater_off': {'electricity': -5, 'gas': -10},
    'dryer_on': {'electricity': 40, 'gas': 0},
    'dryer_off': {'electricity': -10, 'gas': 0},
    'dishwasher_on': {'electricity': 25, 'gas': 0},
    'dishwasher_off': {'electricity': -5, 'gas': 0},
    'washing_machine_on': {'electricity': 20, 'gas': 0},
    'washing_machine_off': {'electricity': -5, 'gas': 0},
    'lights_on': {'electricity': 15, 'gas': 0},
    'lights_off': {'electricity': -5, 'gas': 0}
}

# Define rewards based on energy savings
def calculate_reward(state, action):
    usage = average_usage[state]
    impact = action_impact[action]
    new_electricity_usage = max(usage['electricity'] - impact['electricity'], 0)
    new_gas_usage = max(usage['gas'] - impact['gas'], 0)
    
    # Reward is the difference between average usage and new usage
    reward_electricity = (usage['electricity'] - new_electricity_usage) / usage['electricity']
    reward_gas = (usage['gas'] - new_gas_usage) / usage['gas']
    
    # Combine rewards for electricity and gas
    return reward_electricity + reward_gas

# Populate the Q-table with calculated reward values
for state in states:
    for action in actions:
        reward = calculate_reward(state, action)
        state_idx = state_indices[state]
        action_idx = action_indices[action]
        q_table[state_idx, action_idx] = reward

# Display the Q-table
print("Initial Q-table:")
print(q_table)

# Example Q-learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

# Simulate the Q-learning process
def q_learning(num_episodes=1000):
    for episode in range(num_episodes):
        state = np.random.choice(states)
        state_idx = state_indices[state]
        
        # Choose an action
        if np.random.rand() < epsilon:
            action_idx = np.random.choice(len(actions))
        else:
            action_idx = np.argmax(q_table[state_idx])
        
        action = actions[action_idx]
        
        # Simulate next state and reward (this would be data-driven in practice)
        next_state = np.random.choice(states)
        next_state_idx = state_indices[next_state]
        reward = calculate_reward(state, action)
        
        # Update Q-table
        best_next_action_idx = np.argmax(q_table[next_state_idx])
        td_target = reward + gamma * q_table[next_state_idx, best_next_action_idx]
        td_error = td_target - q_table[state_idx, action_idx]
        q_table[state_idx, action_idx] += alpha * td_error
        
        # Move to the next state
        state = next_state
        state_idx = next_state_idx

# Run Q-learning
q_learning()

# Display the updated Q-table
print("Updated Q-table after Q-learning:")
print(q_table)
