import pandas as pd

# Sample data
data = {
    'age': [25, 30, 45, 28, None],
    'income': [50000, 60000, None, 45000, 70000],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'city': ['Mumbai', 'Delhi', 'Kolkata', 'Chennai', 'Mumbai'],
    'target': [1, 0, 1, 0, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('raw_data.csv', index=False)

print("✅ raw_data.csv created!")


import pandas as pd
df = pd.read_csv('raw_data.csv')
print(df.head())
