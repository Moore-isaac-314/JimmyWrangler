# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 11:52:10 2020

@author: Isaac Moore
"""

import matplotlib.pyplot as plt
import pandas as pd

#Get the data from the raw data files
crime = pd.read_csv("Crime-Data.csv")
laws = pd.read_csv("GunLaw-Data.csv")
# print(crime.head)
#Sorting the data to make them fit together
crime=crime.sort_values(by=['Label'])
laws=laws.sort_values(by=['state','year'])

#Extracting the valid columns
vctot = pd.Series(crime['Violent/100K'].tolist())
states = pd.Series(crime['Label'].tolist())
gunlaws = pd.Series(laws['lawtotal'].tolist())
print(vctot)
print(states)
print(gunlaws)
# Putting the final columns into the final dataset
finaldata = pd.DataFrame({'State': states,'Violent/100K':vctot,'Number of Laws':gunlaws})
#Exporting the transformed datasets as .csv
finaldata.to_csv('Gun Laws vs Violent Crime by State.csv')

fifteenstates = []
fifteenlaws = []
fifteenvctot = []
for i in range(len(states)):
    if (i+1)%3==0:
        fifteenstates.append(states[i])
        fifteenlaws.append(gunlaws[i])
        fifteenvctot.append(vctot[i])

fifteendata = pd.DataFrame({'State':fifteenstates,'Violent/100K':fifteenvctot,'Number of Laws':fifteenlaws})
fifteendata.to_csv('2015 Data.csv')

sixteenstates = []
sixteenlaws = []
sixteenvctot = []
for i in range(len(states)):
    if (i+1)%3==0:
        sixteenstates.append(states[i])
        sixteenlaws.append(gunlaws[i])
        sixteenvctot.append(vctot[i])
sixteendata = pd.DataFrame({'State':sixteenstates,'Violent/100K':sixteenvctot,'Number of Laws':sixteenlaws})
sixteendata.to_csv('2016 Data.csv')

changedlaws = []
changedvctot = []
changedstates =  []
for i in range(len(states)):
    if (i+1)%3==0:
        changedstates.append(states[i])
        changedlaws.append(gunlaws[i])
        changedvctot.append(vctot[i])
changedata = pd.DataFrame({'State':changedstates,'Violent/100K':changedvctot,'Number of Laws':changedlaws})
changedata.to_csv('Change Data.csv')

#Plotting the data
plt.figure()
fifteendata.plot()
plt.savefig('2015Data.pdf')

plt.figure()
sixteendata.plot()
plt.savefig('2016Data.pdf')

plt.figure()
changedata.plot()
plt.savefig('ChangeData.pdf')