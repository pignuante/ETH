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
    data_ = np.array(data.iloc[:, :4])
    meds_ = np.array(data.loc[medoids, col])

    medoids_list = []
    for med in range(len(medoids)):
        row = np.sum(abs(data_ - meds_[med]), axis=1)
        medoids_list.append(row)

    medoids_array = np.array(np.transpose(medoids_list))
    min_value = np.min(medoids_array, axis=1)
    cost_of_clustering = np.sum(min_value)

    data['medoids'] = list(np.transpose(medoids_list))
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
        medoids = [92, 83, 37]

    cost = get_cost(medoids)
    lowest_medoids = medoids.copy()

    cost_decreased = True
    while cost_decreased:
        cost_decreased = False
        ## Swap every medoid with every data point and recalculate the clustering cost to check if it decreases.
        ## This way you find the best medoid (minimal cost) for every cluster.
        for idx, cdf in enumerate(lowest_medoids):
            test_medoids = lowest_medoids.copy()
            for new_point in data.index:
                if new_point == cdf:
                    continue
                test_medoids[idx] = new_point
                test_cost = get_cost(test_medoids)
                if cost > test_cost:
                    updated_idx = idx
                    updated_new_point = new_point
                    cost_decreased = True
                    cost = test_cost
        if cost_decreased:
            lowest_medoids[updated_idx] = updated_new_point
            get_cost(lowest_medoids)
            data['cluster'] = data['medoids'].apply(np.argmin)
    return cost


def start_clustering():
    is_random = select.value
    final_cost = k_medoids(is_random)
    color_map = {0: 'red', 1: 'green', 2: 'blue'}
    # source = ColumnDataSource(data = data)
    source.data['color'] = data['cluster'].map(color_map)

    # p1.circle(x="petal_length",y="sepal_length",color = "color",fill_alpha = 0.5,size=5,source=source)
    # p2.circle(x="petal_width",y="petal_length",color = "color",fill_alpha = 0.5,size=5,source=source)
    div.text = "The final cost is : {}".format(final_cost)


def click():
    div.text = f'{"The final cost is : calculating..."}'
    curdoc().add_next_tick_callback(start_clustering)


if __name__ == "__main__":
    # read and store the dataset
    data = flowers.copy(deep=True)
    data = data.drop(['species'], axis=1)

    # create a color column in your dataframe and set it to gray on startup
    data['color'] = 'gray'
    col = data.columns.tolist()[:4]

    # Create a ColumnDataSource from the data
    source = ColumnDataSource(data=data)

    # Create a select widget, a button, a DIV to show the final clustering cost and two figures for the scatter plots.
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
