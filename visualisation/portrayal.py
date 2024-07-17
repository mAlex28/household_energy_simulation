def portrayAgent(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "rect",
        "w": 1,
        "h": 1,
        "Filled": "true",
        "r": 0.5,
        "Layer": 0
    }
    if agent.house_type == 'Flat/1-bedroom':
        portrayal["Color"] = "blue"
    elif agent.house_type == 'Medium 2-3 bedroom':
        portrayal["Color"] = "green"
    else:
        portrayal["Color"] = "red"
    return portrayal
