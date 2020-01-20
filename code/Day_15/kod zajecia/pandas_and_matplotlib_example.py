import pandas as pd
import matplotlib.pyplot as plt

food_info = pd.read_csv("food_info.csv")
col_names = food_info.columns.tolist()
print(col_names)
print(food_info.head(3))

sugar_and_iron = food_info[["Iron_(mg)", "Sugar_Tot_(g)"]]
print(sugar_and_iron)

print("Sugar and iron correlation:")
print(sugar_and_iron.corr())

sugar_and_iron.plot(kind="scatter", x="Iron_(mg)", y="Sugar_Tot_(g)")

plt.show()
