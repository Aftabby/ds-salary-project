# # DELETE LATER, IMPLEMENTED IT IN UTILS.PY

import numpy as np


def main():
    pass


path = "./../static/data/prediction_input.csv"  # Path to the CSV file
data = np.genfromtxt(path, delimiter=",")
data = data.reshape(149, -1)  # Reshape the array to have one row and multiple columns
print(data)  # Display the reshaped NumPy array
print(data.shape)  # Display the shape of the reshaped array
