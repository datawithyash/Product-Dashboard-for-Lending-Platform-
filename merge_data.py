import pandas as pd

# Load feature data and target labels
X = pd.read_csv('X.csv')
y = pd.read_csv('target.csv')

# Add target column to the X dataframe
X['loan_status'] = y

# Save the merged file
X.to_csv('lending_dashboard_data.csv', index=False)

print("✅ Merged file saved as lending_dashboard_data.csv")
