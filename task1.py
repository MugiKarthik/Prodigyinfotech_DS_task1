#!/usr/bin/env python
# coding: utf-8

# # Prodigy_InfoTech_DS_Task1
# 
# Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.
# 
# importing the data and understanding data:

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# In[4]:


data=pd.read_csv("C:\\Users\\KARTHIK M\\Documents\\Internship\\Prodigy InfoTech\\Task 1\\population_data.csv")
pd.set_option('display.max_columns', None)
data.head()


# In[5]:


data.shape


# In[6]:


data.info()


# In[7]:


data.describe()


# # Data preprocessing

# In[8]:


#missing data
missing_data = data.isna().sum()
pd.set_option('display.max_rows', None)
print(missing_data)


# In[9]:


#filling the missing data with average for Continuous variable
data = data.fillna(data.mean())
missing_data = data.isna().sum()
pd.set_option('display.max_rows', None)
print(missing_data)


# In[10]:


#feature Selection
columns_to_drop = ['Country Code', 'Indicator Name', 'Indicator Code', '2023']
data.drop(columns=columns_to_drop, inplace=True, errors='ignore')
data.head()


# # EDA
# univariant - Continuous variable

# In[21]:


years = [str(year) for year in range(1960, 2023)]

continuous_vars = [year for year in years if year in data.columns]

fig, axes = plt.subplots(nrows=len(continuous_vars), figsize=(6, 4 * len(continuous_vars)))
fig.subplots_adjust(hspace=0.5)

for i, var in enumerate(continuous_vars):
    ax = axes[i]
    sns.histplot(data[var], ax=ax, kde=True)
    ax.set_title(f'Histogram of {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Frequency')
    
plt.tight_layout()
plt.show()


# In[40]:


# yearly trend of the population by sum
years = list(map(str, range(1960, 2023)))  # List of years as strings from '1960' to '2022'

sum_values = data[years].sum()

plt.figure(figsize=(12, 6))
plt.plot(years, sum_values, marker='o', linestyle='-', color='b', label='Sum of Values')
plt.title('Sum of population for Years 1960 to 2022')
plt.xlabel('Years')
plt.ylabel('Sum of Values')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

z = np.polyfit(range(len(years)), sum_values, 1)
p = np.poly1d(z)
plt.plot(years,p(range(len(years))), linestyle='--', color='r', label='Trend Line')
plt.tight_layout()
plt.legend()
plt.show()


# In[41]:


# yearly trend of the population by average

years = list(map(str, range(1960, 2023)))

# Calculate average (mean) values for each year
average_values = data[years].mean()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(years, average_values, marker='o', linestyle='-', color='b', label='Average Values')
plt.title('Average population for Years 1960 to 2022')
plt.xlabel('Years')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
z = np.polyfit(range(len(years)), average_values, 1)
p = np.poly1d(z)
plt.plot(years, p(range(len(years))), linestyle='--', color='r', label='Trend Line')

plt.tight_layout()
plt.legend()
plt.show()


# univarant - catergorical variable

# In[57]:



years = list(map(str, range(1960, 2023)))

data['Total'] = data[years].sum(axis=1)

country_totals = data.groupby('Country Name')['Total'].sum()

top_countries = country_totals.nlargest(30)

plt.figure(figsize=(20, 12))
top_countries.plot(kind='bar', color='skyblue')
plt.title('Top 30 Countries by Total Values from 1960 to 2022')
plt.xlabel('Country')
plt.ylabel('Total Value')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# # Bivariate analysis
# bar chart for top 30 countries population for each year

# In[22]:


years = [str(year) for year in range(1960, 2023)]

continuous_vars = [year for year in years if year in data.columns]

fig, axes = plt.subplots(nrows=len(continuous_vars), figsize=(12, 6 * len(continuous_vars)))
fig.subplots_adjust(hspace=0.5)

