#!/usr/bin/env python

import sys, getopt, string
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *


def plotFeature(ax, feature):
  x = []
  y = []
  
  for i in range(0, len(feature)/2):
    x.append(feature[i])
  
  for i in range(len(feature)/2, len(feature)):
    y.append(feature[i])
  
  N = len(feature)/2
  ind = np.arange(N)
  width = 0.35
  
  rects1 = ax.bar(ind, x, width, color='b')
  rects2 = ax.bar(ind+width, y, width, color='y')
  
  labels = ['zcr', 'ctd', 'rlf', 'flx', 'mfcc0', 'mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11', 'mfcc12', 'chroma0', 'chroma1', 'chroma2', 'chroma3', 'chroma4', 'chroma5', 'chroma6', 'chroma7', 'chroma8', 'chroma9', 'chroma10', 'chroma11', 'av_chr_A', 'min_chr_A']
  
  ax.legend( (rects1[0], rects2[0]), ('Mean', 'Std'), loc='upper right', bbox_to_anchor=(1.01, 1.55), prop={'size':11})
  ax.set_xticklabels( labels, rotation='vertical')
  ax.set_xticks(ind+width)
  ax.set_ylim([0, 1])
  ax.set_xlim([-0.5, 31])
  
  
  
  
def plotGesture(ax, gesture):
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
  
  Z = []
  for y in range(0, row):
    z = []
    for x in range(0, col):
      j = y*col + x
      z.append(gesture[j])
    Z.append(z)
  
  ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
  ax.set_xticks([1,2,3,4,5,6,7,8])
  ax.set_yticks([1,2,3,4])
  ax.set_zlim([0,2])


def main(argv):
  inputfile = ''
  outputfile = ''
  filterfile = ''
  name = ''
  
  try:
    opts, args = getopt.getopt(argv,"hi:o:n:f:",["ifile=","ofile=","name=", "filter="])
  except getopt.GetoptError:
    print "plotEigenValues.py -i <inputfile> -o <outputfile> -n <name> -f <filterfile>"
    sys.exit()
  for opt, arg in opts:
    if opt == '-h':
      print "plotEigenValues.py -i <inputfile> -o <outputfile> -n <name> -f <filterfile>"
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
  vals = []
  files = string.split(inputfile, ":")
  
  for f in files:
    val = []
    file = open(f, "rb")
    for line in file.xreadlines():
      val.append([float(v) for v in string.split(line, ",") if v != '\n'])
    vals.append(val)
    
  file = open(filterfile)
  filter = string.split(file.readline(), ",")
  
  for i in range(0, len(vals[0])):
    print "Output Record", i+1
    fig = plt.figure(figsize=(12,5))
    fig.suptitle("")
    
    ax = fig.add_subplot(1,2,1)
    plotFeature(ax, vals[0][i])

    ax = fig.add_subplot(1,2,2, projection='3d')
    plotGesture(ax, vals[1][i])

    plt.tight_layout()
    #plt.margins(0.02)
    plt.subplots_adjust(bottom=0.2, top=0.88)
    plt.show()


if __name__ == "__main__":
  main(sys.argv[1:])