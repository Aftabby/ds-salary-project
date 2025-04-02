# # DELETE LATER, IMPLEMENTED IT IN UTILS.PY

import numpy as np

path = "./../static/data/ground_truth.csv"  # Path to the CSV file
data = np.genfromtxt(path, delimiter=",")  # Skip the header row
data = data.reshape(-1, 1)  # Reshape the array to have one row and multiple columns
print(data)  # Display the reshaped NumPy array
print(data.shape)  # Display the shape of the reshaped array


"""
@ Give me a template for a webpage that will be dedicated for a data science and machine learning project. The project should contain all the things a portfolio project webpage should have step by step.
"""
