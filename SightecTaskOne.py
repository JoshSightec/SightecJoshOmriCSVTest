import re #imports regex library to be used in python
import csv #used to write to csv files
import pandas as pd

#with open('_loggertracks - _loggertracks.csv', 'r', encoding='UTF8') as readFile:
  #add another with open for second file
  #for line in readFile:
    #take the same line in the other file
    #get a specific csv from both files in that line - use regex
    #compare - maybe do a difference calculation so abs(firstValue - secondValue) and convert to percentage
    #output all values that have a percentage difference higher than a set threshold
    #???
    #profit


df = pd.read_csv('_loggertracks - _loggertracks.csv', usecols = ['topLeftY','centerOfMassX'])
print(df)

df = pd.read_csv('_loggertracks - _loggertracks.csv', usecols=['trackId'])#.tail(1)
dups = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:'count'})
print(dups)
#find out how many track id 1s there are in either and work out difference
#once we have difference we ant to save to another file all the frames that there is a difference  between
dupsFirstFileCount = dups["count"][0]
print(dupsFirstFileCount)

df = pd.read_csv('_loggertracks.csv', usecols=['trackId'])#.tail(1)
dups = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:'count'})


dupsSecondFileCount = dups["count"][0]
print(dupsSecondFileCount)
difference = abs(dupsFirstFileCount - dupsSecondFileCount)
print(difference)


#idk do now from the 1513th line to the 1560th line and look at those lines or smth idk