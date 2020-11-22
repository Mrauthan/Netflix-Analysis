# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:05:29 2020

@author: MRauthan
"""

import pandas as pd
import matplotlib.pyplot as plt

Netflix_df=pd.read_csv(r"C:\Users\mrauthan\OneDrive - ascenaretail.com\Desktop\Ascena\DS\Python Practice\Netflix\netflix_titles.csv")
#print(Netflix_df)

print('print Netflix_df column')
print(Netflix_df.columns)

print('datatype column')
print(Netflix_df['type'].describe())


print('trying to print only null rows')

Netflix_Null=Netflix_df.columns[Netflix_df.isnull().any()]
print(Netflix_Null)

print('trying to print total for null rows')
print(Netflix_df[Netflix_Null].isnull().sum())

Netflix_df['director']=Netflix_df['director'].fillna('Standard')
Netflix_df['cast']=Netflix_df['cast'].fillna('No Cast')
Netflix_df['country']=Netflix_df['country'].fillna('No Country')
Netflix_df['date_added']=Netflix_df['date_added'].fillna('00-DTA-00')
Netflix_df['rating']=Netflix_df['rating'].fillna(0)

print('Again trying to print total for null rows')
print(Netflix_df[Netflix_Null].isnull().sum())

print('split based on duration delemited by space')
Netflix_split=Netflix_df['duration'].str.split(" ",0,expand=True)
print(Netflix_split[0])

Netflix_split=Netflix_df['duration'].str.split(" ",0,expand=True)
print(Netflix_split[1])

print('Trying to make all time in mins')

print('No of rows in dataframe: ')
total_rows=Netflix_df.shape[0]#['duration'].count
print(total_rows)
#print(Netflix_df['duration'].count)

print('Before For Loop')
print(Netflix_split[1][0])
print('Before For Loop start for duration')

for i in range(1,len(Netflix_df)):
    print(Netflix_split[1][i])
    if Netflix_split[1][i] in 'hours':
       Netflix_split[0][i]=int(Netflix_split[0][i])*60
       print(Netflix_split[0][i])
    elif Netflix_split[1][i] in 'Seasons':
            Netflix_split[0][i]=int(Netflix_split[0][i])*60*24
            Netflix_split[0][i]
    else:
            Netflix_split[0][i]=int(Netflix_split[0][i])*60*24*24
            Netflix_split[0][i]
            

print('print Netflix_split[0] again')
Netflix_split=Netflix_df['duration'].str.split(" ",0,expand=True)
print(Netflix_split[0])    

print('Create new column Time_duration')
Netflix_df['Time_duration']=Netflix_split[0]

print ('Time_duration')
print(Netflix_df['Time_duration'])

print('print Netflix_df column again')
print(Netflix_df.columns)

print('print sort column based on duration')
print(Netflix_df.sort_values('Time_duration', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last'))


print('Before Scatter plot for Movie and duration')
plt.scatter(Netflix_df['type'],Netflix_df['Time_duration'])##working

print('After Scatter plot for Movie and duration')


print('unique value of rating')
print(Netflix_df.rating.unique())

print('Copying all value of rating to Movice_Rating')
Netflix_df['Movie_Rating']=Netflix_df['rating']

print(Netflix_df.columns)

print('Before if condition for Rating')

for i in range(0,len(Netflix_df)):
    if str(Netflix_df['rating'][i]) in 'TV-PG':
       #Netflix_df['Movie_Rating'][i]=1
       Netflix_df['Movie_Rating'][i]=1
    elif str(Netflix_df['rating'][i]) in 'TV-MA':
       Netflix_df['Movie_Rating'][i]=2
    elif str(Netflix_df['rating'][i]) in 'TV-PG':
       Netflix_df['Movie_Rating'][i]=3
    elif str(Netflix_df['rating'][i]) in 'TV-Y7-FV':
       Netflix_df['Movie_Rating'][i]=4
    elif str(Netflix_df['rating'][i]) in 'TV-Y7':
       Netflix_df['Movie_Rating'][i]=5
    elif str(Netflix_df['rating'][i]) in 'TV-14':
       Netflix_df['Movie_Rating'][i]=6
    elif str(Netflix_df['rating'][i]) in 'R':
       Netflix_df['Movie_Rating'][i]=7
    elif str(Netflix_df['rating'][i]) in 'TV-Y':
       Netflix_df['Movie_Rating'][i]=8
    elif str(Netflix_df['rating'][i]) in 'NR':
       Netflix_df['Movie_Rating'][i]=9
    elif str(Netflix_df['rating'][i]) in 'PG-13':
       Netflix_df['Movie_Rating'][i]=10
    elif str(Netflix_df['rating'][i]) in 'TV-G':
       Netflix_df['Movie_Rating'][i]=11
    elif str(Netflix_df['rating'][i]) in 'PG':
       Netflix_df['Movie_Rating'][i]=12
    elif str(Netflix_df['rating'][i]) in 'G':
       Netflix_df['Movie_Rating'][i]=13
    elif str(Netflix_df['rating'][i]) in 'UR':
       Netflix_df['Movie_Rating'][i]=14
    elif str(Netflix_df['rating'][i]) in 'NC-17':
       Netflix_df['Movie_Rating'][i]=15
    else:
       Netflix_df['Movie_Rating'][i]=16

print(Netflix_df['Movie_Rating'][1])
print(Netflix_df['Movie_Rating'][2])
print(Netflix_df['Movie_Rating'][100])
print(Netflix_df['Movie_Rating'][1000])

print('After if condition for Rating')