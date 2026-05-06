#George Rodriguez w/ partner Logan Cheng

# Import pandas library that helps us work with data tables
import pandas as pd

# Try to load the CSV file so the program does not crash if the file is missing
try:
    # Read the CSV file and store it in a DataFrame
    # A DataFrame is a table with rows and columns
    df = pd.read_csv('/Users/georgejrodriguez/Downloads/IS170 Lab #1/daily_gym_attendance_workout_data.csv')
    # Print the number of rows and columns in the dataset
    # This helps us see how large the dataset is before cleaning
    print("Original data shape:", df.shape)
except FileNotFoundError:
    # If the file cannot be found, print an error message and stop the program
    print("Error: daily_gym_attendance_workout_data.csv not found. Please check the file path.")
    exit()

# Remove any rows that contain missing values
# To ensure we are working only with complete data
df_cleaned = df.dropna()

# Print the new size of the dataset after removing missing values
# This shows how much data was removed during the cleaning step
print("Cleaned data shape:", df_cleaned.shape)

# Save the cleaned dataset to a new CSV file
# index=False prevents pandas from adding extra row numbers to the file
output_path = 'drop_cleaned_daily_gym_attendance_workout_data.csv'
df_cleaned.to_csv(output_path, index=False)
# Let the us know the file was saved successfully
print(f"Cleaned data saved to {output_path}")