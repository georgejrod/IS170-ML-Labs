#George Rodriguez w/ partner Logan Cheng

# Import pandas, which is used to load and work with datasets in table form
import pandas as pd

# Use a try/except block so the program handles errors if the file path is incorrect
try:
    # Load the CSV file into a pandas DataFrame
    # This allows us to easily clean and modify the data
    df = pd.read_csv('/Users/georgejrodriguez/Downloads/IS170 Lab #1/student+performance/student/student-por.csv')
    # Print the number of rows and columns before cleaning
    # This helps us compare the dataset size before and after cleaning
    print("Original data shape:", df.shape)
except FileNotFoundError:
    # Print an error message if the file cannot be found and stop the program
    print("Error: student-por.csv not found. Please check the file path.")
    exit()

# Replace all missing values (NaN) with the string "0"
# This approach is useful when we want to keep all rows in the dataset
# while clearly marking where data was originally missing
df_cleaned = df.fillna(0)

# Print the shape of the dataset after filling missing values
# The shape should stay the same since no rows are removed
print("Cleaned data shape:", df_cleaned.shape)

# Save the cleaned dataset to a new CSV file
# index=False prevents pandas from adding extra row numbers to the file
output_path = 'fill_0_cleaned_student-por.csv'
df_cleaned.to_csv(output_path, index=False)
# Confirm that the cleaned file was saved successfully
print(f"Cleaned data saved to {output_path}")