for i, var in enumerate(continuous_vars):
    ax = axes[i] if len(continuous_vars) > 1 else axes  
    top_countries = data.nlargest(30,var)
    sns.barplot(x='Country Name', y=var, data=top_countries, ax=ax)
    ax.set_title(f'Bar Chart of {var}')
    ax.set_xlabel('Country')
    ax.set_ylabel(var)
    ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels for better readability

plt.tight_layout()
plt.show()


# # Population male dataset analysis

# In[23]:


data=pd.read_csv("C:\\Users\\KARTHIK M\\Documents\\Internship\\Prodigy InfoTech\\Task 1\\population_data_male.csv")
pd.set_option('display.max_columns', None)
data.head()


# In[24]:


data.shape


# In[16]:


data.info()


# In[17]:


data.describe()


# In[25]:


#missing data
missing_data = data.isna().sum()
pd.set_option('display.max_rows', None)
print(missing_data)


# In[26]:


#filling the missing data with average for Continuous variable
data = data.fillna(data.mean())
missing_data = data.isna().sum()
pd.set_option('display.max_rows', None)
print(missing_data)


# In[27]:


#feature Selection
columns_to_drop = ['Country Code', 'Indicator Code', '2023']
data.drop(columns=columns_to_drop, inplace=True, errors='ignore')
data.head()


# In[28]:


years = [str(year) for year in range(1960, 2023)]

continuous_vars = [year for year in years if year in data.columns]

fig, axes = plt.subplots(nrows=len(continuous_vars), figsize=(6, 4 * len(continuous_vars)))
fig.subplots_adjust(hspace=0.5)

for i, var in enumerate(continuous_vars):
    ax = axes[i]
    sns.histplot(data[var], ax=ax, kde=True)
    ax.set_title(f'Histogram of {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Frequency')
    
plt.tight_layout()
plt.show()


# In[29]:


# yearly trend of the population by sum
years = list(map(str, range(1960, 2023)))  # List of years as strings from '1960' to '2022'

sum_values = data[years].sum()

plt.figure(figsize=(12, 6))
plt.plot(years, sum_values, marker='o', linestyle='-', color='b', label='Sum of Values')
plt.title('Sum of population for Years 1960 to 2022')
plt.xlabel('Years')
plt.ylabel('Sum of Values')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

z = np.polyfit(range(len(years)), sum_values, 1)
p = np.poly1d(z)
plt.plot(years,p(range(len(years))), linestyle='--', color='r', label='Trend Line')
plt.tight_layout()
plt.legend()
plt.show()


# In[30]:


# yearly trend of the population by average

years = list(map(str, range(1960, 2023)))

# Calculate average (mean) values for each year
average_values = data[years].mean()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(years, average_values, marker='o', linestyle='-', color='b', label='Average Values')
plt.title('Average population for Years 1960 to 2022')
plt.xlabel('Years')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
z = np.polyfit(range(len(years)), average_values, 1)
p = np.poly1d(z)
plt.plot(years, p(range(len(years))), linestyle='--', color='r', label='Trend Line')

plt.tight_layout()
plt.legend()
plt.show()


# In[31]:


years = list(map(str, range(1960, 2023)))

data['Total'] = data[years].sum(axis=1)

country_totals = data.groupby('Country Name')['Total'].sum()

top_countries = country_totals.nlargest(30)

plt.figure(figsize=(20, 12))
top_countries.plot(kind='bar', color='skyblue')
plt.title('Top 30 Countries by Total Values from 1960 to 2022')
plt.xlabel('Country')
plt.ylabel('Total Value')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[32]:


years = [str(year) for year in range(1960, 2023)]

continuous_vars = [year for year in years if year in data.columns]

fig, axes = plt.subplots(nrows=len(continuous_vars), figsize=(12, 6 * len(continuous_vars)))
fig.subplots_adjust(hspace=0.5)

for i, var in enumerate(continuous_vars):
    ax = axes[i] if len(continuous_vars) > 1 else axes  
    top_countries = data.nlargest(30,var)
    sns.barplot(x='Country Name', y=var, data=top_countries, ax=ax)
    ax.set_title(f'Bar Chart of {var}')
    ax.set_xlabel('Country')
    ax.set_ylabel(var)
    ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels for better readability

