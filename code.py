import csv
import statistics 
import random
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
data = df['temp'].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(meanList):
    df = meanList
    sampling_mean = statistics.mean(meanList)
    print('The SAMPLING mean is: ', sampling_mean)
    fig = ff.create_distplot([df], ['temp'], show_hist = False)
    fig.show()

def setup():
    meanList = []
    for i in range(100):
        set_of_means = random_set_of_mean(30)
        meanList.append(set_of_means)
    show_fig(meanList)

population_mean = statistics.mean(data)
print('The POPULATION mean is: ', population_mean)
setup()