import numpy as np
import plotly.graph_objects as go


class Ackley:
    def __init__(self):
        """
        2D Ackley function
        """
        self.name = "Ackley"
        self.global_min = 0.0
        self.global_min_parameters = (0, 0)
        self.upper_limit = 5
        self.lower_limit = -5
        self.figure = go.Figure()

    def calculate(self, X):
        x1 = X[0]
        x2 = X[1]
        part_1 = -0.2 * np.sqrt(0.5 * (x1 * x1 + x2 * x2))
        part_2 = 0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))
        value = np.exp(1) + 20 - 20 * np.exp(part_1) - np.exp(part_2)
        return value

    def gradient(self, X):
        """
        Gradient of Ackley function
        :param X: 2D point
        :return: gradient
        """
        def part1_grad(x, y):
            part_1 = -0.2 * np.sqrt(0.5 * (x * x + y * y))
            return (2 * x * np.exp(part_1)) / (np.sqrt(((x ** 2 + y ** 2) / 2)))

        def part2_grad(x, y):
            part_2 = 0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))
            return 0.25 * part_2 * np.sin(2 * np.pi * x) * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))

        x1 = X[0]
        x2 = X[1]
        x1_grad = part1_grad(x1, x2) + part2_grad(x1, x2)
        x2_grad = part1_grad(x2, x1) + part2_grad(x2, x1)
        gradient = [x1_grad, x2_grad]
        return np.array(gradient)

    def plot(self):
        x = np.linspace(self.lower_limit, self.upper_limit, 100)
        y = np.linspace(self.lower_limit, self.upper_limit, 100)
        xgrid, ygrid = np.meshgrid(x, y)
        zgrid = self.calculate([xgrid, ygrid])
        self.figure.add_trace(go.Contour(x=x, y=y, z=zgrid))
        self.figure.layout.autosize = True
        return self.figure


class Sphere:
    def __init__(self):
        """
        2D Sphere function
        """
        self.name = "Sphere"
        self.global_min = 0.0
        self.global_min_parameters = (0, 0)
        self.upper_limit = 10
        self.lower_limit = -10
        self.figure = go.Figure()

    def calculate(self, X):
        x1 = X[0]
        x2 = X[1]
        value = np.square(x1) + np.square(x2)
        return value

    def gradient(self, X: np.ndarray):
        """
        Gradient of the Sphere function
        :param X: 2D point
        :return: Gradient
        """
        return 2 * X

    def plot(self):
        x = np.linspace(self.lower_limit, self.upper_limit, 100)
        y = np.linspace(self.lower_limit, self.upper_limit, 100)
        xgrid, ygrid = np.meshgrid(x, y)
        zgrid = self.calculate([xgrid, ygrid])
        self.figure.add_trace(go.Contour(x=x, y=y, z=zgrid))
        self.figure.layout.autosize = True
        return self.figure


def available_functions():
    return {"Ackley": Ackley, "Sphere": Sphere}