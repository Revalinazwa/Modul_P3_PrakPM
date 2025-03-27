# %%
import pandas as pd

# %%
data = pd.read_csv("DatasetForCoffeeSales2.csv")

# %%
display(data.head(10))

#%%
data.filter(["City", "Category", "Product", "Quantity"]).head()

# %%
data.sort_values("Quantity", axis=0, ascending=False, inplace=True, na_position="last")
display(data.head())

# %%
grp1 = data.groupby('City')
result = grp1['Final Sales'].aggregate('sum')
print(result)
# %%
