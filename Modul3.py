# %% 
import pandas as pd 

# %% 
data = pd.read_csv("students.csv") 

# %% 
display(data.head(10))

# %% 
data.info() 

# %% 
data.isna().sum() 

# %% 
data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)

#%% 
data['reading score'].fillna(data['reading score'].mean(), inplace=True) 

# %% 
data['grade'].fillna(data['grade'].median(), inplace=True) 

# %% 
data.info() 

# %% 
data['lunch'].interpolate(method='linear', inplace=True) 

# %% 
# isi data dengan data sebelumnya
data['grade'].fillna(method='bfill', inplace=True) 

# %% 
data['reading score'].fillna(method= 'ffill', inplace = True) 



# %% 
# menghapus data baris atau kolom Nan secara permanen
data['grade'].dropna(axis=0, inplace=True) 

data['reading score'].drop(axis=1, inplace=True) 