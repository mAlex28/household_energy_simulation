from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import Slider
from models.model import HouseholdEnergyModel
from visualisation.portrayal import portrayAgent

grid = CanvasGrid(portrayAgent, 50, 50, 300, 300)

chart = ChartModule(
    [{"Label": "Electricity Usage", "Color": "Black"}],
    data_collector_name="datacollector"
)

# Assuming default season is 'winter'
server = ModularServer(
    HouseholdEnergyModel,
    [grid, chart],
    "Household Energy Model",
    {"num_households": Slider('Number of households', 137, 10, 200, 1), 'season': 'winter'}
)
