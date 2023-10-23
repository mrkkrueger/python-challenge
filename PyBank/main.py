import pandas as pd
from pathlib import Path

budget_data=Path("PyBank/Resources/budget_data.csv")
budget_data_df=pd.read_csv(budget_data)

total_months=len(budget_data_df.index)

net_total=budget_data_df["Profit/Losses"].sum()

budget_data_df["Difference"]=budget_data_df["Profit/Losses"].diff()
average_change=budget_data_df["Difference"].mean()
average_change=round(average_change,2)

greatest_increase=budget_data_df["Difference"].max()
greatest_increase=int(greatest_increase)

greatest_decrease=budget_data_df["Difference"].min()
greatest_decrease=int(greatest_decrease)

df=budget_data_df.set_index("Difference")
date_greatest_increase=df.loc[greatest_increase,"Date"]
date_greatest_decrease=df.loc[greatest_decrease,"Date"]

print("Financial Analysis")
print("----------------------------")
print("Total Months:", total_months)
print("Total: $", net_total)
print("Average Change:", "$",average_change)
print("Greatest Increase in Profits:", date_greatest_increase, "($",greatest_increase,")")
print("Greatest Decrease in Profits:", date_greatest_decrease, "($",greatest_decrease,")")


import sys
with open('PyBank/analysis/Financial_Analysis.txt', 'w') as file:
    sys.stdout=file
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", total_months)
    print("Total: $", net_total)
    print("Average Change: $",average_change)
    print("Greatest Increase in Profits:", date_greatest_increase, "($",greatest_increase,")")
    print("Greatest Decrease in Profits:", date_greatest_decrease, "($",greatest_decrease,")")
  