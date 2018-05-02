# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 04:36:22 2018

@author: ChenZhengyang
"""
import csv
from matplotlib import pyplot
import numpy as np

def plot_iter_time(filename):
    ittdata=[]
    with open (filename,'r') as csvfile:
        ittfile=csv.reader(csvfile)
        for row in ittfile:
            nums=[]
            for item in row:
                nums.append(float(item))
                #print (nums)
            ittdata.append(nums)

    pyplot.plot(ittdata[0], linewidth=2, label = "randomized hill climbing")
    pyplot.plot(ittdata[2], linewidth=2, label = "simulation annealing")
    pyplot.plot(ittdata[4], linewidth=2, label = "generic algorithm")
    pyplot.plot(ittdata[6], linewidth=2, label = "MIMIC")
    pyplot.legend()
    pyplot.xlim(0,20)
    pyplot.xlabel("iteration")
    pyplot.ylabel("optimal finding")
    pyplot.show()

    pyplot.plot(ittdata[1], linewidth=2, label = "randomized hill climbing")
    pyplot.plot(ittdata[3], linewidth=2, label = "simulation annealing")
    pyplot.plot(ittdata[5], linewidth=2, label = "generic algorithm")
    pyplot.plot(ittdata[7], linewidth=2, label = "MIMIC")
    pyplot.legend()
    pyplot.xlim(0,20)
    pyplot.xlabel("iteration")
    pyplot.ylabel("time consuming")
    pyplot.show()
    
    pyplot.plot(ittdata[8], linewidth=2, label = "randomized hill climbing")
    pyplot.plot(ittdata[10], linewidth=2, label = "simulation annealing")
    pyplot.plot(ittdata[12], linewidth=2, label = "generic algorithm")
    pyplot.plot(ittdata[14], linewidth=2, label = "MIMIC")
    pyplot.legend()
    pyplot.xlabel("input numbers")
    pyplot.ylabel("optimal finding")
    pyplot.show()

    pyplot.plot(ittdata[9], linewidth=2, label = "randomized hill climbing")
    pyplot.plot(ittdata[11], linewidth=2, label = "simulation annealing")
    pyplot.plot(ittdata[13], linewidth=2, label = "generic algorithm")
    pyplot.plot(ittdata[15], linewidth=2, label = "MIMIC")
    pyplot.legend()
    pyplot.xlabel("input numbers")
    pyplot.ylabel("time consuming")
    pyplot.show()
    
plot_iter_time("cpdata.csv")
plot_iter_time("tspdata.csv")
plot_iter_time("ksdata.csv")




