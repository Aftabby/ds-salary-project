import numpy as np


def main():
    pass


def save_to_flask_compare(
    x_test, y_test
):  # To use it in Flask app for prediction and comparing the results
    x_path = "./../app/static/data/prediction_input.csv"
    y_path = "./../app/static/data/ground_truth.csv"

    # Save the numpy array to a CSV file - for predicting in the Flask app
    # The prediction input is the x_test and the ground truth is the y_test
    np.savetxt(x_path, x_test, delimiter=",")
    np.savetxt(y_path, y_test, delimiter=",")


def save_to_flask_sample(df):
    path = "./../app/static/data/final_sample.csv"
    # Save the DataFrame to a CSV file - for displaying in the Flask app(webpage)
    df.to_csv(path, index=False)


if __name__ == "--main__":
    main()
