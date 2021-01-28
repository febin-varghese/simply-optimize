# Reference: https://stackabuse.com/gradient-descent-in-python-implementation-and-theory/

import numpy as np
import plotly.graph_objects as go

# User defined modules
from test_functions import available_functions


class GradientDescent:
    def __init__(self, objective_function, initial_point, precision=1e-6, max_iter=10000, rate=0.1, momentum=0.1):
        self.objective_fn = objective_function
        self.initial_point = np.array(initial_point)
        self.precision = precision
        self.max_iter = max_iter
        self.learning_rate = rate
        self.momentum = momentum

        self.step_size = 1
        self.iters = 0
        self.points_history = np.array(initial_point)
        self.fun_history = np.array(objective_function.calculate(initial_point))
        self.name = "Gradient Descent"

    def optimize(self):
        current_point = self.initial_point
        delta_pts = np.zeros(current_point.shape)  # change in points
        print("Starting point = ", np.round(self.initial_point, 2))
        while self.step_size > self.precision and self.iters < self.max_iter:
            # print("Iteration: ", self.iters)
            delta_pts = -self.learning_rate * self.objective_fn.gradient(current_point) + self.momentum * delta_pts
            current_point = current_point + delta_pts
            self.update_history(current_point)

            self.step_size = np.absolute(self.fun_history[-1] - self.fun_history[-2])
            self.iters += 1
        return {"minimum": self.fun_history[-1], "position": current_point, "path": self.optimization_path()}

    def update_history(self, new_point):
        self.points_history = np.vstack((self.points_history, new_point))
        self.fun_history = np.vstack((self.fun_history, self.objective_fn.calculate(new_point)))

    def print_output(self):
        minimum = np.round(self.fun_history[-1], 3)
        position = np.round(self.points_history[-1], 3)
        print(f'Predicted minimum = {minimum} at {position}')

    def optimization_path(self):
        return go.Scatter(x=self.points_history[:, 0], y=self.points_history[:, 1], mode="lines+markers")


def available_optimizers():
    return {"Gradient Descent": GradientDescent}


def optimize_function(point, fn_name: str, alg_name: str):
    test_fns = available_functions()
    selected_fn = test_fns[fn_name]
    optimizers = available_optimizers()
    selected_alg = optimizers[alg_name]
    optimizer_obj = selected_alg(selected_fn(), point)
    output = optimizer_obj.optimize()
    optimizer_obj.print_output()
    minimum = np.round(output["minimum"], 3)
    position = np.round(output["position"], 3)
    return minimum[0], (position[0], position[1]), output["path"]


if __name__ == "__main__":
    funs = available_functions()
    opt_algorithms = available_optimizers()
    for alg_name, algs in opt_algorithms.items():
        print(alg_name)
        for fn_name, test_fn in funs.items():
            print(fn_name)
            fun_object = test_fn()
            opt_obj = algs(fun_object, np.random.uniform(fun_object.lower_limit, fun_object.upper_limit, 2))
            _ = opt_obj.optimize()
            opt_obj.print_output()
