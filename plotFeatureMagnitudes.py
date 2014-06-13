#!/usr/bin/env python

import sys, getopt, string
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def plot(vals, name):
  fig = plt.figure()
  fig.suptitle("\n" + name + " Sample Eigenfeature Magnitudes")
  
  ax = fig.add_subplot(1,1,1)
  duration = float(len(vals[0])) / 30
  rate = 1./30;
  
  colors = ["green", "blue", "red"]
  labels = ["Eigenfeature 1", "Eigenfeature 2", "Eigenfeature 3"]
  for n in range(0, len(vals)):
    x = arange(0,duration-0.001,rate)
    y = []
    
    for i in range(0, len(vals[n])):
      y.append(vals[n][i])
      
    ax.plot(x,y, color=colors[n], label=labels[n], zorder=n)
    
  legend(prop={'size':11}, bbox_to_anchor=(1.01, 1.16))
  #ax.set_ylim([0, 10])
  ax.set_xlim([0, duration])
  ax.set_ylabel("Eigenfeature contribution")
  ax.set_xlabel("time (s)")
  fig.tight_layout()
  plt.subplots_adjust(bottom=0.15, top=0.88)
  plt.show()

def main(argv):
  inputfile = ''
  outputfile = ''
  name = ''
  
  try:
    opts, args = getopt.getopt(argv,"hi:o:n:",["ifile=","ofile=","name="])
  except getopt.GetoptError:
    print "plotFeatureMagnitudes.py -i <inputfile> -o <outputfile> -n <name>"
    sys.exit()
  for opt, arg in opts:
    if opt == '-h':
      print "plotFeatureMagnitudes.py -i <inputfile> -o <outputfile> -n <name>"
      sys.exit()
    elif opt in("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--outfile"):
      outputfile = arg
    elif opt in ("-n", "--name"):
      name = arg
  
  print "Input file is:", inputfile
  print "Output file is:", outputfile
  
  file = open(inputfile, "rb")
  
  vals = []
  for line in file.xreadlines():
    vals.append([float(val) for val in string.split(line, ",") if val != '\n'])
  
  plot(vals, name)
    
  


if __name__ == "__main__":
  main(sys.argv[1:])
