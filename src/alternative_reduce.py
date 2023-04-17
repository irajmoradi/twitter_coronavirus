#!/usr/bin/env python3
import matplotlib
import numpy as np
matplotlib.use('Agg')

import matplotlib.pyplot as plt
# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys',nargs='+',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()


# imports
import os
import json
from collections import Counter,defaultdict

for key in args.keys:
    # load each of the input paths
    sorted(args.input_paths)
    yaxis = []
    total = defaultdict(lambda: Counter())
    for path in args.input_paths:
        with open(path) as f:
            tmp = json.load(f)
            sumofnum = 0
            try:
                for k in tmp[key]:
                    sumofnum += tmp[key][k]
            except:
                pass
            yaxis.append(sumofnum)
    plt.plot(np.arange(366), yaxis, label = key)
plt.xlabel("Date in 2020") 
plt.ylabel("# of Tweets")
plt.title("Number of Tweets of a given hashtag by day in 2020")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sept", "Nov"])
plt.savefig("hi.png", bbox_inches = "tight")



