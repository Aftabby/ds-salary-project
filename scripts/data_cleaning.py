import pandas as pd


def main():
    clean()


def clean(
    df=pd.read_csv("../data/raw/glassdoor_jobs.csv"),
    output_path="../data/processed/salary_data_cleaned.csv",
):
    # Salary parsing
    df = df[
        (df["Salary Estimate"] != "-1")
        & (~df["Salary Estimate"].str.lower().str.contains("employer|hour"))
    ].copy()

    salary = df["Salary Estimate"].apply(lambda x: x.split("(")[0])
    salary = salary.apply(lambda x: x.replace("K", "000").replace("$", ""))

    # Optional: Add min and max salary as columns - I just used the average
    avg_salary = salary.apply(
        lambda x: int((int(x.split("-")[0]) + int(x.split("-")[1])) / 2)
    )

    df["Salary Estimate"] = avg_salary

    # Company name text only
    df["Company Name"] = df["Company Name"].apply(lambda x: x.split("\n")[0])

    # State field
    df["Job_State"] = df["Location"].apply(lambda x: x.split(", ")[1])

    df["Same_State"] = df.apply(
        lambda x: 1 if x.Location == x.Headquarters else 0, axis=1
    )

    # Age of company
    df["Company_Age"] = df.Founded.apply(lambda x: 0 if x < 1 else 2025 - x)

    # Parsing of job description (python, etc.)
    # python
    df["Python"] = df["Job Description"].apply(
        lambda x: 1 if "python" in x.lower() else 0
    )
    # r studio
    df["R"] = df["Job Description"].apply(
        lambda x: 1 if "r studio" in x.lower() or "r-studio" in x.lower() else 0
    )
    # spark
    df["Spark"] = df["Job Description"].apply(
        lambda x: 1 if "spark" in x.lower() else 0
    )
    # aws
    df["AWS"] = df["Job Description"].apply(lambda x: 1 if "aws" in x.lower() else 0)
    # excel
    df["Excel"] = df["Job Description"].apply(
        lambda x: 1 if "excel" in x.lower() else 0
    )

    # Drop the Unnamed: 0 column and reset the index
    df.reset_index(drop=True, inplace=True)
    df.drop("Unnamed: 0", axis=1, inplace=True)

    df.to_csv(output_path, index=False)

    return df


if __name__ == "__main__":
    main()
