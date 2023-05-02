#!/usr/bin/env python3

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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

#sorted_items = sorted(items.items(), key = lambda x: x[1])

#x_axis = []
#y_axis = []

#for x in items[0:10]:
#    x_axis.append(x[0])

#for y in items[0:10]:
#    y_axis.append(y[1])

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True
#
#index = range(len(x_axis))[::-1]
#plt.bar(index, y_axis)
#plt.xticks(index, x_axis)
#print("args.input_path=", type(args.input_path))
#if str(args.key) == 'lang':
#    plt.title (f'Twitter Usage of {args.key} by Language in 2020') 
#    plt.xlabel ('Language')
#    plt.ylabel ('Count')
#    plt.show()
#    plt.savefig (f'lang2 {args.key} barchart.png')
#else:
#    plt.title (f'Twitter Usage of {args.key} by Language in 2020')
#    plt.xlabel ('Country')
#    plt.ylabel ('Count')
#    plt.show()
#    plt.savefig (f'country{args.key} barchart.png')
for k,v in items:
    #list1.append(k)
    #list2.append(v)
    print(k, ':' ,v)
#print(list1)
#print(list2)
top_items = items[:10]
keys = [item[0] for item in top_items]
values = [item[1] for item in top_items]
keys = keys[::-1]
values = values[::-1]

plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)

if args.input_path[-1] == 'g': 
    plt.xlabel('Language')
else:
    plt.xlabel('Country')
if args.percent:
    ply.ylabel('Percent of Total')
else:
    plt.ylabel('Tweet Volume')
if args.input_path[-1] == 'g':
    plt.savefig(args.key[1:] + '_lang.png')
else:
    plt.savefig(args.key[1:] + '_country.png')
