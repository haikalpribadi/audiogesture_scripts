#!/usr/bin/env python

import sys, getopt, string
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *

def plot(vals, name):
  fig = plt.figure()
  fig.suptitle(name + " Magnitude Correlation")
  
  x = [1,2,3]
  labels = ["Feature mag. 1 contribution","Feature mag. 2 contribution","Feature mag. 3 contribution"]
  for n in range(0, len(vals)):
    ax = fig.add_subplot(2,2,n+1)
    
    for i in range(0, len(vals[n])):
      y = []
      for j in range(0, len(vals[n][i])):
        y.append(vals[n][i][j])
      ax.plot(x,y, "o-", label=labels[i]) #,color=colors[i], label=labels[i])
    
    ax.set_xticks([1,2,3])
    ax.set_xlim([0.8,3.2])
    
    #if(n%2==0):
    ax.set_ylabel("Feature mag. contribution")
    #if(n/2>=1):
    ax.set_xlabel("Gesture mag. coefficients")
    ax.set_title("Participant " + str(n+1),fontsize=12)
  
  #legend(prop={'size':11}, bbox_to_anchor=(1.019, 2.85))
  fig.tight_layout()
  plt.subplots_adjust(top=0.9)
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
