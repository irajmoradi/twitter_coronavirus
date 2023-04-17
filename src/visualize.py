#!/usr/bin/env python3
import matplotlib
import numpy as np
matplotlib.use('Agg')

import matplotlib.pyplot as plt
# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]
z =0
list1 = []
list2 = []
# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
#    print(k,':',v)
    z += 1
    if z < 12:
        list1.append(k)
        list2.append(v)
n = len(list1)
ind = np.arange(n)
if "country" in str(args.input_path):
    strx = "Country"
else:
    strx = "Language"
p1 = plt.bar(ind, list2, .5)
plt.ylabel('# of Tweets')
plt.xticks(ind, list1)
plt.xlabel(strx)
strkey = str(args.key)

#plt.yticks(np.arange(0, max(v), 10))
#print(args.key)
#print("strtitle=", strtitle)
filename = strx + strkey + ".png"
plt.savefig(filename, bbox_inches = "tight")
