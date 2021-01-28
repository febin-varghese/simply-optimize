import numpy as np
import plotly.graph_objects as go

class Ackley:
    def __init__(self):
        """
        2D Ackley function
        """
        self.name = "Ackley"
        self.global_min = 0.0
        self.global_min_parameters = [0, 0]
        self.upper_limit = 5
        self.lower_limit = -5

    def calculate(self, X):
        x1 = X[0]
        x2 = X[1]
        part_1 = -0.2 * np.sqrt(0.5 * (x1 * x1 + x2 * x2))
        part_2 = 0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))
        value = np.exp(1) + 20 - 20 * np.exp(part_1) - np.exp(part_2)
        return value

    def plot(self):
        x = np.linspace(self.lower_limit, self.upper_limit, 100)
        y = np.linspace(self.lower_limit, self.upper_limit, 100)
        xgrid, ygrid = np.meshgrid(x, y)
        zgrid = self.calculate([xgrid, ygrid])
        fig = go.Figure(data=go.Contour(x=x, y=y, z=zgrid))
        fig.layout.autosize = True
        return fig


class Sphere:
    def __init__(self):
        """
        2D Sphere function
        """
        self.name = "Sphere"
        self.global_min = 0.0
        self.global_min_parameters = [0, 0]
        self.upper_limit = 10
        self.lower_limit = -10

    def calculate(self, X):
        x1 = X[0]
        x2 = X[1]
        value = np.square(x1) + np.square(x2)
        return value

    def plot(self):
        x = np.linspace(self.lower_limit, self.upper_limit, 100)
        y = np.linspace(self.lower_limit, self.upper_limit, 100)
        xgrid, ygrid = np.meshgrid(x, y)
        zgrid = self.calculate([xgrid, ygrid])
        fig = go.Figure(data=go.Contour(x=x, y=y, z=zgrid))
        fig.layout.autosize = True
        # fig.update_layout(title=self.name)
        return fig


def available_functions():
    return {"Ackley": Ackley, "Sphere": Sphere}