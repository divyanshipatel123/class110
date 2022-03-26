import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random
df = pd.read_csv("data.csv")
data = df["temp"].tolist()
mean = statistics.mean(data)
sd = statistics.stdev(data)
#fig.show()
#print(mean , sd)
#print(meanSample,sdSample,"of the sample of 100 data points")
def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,(len(data)-1))
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def showfig(meanlist):
    df = meanlist
    meanSample = statistics.mean(meanlist)
    sdSample = statistics.stdev(meanlist)
    print(meanSample , 'mean of the sample')
    print(sdSample, "standard deviation of the sample ")

    fig = ff.create_distplot([df] , ["tempertaure sample"] , show_hist=False)
    fig.add_trace(go.Scatter(x = [mean , mean] , y  = [0 , 1] , mode = "lines" , name = "mean"))
    fig.show()
def main():
    meanlist = []
    for i in range(0,1000):
        set_of_means = randomSetOfMean(100)
        meanlist.append(set_of_means)
    showfig(meanlist)
main()


    