import numpy as np


def main():
    pass


def save_to_flask_compare(
    y_pred, y_test
):  # To use it in Flask app for prediction and comparing the results
    y_pred_path = "./../app/static/data/predicted_value.csv"
    y_test_path = "./../app/static/data/ground_truth.csv"

    # Predicting the y_test using the model

    # Save the numpy array to a CSV file - for predicting in the Flask app
    # The prediction input is the x_test and the ground truth is the y_test
    np.savetxt(y_pred_path, y_pred, delimiter=",")
    np.savetxt(y_test_path, y_test, delimiter=",")


def save_to_flask_sample(df):
    path = "./../app/static/data/final_sample.csv"
    # Save the DataFrame to a CSV file - for displaying in the Flask app(webpage)
    df.to_csv(path, index=False)


if __name__ == "__main__":
    main()
