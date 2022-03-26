import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random

#standard deviation of *mean sampling distribution* = standard deviation of the population / sqrt of (number of sample in each sample) here number of data in each sample was 100 so standard deviation of the mean sampling distribution was 1/10 th of the population
# In simple language we take a load of samples from the population then, we take the mean of these different sample and plot it. And it turns out that although the population of where our sample come from is not normal distribution the plot of means of the samples we take from the population comes out to be normal 
# And the means of the population and the mean of the (mean of  different samples from population) are the same 


#Standard deviation of sampling mean distribution or Standard Error of the Mean (SEM) is calculated by taking the standard deviation and dividing it by the square root of the sample size.
#Standard error gives the accuracy of a sample mean by measuring the sample-to-sample variability of the sample means. The SEM describes how precise the mean of the sample is as an estimate of the true mean of the population. As the size of the sample data grows larger, the SEM decreases versus the SD; hence, as the sample size increases, the sample mean estimates the true mean of the population with greater precision. In contrast, increasing the sample size does not make the SD necessarily larger or smaller, it just becomes a more accurate estimate of the population SD.
df = pd.read_csv("newData.csv")
data = df["average"].tolist()
mean = statistics.mean(data)
sd = statistics.stdev(data)
print(mean , 'mean of the population')
print(sd, "standard deviation of the population")
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
    print(meanSample , 'mean of mean sampling distribution')
    print(sdSample, "standard deviation of the mean sampling distribution ")
    fig = ff.create_distplot([df] , ["average sample"] , show_hist=False)
    fig.add_trace(go.Scatter(x = [mean , mean] , y  = [0 , 1] , mode = "lines" , name = "mean"))
    fig.show()
def main():
    meanlist = []
    for i in range(0,1000):
        set_of_means = randomSetOfMean(100)
        meanlist.append(set_of_means)
    showfig(meanlist)
main()

#100 value will be taken to get the mean each time with this function. randomSetOfMean(100)
#So this function gives us one mean which we get from taking 100** (or whatever counter times) random values from the population data
#This function is called 1000 times in this for loop so we will 1000 means in the meanlist 