# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts here
summer = data['Total_Summer']
winter = data['Total_Winter']
data['Better_Event'] = np.where(summer > winter, "Summer", np.where(summer < winter, "Winter", "Both"))

better_event = data['Better_Event'].value_counts().idxmax()


# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.set_index(["Country_Name"], inplace = True) 
top_countries = top_countries.drop('Totals')
top_countries.reset_index(inplace = True)

def top_ten(topcon, column_name):
    country_list = data.nlargest(11, column_name)['Country_Name'].values
    country_list = np.delete(country_list, 0)
    print(country_list.tolist())
    return country_list.tolist()

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = np.intersect1d(top_10_summer, top_10_winter)
common = np.intersect1d(common, top_10).tolist()
print(common)



# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.figure(figsize=[20,10])
plt.xlabel("Country Name")
plt.ylabel("Total Medal Count")

plt.subplot(131)
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xticks(rotation=45)
plt.subplot(132)
plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.xticks(rotation=45)
plt.subplot(133)
plt.bar(top_df['Country_Name'],top_df['Total_Medals'])
plt.xticks(rotation=45)


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
top_df['Golden_Ratio'] = summer_df['Gold_Total']/summer_df['Total_Medals']

def best(dataframe):
    dataframe.set_index("Country_Name", inplace = True)
    s =  dataframe['Golden_Ratio']
    return s.max(), s.idxmax()

summer_max_ratio, summer_country_gold = best(summer_df)
print(summer_max_ratio, summer_country_gold)

winter_max_ratio, winter_country_gold = best(winter_df)
print(winter_max_ratio, winter_country_gold)

top_max_ratio, top_country_gold = best(top_df)
print(top_max_ratio, top_country_gold)


# --------------
#Code starts here
data_1 = data[:-1]
data_1['Total_Points'] = 3*data_1['Gold_Total'] + (2*data_1['Silver_Total']) + data_1['Bronze_Total']
print(data_1['Total_Points'])
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points, best_country)


# --------------
#Code starts here

best = data[data['Country_Name']==str(best_country)]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]
res = best.groupby(['Gold_Total','Silver_Total','Bronze_Total']).size().unstack()
res.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


