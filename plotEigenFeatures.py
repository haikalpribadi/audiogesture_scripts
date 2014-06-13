#!/usr/bin/env python

import sys, getopt, string
import numpy as np
import matplotlib.pyplot as plt

def plot(vals, name):
  fig = plt.figure()
  fig.suptitle("\n\n" +name + " Sample Eigenfeatures")
  
  for n in range(0, len(vals)):
    x = []
    y = []
    
    for i in range(0, len(vals[n])/2):
      x.append(vals[n][i])
      
    for i in range (len(vals[n])/2, len(vals[n])):
      y.append(vals[n][i])
      
    N = len(vals[n])/2
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    
    ax = fig.add_subplot(len(vals),1,n+1)
    rects1 = ax.bar(ind, x, width, color='b')
    rects2 = ax.bar(ind+width, y, width, color='y')

    labels = ['zcr', 'ctd', 'rlf', 'flx', 'mfcc0', 'mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11', 'mfcc12', 'chroma0', 'chroma1', 'chroma2', 'chroma3', 'chroma4', 'chroma5', 'chroma6', 'chroma7', 'chroma8', 'chroma9', 'chroma10', 'chroma11', 'av_chr_A', 'min_chr_A']
    
    spaces = []
    for i in range (0, len(vals[n])/2):
      spaces.append("")
    
    ax.set_ylabel('Eigenfeature ' + str(n+1))
    if(n==0):
      #ax.legend( (rects1[0], rects2[0]), ('Mean', 'Std'), loc='upper right', bbox_to_anchor=(0.1, -2.5))
      ax.legend( (rects1[0], rects2[0]), ('Mean', 'Std'), loc='upper right', bbox_to_anchor=(1.01, 1.55), prop={'size':11})
    
    if(n==len(vals)-1):
      ax.set_xticklabels( labels, rotation='vertical')
    else:
      ax.set_xticklabels( spaces, rotation='vertical')
      
    ax.set_xticks(ind+width)
    #if(n==len(vals)-1):
      #ax.set_xticklabels( labels, rotation='vertical')
      #ax.set_xticks(ind+width)
    #else:
      #plt.tick_params(axis='x', which='both', labelbottom='off')
    
    ax.set_ylim([-1, 1])
    ax.set_xlim([-0.5, 31])
    ax.xaxis.grid(True)
    
    
  plt.tight_layout()
  plt.margins(0.02)
  # Tweak spacing to prevent clipping of tick-labels
  plt.subplots_adjust(bottom=0.2, top=0.88)
  plt.show()


def main(argv):
  inputfile = ''
  outputfile = ''
  name = '';
  
  try:
    opts, args = getopt.getopt(argv,"hi:o:n:",["ifile=","ofile=","name="])
  except getopt.GetoptError:
    print "plotEigenFeatures.py -i <inputfile> -o <outputfile> -n <name>"
    sys.exit()
  for opt, arg in opts:
    if opt == '-h':
      print "plotEigenFeatures.py -i <inputfile> -o <outputfile> -n <name>"
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
