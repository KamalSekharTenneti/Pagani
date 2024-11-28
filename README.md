# Pagani


This project focuses on predictive analysis for car sales and satisfaction trends, leveraging Python to forecast critical metrics such as UnitsSold, AvgPriceUSD, and CustomerSatisfaction for the year 2025. The dataset comprises historical data across multiple years, detailing various car models, fuel types, and their respective performance metrics. The aim is to derive actionable insights into future trends using machine learning techniques.

The project is implemented using Python libraries such as pandas and sklearn. The workflow begins with data preprocessing, where the historical data is loaded and categorical features like Model and FuelType are encoded using LabelEncoder. Independent variables such as Year, Model, and FuelType are separated from the dependent variables (UnitsSold, AvgPriceUSD, and CustomerSatisfaction) to prepare the dataset for machine learning models.

A Random Forest Regressor, known for its accuracy and robustness with both numerical and categorical data, is employed to predict each target variable. The dataset is split into training and testing sets to ensure the model generalizes well to unseen data. Once trained, the model uses inputs for 2025 to predict sales, average price, and customer satisfaction for various car models and fuel types.

This project stands out for its practical application of machine learning to solve real-world business problems. It demonstrates the ability to analyze historical data, build predictive models, and generate meaningful insights that can aid in decision-making processes. The use of Random Forest ensures reliable predictions, while the handling of categorical and numerical data showcases robust preprocessing skills.

The GitHub repository for this project includes well-documented Python scripts, the dataset, and step-by-step instructions to run the code and interpret the results. The repository serves as a valuable resource for understanding the complete workflow, from data preprocessing to model evaluation and prediction.

On LinkedIn, this project can be highlighted as a prime example of using data science for business forecasting. A post can include visualizations of the predictions for 2025, insights into the modeling process, and the potential business applications. This can inspire discussions, collaboration, and feedback from peers in the data science community.

Overall, this project reflects strong skills in data analysis, machine learning, and problem-solving, making it an excellent addition to GitHub and LinkedIn profiles. It underscores the ability to transform raw data into actionable insights, aligning with industry demands for data-driven decision-making.