plt.tight_layout()
plt.show()


# # population female dataset analysis

# In[33]:


data=pd.read_csv("C:\\Users\\KARTHIK M\\Documents\\Internship\\Prodigy InfoTech\\Task 1\\population_data_female.csv")
pd.set_option('display.max_columns', None)
data.head()


# In[34]:


data.info()


# In[35]:


data.shape


# In[36]:


data.describe()


# In[37]:


#missing data
missing_data = data.isna().sum()
pd.set_option('display.max_rows', None)
print(missing_data)


# In[38]:


#filling the missing data with average for Continuous variable
data = data.fillna(data.mean())
missing_data = data.isna().sum()
pd.set_option('display.max_rows', None)
print(missing_data)


# In[39]:


#feature Selection
columns_to_drop = ['Country Code', 'Indicator Code', '2023']
data.drop(columns=columns_to_drop, inplace=True, errors='ignore')
data.head()


# In[40]:


years = [str(year) for year in range(1960, 2023)]

continuous_vars = [year for year in years if year in data.columns]

fig, axes = plt.subplots(nrows=len(continuous_vars), figsize=(6, 4 * len(continuous_vars)))
fig.subplots_adjust(hspace=0.5)

for i, var in enumerate(continuous_vars):
    ax = axes[i]
    sns.histplot(data[var], ax=ax, kde=True)
    ax.set_title(f'Histogram of {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Frequency')
    
plt.tight_layout()
plt.show()


# In[41]:


# yearly trend of the population by sum
years = list(map(str, range(1960, 2023)))  # List of years as strings from '1960' to '2022'

sum_values = data[years].sum()

plt.figure(figsize=(12, 6))
plt.plot(years, sum_values, marker='o', linestyle='-', color='b', label='Sum of Values')
plt.title('Sum of population for Years 1960 to 2022')
plt.xlabel('Years')
plt.ylabel('Sum of Values')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

z = np.polyfit(range(len(years)), sum_values, 1)
p = np.poly1d(z)
plt.plot(years,p(range(len(years))), linestyle='--', color='r', label='Trend Line')
plt.tight_layout()
plt.legend()
plt.show()


# In[42]:


# yearly trend of the population by average

years = list(map(str, range(1960, 2023)))

# Calculate average (mean) values for each year
average_values = data[years].mean()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(years, average_values, marker='o', linestyle='-', color='b', label='Average Values')
plt.title('Average population for Years 1960 to 2022')
plt.xlabel('Years')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
z = np.polyfit(range(len(years)), average_values, 1)
p = np.poly1d(z)
plt.plot(years, p(range(len(years))), linestyle='--', color='r', label='Trend Line')

plt.tight_layout()
plt.legend()
plt.show()


# In[43]:


years = list(map(str, range(1960, 2023)))

data['Total'] = data[years].sum(axis=1)

country_totals = data.groupby('Country Name')['Total'].sum()

top_countries = country_totals.nlargest(30)

plt.figure(figsize=(20, 12))
top_countries.plot(kind='bar', color='skyblue')
plt.title('Top 30 Countries by Total Values from 1960 to 2022')
plt.xlabel('Country')
plt.ylabel('Total Value')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[44]:


years = [str(year) for year in range(1960, 2023)]

continuous_vars = [year for year in years if year in data.columns]

fig, axes = plt.subplots(nrows=len(continuous_vars), figsize=(12, 6 * len(continuous_vars)))
fig.subplots_adjust(hspace=0.5)

for i, var in enumerate(continuous_vars):
    ax = axes[i] if len(continuous_vars) > 1 else axes  
    top_countries = data.nlargest(30,var)
    sns.barplot(x='Country Name', y=var, data=top_countries, ax=ax)
    ax.set_title(f'Bar Chart of {var}')
    ax.set_xlabel('Country')
    ax.set_ylabel(var)
    ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels for better readability

plt.tight_layout()
plt.show()


# In[ ]:




