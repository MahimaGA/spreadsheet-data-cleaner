import sys
import pandas as pd

data_frame = pd.read_excel(sys.argv[1])
data_frame.to_excel("cleaned_output.xlsx", index=False)
