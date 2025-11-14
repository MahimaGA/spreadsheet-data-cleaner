import sys
import pandas as pd

if len(sys.argv) != 2:
    print("Please provide one file as argument")
    sys.exit()

input_file = sys.argv[1]

try:
    data_frame = pd.read_excel(input_file)
except ValueError:
    print("Please provide an excel file")
    sys.exit()

# Standardize column names
new_columns = []
for column in data_frame.columns:
    new_columns.append(column.lower().strip().replace(" ", "_"))
data_frame.columns = new_columns

# Trim whitespace and standardize text case in string columns
for column in data_frame.select_dtypes(include=["object"]).columns:
    data_frame[column] = data_frame[column].str.strip().str.title()

# Convert all date columns to "YYYY-MM-DD" format
for column in data_frame.select_dtypes(include=["object"]).columns:
    if "date" in column:
        data_frame[column] = pd.to_datetime(data_frame[column], errors="coerce").dt.strftime("%Y-%m-%d")

# Fill missing values with "unknown"
for column in data_frame.select_dtypes(include=["object", "number"]).columns:
    data_frame[column] = data_frame[column].fillna("unknown")

# Remove duplicate rows
data_frame = data_frame.drop_duplicates()

output_file = f"cleaned_{input_file}"
data_frame.to_excel(output_file, index=True)
