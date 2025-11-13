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

output_file = f"cleaned_{input_file}"
data_frame.to_excel(output_file, index=False)
