# George Rodriguez w/ partner Logan Cheng

# Import pandas, a library used to work with data in table form
import pandas as pd

# Use a try/except block to safely load the dataset
# This helps prevent the program from crashing if the file path is wrong
try:
    # Read the CSV file into a pandas DataFrame
    # A DataFrame is similar to a spreadsheet with rows and columns
    df = pd.read_csv('/Users/georgejrodriguez/Downloads/IS170 Lab #1/daily_gym_attendance_workout_data.csv')
    # Print the number of rows and columns before cleaning
    # This allows us to compare the data before and after processing
    print("Original data shape:", df.shape)
except FileNotFoundError:
    # Display an error message if the file cannot be found and stop the program
    print("Error: daily_gym_attendance_workout_data.csv not found. Please check the file path.")
    exit()

# Select only the numeric columns in the dataset
# Missing values in numeric columns are replaced with the column mean
# because the mean represents an average value
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Select the categorical (non-numeric) columns in the dataset
# Missing values in these columns are replaced with the most common value
# since averages do not apply to categories
categorical_cols = df.select_dtypes(exclude='number').columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Save the cleaned DataFrame to a new variable
# This makes it clear that the dataset has been cleaned
df_cleaned = df

# Print the dataset shape after cleaning
# The shape should stay the same because rows were not removed
print("Cleaned data shape:", df_cleaned.shape)

# Save the cleaned dataset to a new CSV file
# index=False prevents pandas from adding extra row numbers
output_path = 'replace_cleaened_daily_gym_attendance_workout_data.csv'
df_cleaned.to_csv(output_path, index=False)
# Confirm that the cleaned file was saved successfully
print(f"Cleaned data saved to {output_path}")