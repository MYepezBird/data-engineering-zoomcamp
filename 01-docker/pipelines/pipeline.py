import sys
import pandas as pd

print("arguments", sys.argv)

month_number = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "numb_passangers": [3, 4], "month": month_number})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")
#print(f"Running pipeline for month {month_number}")