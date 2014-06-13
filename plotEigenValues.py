#!/usr/bin/env python

import sys, getopt, string
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def plot(vals, name):
  fig = plt.figure()
  fig.suptitle(name + " Top 20 Eigenvalues")
  
  for n in range(0, len(vals)):
    x = arange(0,len(vals[n]),1)
    y = []
    
    ax = fig.add_subplot(1,len(vals),n+1)
    
    for i in range(0, len(vals[n])):
      y.append(vals[n][i])
    
    ax.plot(x,y);
    ax.set_ylim([0, 1])
    ax.set_xlim([0, 20])
    ax.set_xlabel("EV number\n(sample " + str(n+1) +")")
    if(n==0):
      ax.set_ylabel("Eigenvalue score")
  
  fig.tight_layout()
  plt.subplots_adjust(bottom=0.2, top=0.88)
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
    file = open(f, "rb")
    for line in file.xreadlines():
      vals.append([float(val) for val in string.split(line, ",") if val != '\n'])
  
  plot(vals, name)
    
  


if __name__ == "__main__":
  main(sys.argv[1:])
