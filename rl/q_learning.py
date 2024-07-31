import numpy as np
import random

# Parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
num_episodes = 1000

# Define states (e.g., different times of the day or energy pricing levels)
states = ['morning', 'afternoon', 'evening', 'night']
state_indices = {state: idx for idx, state in enumerate(states)}

# Define actions (control each appliance)
actions = [
    'hvac_on', 'hvac_off',
    'water_heater_on', 'water_heater_off',
    'washer_on', 'washer_off',
    'lights_on', 'lights_off'
]
action_indices = {action: idx for idx, action in enumerate(actions)}

# Initialize Q-table with zeros
q_table = np.zeros((len(states), len(actions)))

# Rewards for each state-action pair
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

# Q-learning algorithm
def q_learning(num_episodes):
    for _ in range(num_episodes):
        state = random.choice(states)  # Start in a random state
        done = False

        while not done:
            # Choose action: explore or exploit
            if random.uniform(0, 1) < epsilon:
                action = random.choice(actions)  # Explore
            else:
                state_idx = state_indices[state]
                action_idx = np.argmax(q_table[state_idx])  # Exploit
                action = actions[action_idx]

            # Take action and observe reward and next state
            reward = rewards.get((state, action), 0)
            next_state = random.choice(states)  # Transition to a random next state

            # Update Q-value
            state_idx = state_indices[state]
            action_idx = action_indices[action]
            next_state_idx = state_indices[next_state]
            best_next_action_idx = np.argmax(q_table[next_state_idx])

            td_target = reward + gamma * q_table[next_state_idx, best_next_action_idx]
            td_error = td_target - q_table[state_idx, action_idx]
            q_table[state_idx, action_idx] += alpha * td_error

            # Transition to the next state
            state = next_state

            # For simplicity, end each episode after one step
            done = True

# Run Q-learning
q_learning(num_episodes)

# Print the learned Q-table
print("Learned Q-table:")
print(q_table)
