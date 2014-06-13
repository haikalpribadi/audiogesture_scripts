#!/usr/bin/env python

import sys, getopt, string
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *

def plot(vals, name, cut, delay, shift):
  fig = plt.figure(figsize=(12,5))
  fig.suptitle("\nGenerated Gesture Responses from Live Audio")
  duration = float(len(vals[1][0])) / 10
  duration = 60
  
  colors = ["green", "blue", "red","#415C9E"]
  labels = ["Gesture mag. 1","Gesture mag. 2","Gesture mag. 3","Feature mag. 1","Feature mag. 2","Feature mag. 3"]
  ylabels = ["Generated Gestures", "Live Audio Features"]
  for n in range(0, len(vals)):
    ax = fig.add_subplot(2,1,n+1)
    dur = float(len(vals[n][0])) / 10
    rate = 1./10
    s = shift
    x = arange(0,dur-0.01,rate)
    cuts = (x > 0) & (x >= delay) & (x < (dur-s)) & ((x-delay) % cut == 0)
    
    for i in range(0, len(vals[n])):
      y = []
      for j in range(0, len(vals[n][i])):
        y.append(vals[n][i][j])
      ax.plot(x,y, color=colors[i], label=labels[i+n*3])
      
    if(n<len(vals)-1):
      ax.get_xaxis().set_visible(False)
      for c in x[cuts]:
        ax.axvline(x=c,ymin=-0.4,ymax=1,c=colors[3],linewidth=1,zorder=0, clip_on=False)
    else:
      ax.set_xlabel("time (s)")
      for c in x[cuts]:
        ax.axvline(x=c,ymin=0,ymax=1,c=colors[3],linewidth=1,zorder=0, clip_on=False)
    ax.set_ylabel(ylabels[n])
    ax.set_xlim([0, duration-s])
    l = legend(prop={'size':10}, bbox_to_anchor=(1.015, 1.094))
    l.set_zorder(20)
    
    #ax.set_title("Participant " + str(n+1),fontsize=11)
  
  
  fig.tight_layout(h_pad=0.3)
  plt.subplots_adjust(left=0.08, top=0.9)
  plt.show()
  
      
      
def main(argv):
  inputfile = ''
  outputfile = ''
  name = ''
  cut = 0.0
  delay = 0.0
  shift = 0.0
  
  try:
    opts, args = getopt.getopt(argv,"hi:o:n:c:d:s:",["ifile=","ofile=","name=","cut=","delay=", "shift="])
  except getopt.GetoptError:
    print "plotEigenValues.py -i <inputfile> -o <outputfile> -n <name> -c <cut> -d <delay> -s <shift>"
    sys.exit()
  for opt, arg in opts:
    if opt == '-h':
      print "plotEigenValues.py -i <inputfile> -o <outputfile> -n <name> -c <cut> -d <delay> -s <shift>"
      sys.exit()
    elif opt in("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--outfile"):
      outputfile = arg
    elif opt in ("-n", "--name"):
      name = arg
    elif opt in ("-c", "--cut"):
      cut = float(arg)
    elif opt in ("-d", "--delay"):
      delay = float(arg)
    elif opt in ("-s", "--shift"):
      shift = float(arg)
      
  
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
  
  plot(vals, name, cut, delay, shift)
    
  


if __name__ == "__main__":
  main(sys.argv[1:])
