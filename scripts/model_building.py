import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.metrics import mean_absolute_error as mae


def main():
    models()


def load_data(path):
    df = pd.read_csv(path)

    # Choose relevant columns
    df_model = df[
        [
            "avg_salary",
            "Rating",
            "Size",
            "Type of ownership",
            "Industry",
            "Sector",
            "Revenue",
            "num_comp",
            "hourly",
            "employer_provided",
            "job_state",
            "same_state",
            "age",
            "python_yn",
            "spark",
            "aws",
            "excel",
            "job_simp",
            "seniority",
            "desc_len",
        ]
    ]

    # One hot encoding/ Pd.get_dummies
    df_dum = pd.get_dummies(df_model, drop_first=True)
    # print(df_dum.head())   #Debugging

    # Train test split
    x = df_dum.drop(columns=["avg_salary"], axis=1)
    y = df_dum.avg_salary.values  # Returns numpy array, useful for sklearn models

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    return df_dum, x_train, x_test, y_train, y_test


def linear_model(x_train, y_train):
    model = LinearRegression()
    scores = cross_val_score(
        model, x_train, y_train, scoring="neg_mean_absolute_error", cv=3
    )  # Internally calls model.fit()
    # print(scores)      #Debugging
    # print(np.mean(scores))  #Debugging
    return model.fit(x_train, y_train)

    """
    Methods of Linear model:
    fit(self, X, y, sample_weight) = Fit linear model.
    get_params(self, deep) = Get parameters for this estimator.
    predict(self, X) = Predict using the linear model.
    score(self, X, y, sample_weight) = Return the coefficient of determination R^2 of the prediction.
    set_params(self, **params) = Set the parameters of this estimator.
    """


def lasso_model(x_train, y_train):
    # Let's check errors for different values of alpha
    alphas_err = dict()
    for i in range(1, 100):
        model = Lasso(
            alpha=i / 100
        )  ## Lasso adds a penalty(regularization, lambda) that scales linearly with the absolute value of each coefficient
        scores = cross_val_score(
            model, x_train, y_train, scoring="neg_mean_absolute_error", cv=3
        )  # Internally calls model.fit()
        alphas_err[i / 100] = np.mean(scores)

    # plt.plot(alphas_err.keys(), alphas_err.values())   # Debugging -visually check the best alpha
    # plt.show() #Debugging - visually check the best alpha
    # print(alphas_err)  # Debugging

    max_score_alpha = max(
        alphas_err, key=alphas_err.get
    )  # Get the key(alpha) with the max value(max score, min error)
    # print(max_score_alpha) # Debugging

    # Now, we can use this alpha to train our model
    model = Lasso(alpha=max_score_alpha)
    scores = cross_val_score(
        model, x_train, y_train, scoring="neg_mean_absolute_error", cv=3
    )  # Internally calls model.fit()

    # print(scores) # Debugging

    return model.fit(x_train, y_train)


def rforest_model(x_train, y_train):
    model = RFR()
    scores = cross_val_score(
        model, x_train, y_train, scoring="neg_mean_absolute_error", cv=3
    )  # Internally calls model.fit()

    # print(scores) # Debugging
    # print(np.mean(scores)) # Debugging

    return model.fit(x_train, y_train)


def mae_calculate(y_test, t_ensemble):
    mae_lnr = mae(y_test, t_ensemble["Linear"])
    mae_lss = mae(y_test, t_ensemble["Lasso"])
    mae_rf = mae(y_test, t_ensemble["RForest"])

    # print(mae_lnr, mae_lss, mae_rf) # Debugging

    return mae_lnr, mae_lss, mae_rf


def models(
    path="./../data/processed/eda_data.csv",
    linear=True,
    lasso=True,
    rforest=True,
):
    # Load data
    df_dum, x_train, x_test, y_train, y_test = load_data(path)

    # Multiple linear regression
    if linear:
        lnr_model = linear_model(x_train, y_train)

    # Lasso regression
    if lasso:
        lss_model = lasso_model(x_train, y_train)

    # Random Forest
    if rforest:
        rf_model = rforest_model(x_train, y_train)

        # Tune models GridsearchCV
        parameters = {
            "n_estimators": range(10, 100, 10),
            "criterion": ["squared_error", "absolute_error"],
            "max_features": ["sqrt"],
        }
        gs = GridSearchCV(rf_model, parameters, scoring="neg_mean_absolute_error", cv=3)
        gs.fit(x_train, y_train)

        # print(gs.best_score_) #Debugging
        # print(gs.best_estimator_) #Debugging
        # print(gs.best_params_) #Debugging

    # Test ensembles
    t_ensemble = {
        "Linear": lnr_model.predict(x_test),
        "Lasso": lss_model.predict(x_test),
        "RForest": gs.best_estimator_.predict(x_test),
    }

    mae_lnr, mae_lss, mae_rf = mae_calculate(y_test, t_ensemble)

    print(mae_lnr, mae_lss, mae_rf)  # Debugging


if __name__ == "__main__":
    main()
