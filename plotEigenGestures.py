#!/usr/bin/env python

import sys, getopt, string
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *

def plot(vals, name):
  fig = plt.figure()
  fig.suptitle("\nParticipant Eigengestures on " + name + " Sample")
  gs = gridspec.GridSpec(len(vals), 3)
  
  row = 4
  col = 8
  X = []
  Y = []
  
  for i in range(0, row):
    x = []
    for j in range(0, col):
      x.append(j+1)
    X.append(x)
  
  for i in range(0, row):
    y = []
    for j in range(0, col):
      y.append(i+1)
    Y.append(y)
  
  for n in range(0, len(vals)):
    for i in range(0, len(vals[n])):
      Z = []
      for y in range(0, row):
        z = []
        for x in range(0, col):
          j = y*col + x
          z.append(vals[n][i][j])
        Z.append(z)
      
      ax = fig.add_subplot(gs[n,i], projection='3d')
      ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
      ax.set_xticks([1,2,3,4,5,6,7,8])
      ax.set_yticks([1,2,3,4])
      
      if(i==0):
        ax.text2D(-0.11,0.04,"Participant " + str(n+1),rotation='vertical')
        
      if(n==len(vals)-1):
        ax.text2D(-0.036,-0.13,"Eigengesture " + str(i+1))
      
  fig.tight_layout()
  plt.subplots_adjust(bottom=0.06, top=0.93, left=0.04)
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
