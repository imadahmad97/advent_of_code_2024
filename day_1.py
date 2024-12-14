import pandas as pd

data = pd.read_csv("data.txt", sep="   ", header=None)
list_1 = data.iloc[:, 0].copy()
list_2 = data.iloc[:, 1].copy()


sorted_list_1 = list_1.sort_values(ascending=True)
sorted_list_2 = list_2.sort_values(ascending=True)

sorted_list_1 = sorted_list_1.reset_index(drop=True)
sorted_list_2 = sorted_list_2.reset_index(drop=True)

print((sorted_list_1 - sorted_list_2).abs().sum())