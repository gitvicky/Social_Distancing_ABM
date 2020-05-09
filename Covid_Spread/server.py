from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from .model import SocialDistancing_Model

COLORS = {  
            "Total": "#feb308",
            "Healthy": "#39ad48",
            "Sick": "#d9544d",
            "Immune": "#3b5b92"
        }


def portrayal(Individual):
    if Individual is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = Individual.get_pos()
    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = COLORS[Individual.condition]
    return portrayal


canvas_element = CanvasGrid(portrayal, 100, 100 , 500, 500)
tree_chart = ChartModule([{"Label": label, "Color": color} for (label, color) in COLORS.items()])
#pie_chart = PieChartModule([{"Label": label, "Color": color} for (label, color) in COLORS.items()])

model_params = {
    "N": 10000,
    "height": 100,
    "width": 100,
    "Initial_Outbreak": UserSettableParameter("slider", "Initial Outbreak (%)", 0.1, 0.01, 1.0, 0.01),
    "TR": UserSettableParameter("slider", "Transmission Rate (%)", 0.5, 0.1, 1.0, 0.01),
    "RT": UserSettableParameter("slider", "Recovery Time (days)", 28, 14, 28),
    "MR": UserSettableParameter("slider", "Mortality Rate (%)", 0.02, 0.01, 0.05, 0.001),
    "Policy": UserSettableParameter("slider", "Social Distancing (%)", 0.5, 0.0, 1.0, 0.05)


}
server = ModularServer(SocialDistancing_Model, [canvas_element, tree_chart], "Covd-19 Spread", model_params)
