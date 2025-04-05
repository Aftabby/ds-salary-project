# Data Scientists Salary Prediction

## Overview
This project involves scraping job listing data from [Glassdoor](https://www.glassdoor.com/) to analyze trends in data scientist roles and predict salaries. The project includes data cleaning, exploratory data analysis (EDA), feature engineering, and machine learning modeling. A web application was developed to showcase the results interactively.

## Dataset
The dataset was scraped using [Selenium](https://selenium-python.readthedocs.io/) and contains detailed information about job listings, including:
- Job Title
- Salary Estimate
- Job Description
- Company Rating
- Location
- Industry, Sector, and more.

The processed dataset contains **{{ context.rows }} rows** and **{{ context.columns }} columns**.

## Methodology
1. **Data Scraping**: Extracted job listing data from Glassdoor.
2. **Data Cleaning and Preprocessing**: Removed inconsistencies and prepared the data for analysis.
3. **Exploratory Data Analysis (EDA)**: Analyzed trends and correlations in the data.
4. **Feature Engineering**: Created new features like `job_simp` and `seniority`.
5. **Model Building**: Applied multiple machine learning models.
6. **Web Application Development**: Built an interactive web app using Flask.

## Exploratory Data Analysis (EDA)
Key insights from the data:
- Correlation between features like `Company_Age`, `Rating`, and `Salary Estimate`.
- Distribution of job titles and seniority levels.
- Average salaries by job state and job title.

## Modeling
The following machine learning models were applied:
- Linear Regression
- Lasso Regression
- Random Forest

The **Random Forest** model achieved the highest accuracy of **84.89%** and was selected for deployment.

## Web Application
An interactive web application was developed using [Flask](https://flask.palletsprojects.com/en/stable/) and deployed in a [Docker](https://docs.docker.com/) container. The app allows users to:
- Visualize salary trends.
- Explore job attributes and their impact on salaries.

## Usage
To run the project locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/Aftabby/ds-salary-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ds-salary-project
   ```
3. Build and run the Docker container:
   ```bash
   docker build -t ds-salary-app .
   docker run -p 5000:5000 ds-salary-app
   ```
4. Open the app in your browser at `http://localhost:5000`.

## Technologies Used
- **Programming Languages**: Python, JavaScript
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly
- **Web Framework**: Flask
- **Visualization**: Power BI
- **Deployment**: Docker
- **Automation**: Selenium

## Contributors
- **Aftabby** - [GitHub Profile](https://github.com/Aftabby) [Portfolio Website](https://www.aftabby.com)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Glassdoor](https://www.glassdoor.com/) for providing the job listing data.
- [Selenium](https://selenium-python.readthedocs.io/) for web scraping.
