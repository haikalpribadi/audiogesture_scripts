#!/usr/bin/env python

import sys, getopt, string
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *

def plot(vals, name):
  fig = plt.figure()
  fig.suptitle("Magnitude Correlation from Audio \n Samples to Participant Gestures")
  
  x = [1,2,3]
  colors = ["g","b","m"]
  markers = ["go-", "bo-", "ro-"]
  labels = ["Feature mag. 1","Feature mag. 2","Feature mag. 3"]
  for n in range(0, len(vals)):
    ymin = -0.61
    ymax = 0.8
    ax = fig.add_subplot(4,4,n+1)
    cmax = 0
    cmin = 0
    for i in range(0, len(vals[n])):
      y = []
      for j in range(0, len(vals[n][i])):
        y.append(-1*vals[n][i][j])
      ax.plot(x,y, markers[i], label=labels[i])
      if(max(y)>cmax):
        cmax = max(y)
      if(min(y)<cmin):
        cmin = min(y)
    
    ax.set_xticks([1,2,3])
    ax.set_xlim([0.8,3.2])
    while(cmax>ymax):
      ymax += 0.5
    while(cmin<ymin):
      ymin -= 0.5
    ax.set_ylim([ymin,ymax])
      
    if(n%4==0):
      ax.set_ylabel("Sample " + str((n/4)+1))
    if(n/4==3):
      ax.set_xlabel("Participant " + str((n%4)+1))
  
  legend(prop={'size':11}, bbox_to_anchor=(1.15, 5.06))
  fig.tight_layout(pad=0)
  fig.text(0.015,0.69,"y-axis: Feature magnitude contribution", rotation="vertical")
  fig.text(0.4,0.02,"x-axis: Gesture magnitude coefficient")
  plt.subplots_adjust(left=0.1,top=0.915,right=0.97,bottom=0.1)
  plt.show()
  
      
      
def main(argv):
  inputfile = ''
  outputfile = ''
  name = ''
  
  try:
    opts, args = getopt.getopt(argv,"hi:o:n:",["ifile=","ofile=","name="])
  except getopt.GetoptError:
    print "plotEigenValues.py -i <inputfile> -o <outputfile> -n <name>"
    sys.exit()
  for opt, arg in opts:
    if opt == '-h':
      print "plotEigenValues.py -i <inputfile> -o <outputfile> -n <name>"
      sys.exit()
    elif opt in("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--outfile"):
      outputfile = arg
    elif opt in ("-n", "--name"):
      name = arg
  
  print "Input file is:", inputfile
  print "Output file is:", outputfile
  
  vals = []
  files = string.split(inputfile, ":")
  for f in files:
    val = []
    file = open(f, "rb")
    for line in file.xreadlines():
      val.append([float(v) for v in string.split(line, ",") if v != '\n'])
    vals.append(val)
  
  plot(vals, name)
    
  


if __name__ == "__main__":
  main(sys.argv[1:])
