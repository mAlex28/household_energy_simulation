from visualisation.server import server

# Set the season manually
server.model_kwargs = {"num_households": 100, "season": 'winter'}

# Run the server
server.port = 8521
server.launch()
