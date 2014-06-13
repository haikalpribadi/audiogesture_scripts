#!/usr/bin/env python

import sys, getopt, string
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *


def plot(vals, name, ids):
  fig = plt.figure(figsize=(10,11))
  fig.suptitle("Selected Sequence of Generated Gestures from Music Stream")
  
  w = 5
  h = 6 #len(vals)/w + 1
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
  
  for i in range(0, min(len(vals),w*h)):
    Z = []
    for y in range(0, row):
      z = []
      for x in range(0, col):
        j = y*col + x
        z.append(vals[i][j])
      Z.append(z)

    ax = fig.add_subplot(h, w, i+1, projection='3d')
    ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
    ax.set_xticks([1,2,3,4,5,6,7,8])
    ax.set_yticks([1,2,3,4])
    ax.set_zticks([1,2,3,4])
    ax.set_zlim(0,4)

    #ax.text2D(-0.09, 0.07, str(ids[i]))
      
  fig.tight_layout()
  plt.subplots_adjust(top=0.955)
  plt.show()


def main(argv):
  inputfile = ''
  outputfile = ''
  filterfile = ''
  name = ''
  
  try:
    opts, args = getopt.getopt(argv,"hi:o:n:f:",["ifile=","ofile=","name=", "filter="])
  except getopt.GetoptError:
    print "plotGestureOuput.py -i <inputfile> -o <outputfile> -n <name> -f <filterfile>"
    sys.exit()
  for opt, arg in opts:
    if opt == '-h':
      print "plotGestureOutput.py -i <inputfile> -o <outputfile> -n <name> -f <filterfile>"
      sys.exit()
    elif opt in("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--outfile"):
      outputfile = arg
    elif opt in ("-n", "--name"):
      name = arg
    elif opt in ("-f", "--file"):
      filterfile = arg
  
  print "Input file is:", inputfile
  print "Output file is:", outputfile
  print "Filter file is:", filterfile
  
  file = open(filterfile)
  filter = [float(val) for val in string.split(file.readline(), ",") if val != '\n']
  
  #st = ''
  #for i in range (61,121):
  #  st += str(i) + ","
  #  
  #print st
  
  file = open(inputfile, "rb")
  vals = []
  ids = []
  i = 0
  j = 0
  for line in file.xreadlines():
    if (j>=len(filter)):
      break
    i = i+1
    if (i!=filter[j]):
      continue
    ids.append(i)
    j = j+1
    vals.append([float(val) for val in string.split(line, ",") if val != '\n'])
  
  plot(vals, name, ids)


if __name__ == "__main__":
  main(sys.argv[1:])