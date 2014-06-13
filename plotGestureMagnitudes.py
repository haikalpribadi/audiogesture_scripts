#!/usr/bin/env python

import sys, getopt, string
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *

def plot(vals, name):
  fig = plt.figure()
  fig.suptitle("\n\nParticipant Eigengesture Magnitudes for " + name + " Sample")
  gs = gridspec.GridSpec(int(math.ceil(len(vals)/2)), min(len(vals),2))
  
  rate = 1./30;
  colors = ["green", "blue", "red"]
  labels = ["Eigengesture 1", "Eigengesture 2", "Eigengesture 3"]
  
  for n in range(0, len(vals)):
    ax = fig.add_subplot(gs[int(n/2),int(n%2)])
    duration = float(len(vals[n][0])) / 30
    x = arange(0,duration-0.001,rate)
    for i in range(0, len(vals[n])):
      y = []
      for j in range(0, len(vals[n][i])):
        y.append(vals[n][i][j])
      ax.plot(x,y, color=colors[i], label=labels[i])
    
    ax.set_xlim([0, duration])
    ax.set_xlabel("time (s)")
    ax.set_ylabel("Eigengesture contribution")
    ax.set_title("Participant " + str(n+1),fontsize=12)
  
  legend(prop={'size':11}, bbox_to_anchor=(1.019, 2.85))
  fig.tight_layout()
  plt.subplots_adjust(left=0.08,top=0.85)
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
