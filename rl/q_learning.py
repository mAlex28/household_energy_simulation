import numpy as np
import random

# Define states and actions
states = ['morning', 'afternoon', 'evening', 'night']
state_indices = {state: idx for idx, state in enumerate(states)}

actions = [
    'hvac_on', 'hvac_off',
    'water_heater_on', 'water_heater_off',
    'washer_on', 'washer_off',
    'lights_on', 'lights_off'
]
action_indices = {action: idx for idx, action in enumerate(actions)}

# Initialize Q-table with zeros
q_table = np.zeros((len(states), len(actions)))

# Define rewards for each state-action pair
rewards = {
    # HVAC control
    ('morning', 'hvac_on'): -2,
    ('morning', 'hvac_off'): 1,
    ('afternoon', 'hvac_on'): -1,
    ('afternoon', 'hvac_off'): 2,
    ('evening', 'hvac_on'): -1,
    ('evening', 'hvac_off'): 2,
    ('night', 'hvac_on'): 1,
    ('night', 'hvac_off'): -1,
    
    # Water heater control
    ('morning', 'water_heater_on'): 1,
    ('morning', 'water_heater_off'): -1,
    ('afternoon', 'water_heater_on'): 1,
    ('afternoon', 'water_heater_off'): -1,
    ('evening', 'water_heater_on'): 2,
    ('evening', 'water_heater_off'): 0,
    ('night', 'water_heater_on'): 2,
    ('night', 'water_heater_off'): 0,
    
    # Washer control
    ('morning', 'washer_on'): -1,
    ('morning', 'washer_off'): 1,
    ('afternoon', 'washer_on'): 0,
    ('afternoon', 'washer_off'): 1,
    ('evening', 'washer_on'): 0,
    ('evening', 'washer_off'): 1,
    ('night', 'washer_on'): -1,
    ('night', 'washer_off'): 1,
    
    # Lighting control
    ('morning', 'lights_on'): 0,
    ('morning', 'lights_off'): 1,
    ('afternoon', 'lights_on'): 0,
    ('afternoon', 'lights_off'): 1,
    ('evening', 'lights_on'): -1,
    ('evening', 'lights_off'): 1,
    ('night', 'lights_on'): -2,
    ('night', 'lights_off'): 2,
}

# Parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

def initialize_state():
    # Randomly select a state from the defined states
    return random.choice(states)

def select_action(state):
    state_idx = state_indices[state]
    if random.uniform(0, 1) < epsilon:
        # Exploration: choose a random action
        return random.choice(actions)
    else:
        # Exploitation: choose the action with the highest Q-value for the given state
        return actions[np.argmax(q_table[state_idx])]

def perform_action(action):
    # For simplicity, we assume that performing an action will lead to a random new state
    # In a real scenario, this function should simulate the effects of the action on the environment
    return random.choice(states)

def calculate_reward(state, action, next_state):
    # Calculate reward based on predefined rewards
    state_action = (state, action)
    return rewards.get(state_action, 0)

def q_learning(episodes):
    for _ in range(episodes):
        state = initialize_state()
        done = False
        
        while not done:
            action = select_action(state)
            next_state = perform_action(action)
            reward = calculate_reward(state, action, next_state)
            
            # Update Q-value
            state_idx = state_indices[state]
            next_state_idx = state_indices[next_state]
            action_idx = action_indices[action]
            
            best_next_action = np.argmax(q_table[next_state_idx])
            q_table[state_idx, action_idx] = q_table[state_idx, action_idx] + alpha * (
                reward + gamma * q_table[next_state_idx, best_next_action] - q_table[state_idx, action_idx])
            
            state = next_state
            
            # Termination condition (if any)
            done = True  # For simplicity, we terminate after one iteration; adjust as needed

# Run Q-learning
q_learning(episodes=1000)

# Print the learned Q-table
print("Learned Q-table:")
print(q_table)
