# DATA-PIPELINE-DEVELOPMENT

COMPANY: CODTECH IT SOLUTIONS

NAME: SRISHTI SHARMA

INTERN ID: CT04DN466

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION OF THE PROJECT:

🔗 Data Pipeline Development Using Python

📌 Overview This project focuses on the development of a data pipeline to automate the preprocessing of structured datasets in CSV format. Built using Python, it showcases the core stages of a traditional ETL (Extract, Transform, Load) pipeline, widely used in data engineering and machine learning workflows.

The goal is to enable efficient and consistent data preparation by:

Automating cleaning and transformation

Handling missing values

Encoding categorical variables

Standardizing numerical data

By the end of the pipeline, the raw data is converted into a machine-learning-ready format — fully numeric, normalized, and free of missing values.

🧠 What Is a Data Pipeline? A data pipeline is a series of automated processes that extract data from a source, transform it into a usable format, and load it into a destination for analysis or modeling. This pipeline simplifies repetitive data wrangling tasks and ensures consistency, especially when working with large datasets or real-time data feeds.

⚙ Pipeline Stages

Extract Reads a dataset from raw_data.csv using pandas.
Validates the file's existence and loads it into memory as a DataFrame.

Transform Separates features into numerical and categorical columns.
Applies a transformation pipeline to each:

Numerical Pipeline:

Fills missing values using the mean strategy.

Standardizes the data using StandardScaler.

Categorical Pipeline:

Fills missing values with the most frequent category.

Applies OneHotEncoding to convert categories into numerical columns.

Uses ColumnTransformer to apply the correct pipeline to each column group.

Optionally excludes a target column to preserve labels for model training.

Load The transformed dataset is saved to processed_data.csv.
Output is clean, consistent, and ready for machine learning models

📌 Key Features Automates data preprocessing using scikit-learn pipelines

Supports missing value imputation for both numeric and categorical features

Scales numeric data for model compatibility

One-hot encodes categorical columns for ML algorithms

Modular, readable, and easy to customize

💡 Use Cases Preparing data for machine learning models

Automating preprocessing in a data science workflow

Teaching basic data engineering and ETL concepts

Integrating into larger MLOps or data pipeline systems

🧑‍💻 Technologies Used

OUTPUT:

![Image](https://github.com/user-attachments/assets/9bb72bb3-88a0-4c78-8028-346616e41fad)
