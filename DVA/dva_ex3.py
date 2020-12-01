# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:51:12 2020

@author: HYEBIN
"""

import numpy as np
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Button, Select, Div
from bokeh.plotting import figure, curdoc
from bokeh.sampledata.iris import flowers


# Important: You must also install pandas for the data import.

# calculate the cost of the current medoid configuration
# The cost is the sum of all minimal distances of all points to the closest medoids
def get_cost(medoids):
    data_ = data[data.columns[:4]]
    temp_ = data[data.columns[:4]].values
    aa = []
    for row in temp_:
        a = []
        for med in medoids:
            a.append(sum(abs(row - data_.iloc[med,].values)))
        aa.append(a)
    data["dist"] = aa
    data['cost'] = data['dist'].apply(min)
    cost_of_clustering = data['cost'].sum()

    return cost_of_clustering


# implement the k-medoids algorithm in this function and hook it to the callback of the button in the dashboard
# check the value of the select widget and use random medoids if it is set to true and use the pre-defined medoids
# if it is set to false.
def k_medoids(is_random):
    # number of clusters:
    k = 3
    if is_random == 'True':
        medoids = list(np.random.choice(data.index, k))
    else:
        # Use the following medoids if random medoid is set to false in the dashboard.
        # These numbers are indices into the data array.
        medoids = [24, 74, 124]
    cost_decreased = True
    while cost_decreased:
        cost = get_cost(medoids)
        data['cluster'] = data['dist'].apply(np.argmin)
        clustered_data = data.groupby('cluster')
        lowest_cost = cost.copy()
        ## Swap every medoid with every data point and recalculate the clustering cost to check if it decreases.
        ## This way you find the best medoid (minimal cost) for every cluster.
        for idx, cdf in clustered_data:
            test_medoids = medoids.copy()
            for new_point in cdf.index:
                test_medoids[idx] = new_point
                test_cost = get_cost(test_medoids)
                if lowest_cost >= test_cost:
                    ## this new point makes lower cost. swap medoids
                    medoids = test_medoids.copy()
                    lowest_cost = test_cost.copy()
        cost_decreased = cost > lowest_cost
    return lowest_cost


def click():
    div.text = f'{"The final cost is : calculating..."}'
    curdoc().add_next_tick_callback(start_clustering)


# select = Select(title="Random Medoids", value="False", options=["False", "True"])
def start_clustering():
    is_random = select.value
    final_cost = k_medoids(is_random)
    color_map = {0: 'red', 1: 'green', 2: 'blue'}
    data['color'] = data['cluster'].map(color_map)
    source = ColumnDataSource(data=data)

    p1.circle(x="petal_length", y="sepal_length", color="color", fill_alpha=0.5, size=5, source=source)
    p2.circle(x="petal_width", y="petal_length", color="color", fill_alpha=0.5, size=5, source=source)
    # div.text = "The final cost is : {0:0.2f}".format(final_cost)
    div.text = "The final cost is :" + str(my_round(final_cost, 2))
    div.text = "The final cost is :" + str(final_cost)


def my_round(number: float = 42.625, digit: int = 2):
    num = str(number) + "0" * digit
    tail = num.split(".")[1]
    t = tail[digit]
    if int(t) >= 5:
        number += 0.1 ** (digit + 1)
    number = round(number, digit)
    return number


# read and store the dataset
data = flowers.copy(deep=True)
data = data.drop(['species'], axis=1)

# create a color column in your dataframe and set it to gray on startup
data['color'] = 'gray'

# Create a ColumnDataSource from the data
source = ColumnDataSource(data=data)

# Create a select widget, a button, a DIV to show the final clustering cost and two figures for the scatter plots.
# select = Select(title="Random Medoids", value="False", options=["False", "True"])
select = Select(title="Random Medoids", value="False", options=["False", "True"])
button = Button(label="Cluster data", button_type="default")
div = Div(text=f'{"The final cost is : click [Cluster data] button above."}')

p1 = figure(title="Scatterplot of flower distribution by petal length and sepal length",
            x_axis_label='Petal_length', y_axis_label='Sepal_length', height=500, width=500)
p2 = figure(title="Scatterplot of flower distribution by petal width and petal length",
            x_axis_label='Petal_width', y_axis_label='Petal_length', height=500, width=500)
p1.circle(x="petal_length", y="sepal_length", color="color", fill_alpha=0.5, size=5, source=source)
p2.circle(x="petal_width", y="petal_length", color="color", fill_alpha=0.5, size=5, source=source)

button.on_click(click)

layout = row(column(select, button, div), column(p1), column(p2))

# # use curdoc to add your widgets to the document
curdoc().add_root(layout)
curdoc().title = "DVA_ex_3"

# # use on of the commands below to start your application
# # bokeh serve --show dva_ex3_skeleton_HS20.py
# # python -m bokeh serve --show dva_ex3_skeleton_HS20.py
# # bokeh serve --dev --show dva_ex3_skeleton_HS20.py
# # python -m bokeh serve --dev --show dva_ex3_skeleton_HS20.py
