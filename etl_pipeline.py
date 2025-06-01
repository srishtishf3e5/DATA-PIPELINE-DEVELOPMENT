# === Step 0: Install Required Libraries (handled automatically) ===
try:
    import pandas as pd
except ImportError:
    import os
    os.system('pip install pandas')
    import pandas as pd

try:
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.impute import SimpleImputer
    from sklearn.pipeline import Pipeline
except ImportError:
    import os
    os.system('pip install scikit-learn')
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.impute import SimpleImputer
    from sklearn.pipeline import Pipeline

import os

# === Step 1: Load the raw data ===
def load_data(file_path):
    return pd.read_csv(file_path)

# === Step 2: Preprocess the data ===
def preprocess_data(df):
    # Identify categorical and numerical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Remove target column from numerical processing (if present)
    if 'target' in numerical_cols:
        numerical_cols.remove('target')

    # Pipeline for numeric columns
    numeric_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Pipeline for categorical columns
    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine both pipelines using ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_pipeline, numerical_cols),
            ('cat', categorical_pipeline, categorical_cols)
        ]
    )

    # Apply transformation
    transformed_data = preprocessor.fit_transform(df)

    # Get transformed feature names
    feature_names = (
        numerical_cols +
        list(preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(categorical_cols))
    )

    # Convert to DataFrame
    return pd.DataFrame(
        transformed_data.toarray() if hasattr(transformed_data, "toarray") else transformed_data,
        columns=feature_names
    )

# === Step 3: Save the processed data ===
def save_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"✅ Data saved to: {output_path}")

# === Main Function to Run the ETL Pipeline ===
def main():
    input_file = 'raw_data.csv'
    output_file = 'processed_data.csv'

    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return

    print("🔄 Loading data...")
    raw_data = load_data(input_file)

    print("🔧 Preprocessing data...")
    processed_data = preprocess_data(raw_data)

    print("💾 Saving transformed data...")
    save_data(processed_data, output_file)

# === Run the script ===
if __name__ == "__main__":
    main()
