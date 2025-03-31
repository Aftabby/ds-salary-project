import pickle
import numpy as np
import pandas as pd


def main():
    pass


def load_model(path="./models/trained_model.pickle"):
    """
    Load the model from the specified path.
    """
    with open(path, "rb") as file:
        models = pickle.load(file)
        model = models[
            "model"
        ]  # As we saved the model with the key "model" in a dictionary within pickle file (in model_building.py)
    return model


def load_prediction_input(path="./static/data/prediction_input.csv"):
    """
    Load the prediction input data from the specified path.
    """
    data = np.genfromtxt(path, delimiter=",")
    data = data.reshape(
        149, -1
    )  # Reshape the array to have one row and multiple columns
    return data


def load_ground_truth(path="./static/data/ground_truth.csv"):
    """
    Load the ground truth data from the specified path.
    """
    data = np.genfromtxt(path, delimiter=",")  # Skip the header row
    data = data.reshape(-1, 1)  # Reshape the array to have one row and multiple columns
    return data


def load_sample(path="./static/data/final_sample.csv"):
    """
    Load the sample data from the specified path.
    """
    df = pd.read_csv(path)
    return df


if __name__ == "__main__":
    main()
