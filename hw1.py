#Open file to write to
extractedValues = open("extractedValues", "w")
#Open the log file
with open("dumpfile") as file:
    #Variable to hold contents of last line
    lastLine = None
    #counter1 for total lines stored, counter2 for individual vales extracted
    counter1 = 0
    counter2 = 0
    #Look through every line in the log file
    for line in file:
        #Reached next traceroute, need to then extract last good ms values from last traceroute
        if "---------------------------------" in line:
            if lastLine != None:
                #print lastLine
                prev = None
                #Look through the words and anything before "ms" gets stored in list
                for w in lastLine.split():
                    if (w=="ms") and (prev is not None):
                        #print prev
                        #write value to file
                        extractedValues.write(prev+'\n')
                        counter2 = counter2 + 1
                    prev = w
                lastLine = None
                counter1=counter1+1
        #Set last line to the last read line that isn't hidden
        elif ("* * *" not in line) and ("---------------------------------" not in line):
            lastLine = line
#Close the file for writting
extractedValues.close()
            
#Print counter statistics
print "Total traceroutes: "+str(counter1)
print "Total values extracted: "+str(counter2)

#-----------------------------Can be run as a separate file from below if desired-----------------------------

import numpy as np
import matplotlib.pyplot as plot

#Array to hold values written from file
latencies = []

#Take the values written from file and save to an array
with open("extractedValues") as file:
    for line in file:
        latencies.append(float(line))

#Form the plot with desired title and labels
#Source for cdf-http://web.stanford.edu/~raejoon/blog/2017/05/16/python-recipes-for-cdfs.html
counts, binEdges = np.histogram (latencies, bins=len(latencies),normed=True)
cdf = np.cumsum (counts)
plot.plot (binEdges[1:], cdf/cdf[-1])
plot.ylabel("Probability")
plot.xlabel("Delay (ms)")
plot.title("CDF of Latency for www.yahoo.co.jp Over 24 Hours")
plot.show()
        
