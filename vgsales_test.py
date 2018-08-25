# -*- coding: utf-8 -*-
"""
Data Handling: Games Sales
"""

import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter


data = pd.read_csv("vgsales.csv")
# Nintendo Sales on North America 
nintendo = data[data.Publisher == 'Nintendo']
figure0 = plt.figure()
plt.figure(figsize=(15,10))
plt.title("Nintendo Sales in NA")
plt.xlim(1,15)
plt.xticks(range(1,16))
plt.plot(nintendo.Rank[0:15],nintendo.NA_Sales[0:15], marker='o', linestyle='--', color='r', label='Square')
plt.xlabel("Rank")
plt.ylabel("Sales (in millions)")
plt.legend(['Curve of sales'])
plt.grid(True)
plt.savefig('NintendoSalesNA.png')
plt.close(figure0)


# Best Sale Game Numbers
first_rank = data[data.Rank == 1]
game_name = first_rank.iloc[0]['Name']
plt.figure(figsize=(15,15))
plt.rcParams.update({'font.size': 22})
labels = ["NA Sales", "EU Sales", "JP Sales", "Other Sales"]
sizes = [first_rank.NA_Sales, first_rank.EU_Sales, first_rank.JP_Sales, first_rank.Other_Sales]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.05,0.05,0.05,0.05)
plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
#plt.tight_layout()
#plt.legend(labels, loc="best")
plt.title(game_name + " Sales")
plt.savefig('PieChart.png')


# Console Comparison Sales
consoles_names = list(set(data.Platform))
cnt = Counter()
for consoles_names in data.Platform:
    cnt[consoles_names] += 1
        
plt.figure(figsize=(15,15))
plt.rcParams.update({'font.size': 22})
x = cnt.keys()
y = cnt.values()
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, y, color='green')
plt.xlabel("Consoles")
plt.ylabel("Number of Titles Sold")
plt.title("Console Comparison Sales")
plt.xticks(x_pos, x, rotation=90)
plt.savefig('BarConsoles.png')   
