# def portrayAgent(agent):
#     if agent is None:
#         return
#
#     portrayal = {
#         "Shape": "rect",
#         "w": 1,
#         "h": 1,
#         "Filled": "true",
#         "r": 0.5,
#         "Layer": 0
#     }
#     if agent.house_type == 'Flat/1-bedroom':
#         portrayal["Color"] = "blue"
#     elif agent.house_type == 'Medium 2-3 bedroom':
#         portrayal["Color"] = "green"
#     else:
#         portrayal["Color"] = "red"
#     return portrayal


def portrayAgent(agent):
    if agent.house_type == 'Flat/1-bedroom':
        portrayal = {"Shape": "rect", "Color": "blue", "Filled": "true", "Layer": 0, "w": 0.8, "h": 0.8}
    elif agent.house_type == 'Medium 2-3 bedroom':
        portrayal = {"Shape": "rect", "Color": "green", "Filled": "true", "Layer": 0, "w": 0.8, "h": 0.8}
    else:
        portrayal = {"Shape": "rect", "Color": "red", "Filled": "true", "Layer": 0, "w": 0.8, "h": 0.8}
    return portrayal
