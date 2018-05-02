# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:26:43 2018

@author: ChenZhengyang
"""

import csv
from matplotlib import pyplot
import numpy as np
import pandas as pd

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
    pyplot.plot(ittdata[1], linewidth=2, label = "simulation annealing")
    pyplot.plot(ittdata[2], linewidth=2, label = "generic algorithm")
    pyplot.legend()
    pyplot.xlabel("instances")
    pyplot.ylabel("accuracy_score")
    pyplot.show()

def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

def plot_diagram(filename):
    disdata=[]
    with open (filename,'r') as csvfile:
        distfile=csv.reader(csvfile)
        for row in distfile:
            nums=[]
            for item in row:
                nums.append(float(item))
                #print (nums)
            disdata.append(nums)
        
    for i in range(3):
        sco=disdata[3*i]
        trt=disdata[3*i+1]
        tst=disdata[3*i+2]
        plot_dist(sco,np.mean(sco),np.std(sco),np.min(sco),np.max(sco),1,\
              'correctness','probability','correctness score')
        plot_dist(trt,np.mean(trt),np.std(trt),np.min(trt),np.max(trt),0.1,\
              'train time','probability','traintime diagram')
        plot_dist(tst,np.mean(tst),np.std(tst),np.min(tst),np.max(tst),0.001,\
              'test time','probability','testtime diagram')
        
    labels=['randomized hill climbing','simulation annealing','generic algorithm']
    for i in range(3):
        sco=disdata[3*i]
        plot_compare(sco,np.mean(sco),np.std(sco),30,90,1,labels[i])
    plt.title('correctness score')
    plt.xlabel('correctness')
    plt.ylabel('probability')
    plt.legend()
    plt.show()
    for i in range(3):
        trt=disdata[3*i+1]
        plot_compare(trt,np.mean(trt),np.std(trt),0,30,5,labels[i])
    plt.title('correctness score')
    plt.xlabel('correctness')
    plt.ylabel('probability')
    plt.legend()
    plt.show()
    
    for i in range(3):
        print (np.mean(disdata[i*3]),np.std(disdata[i*3]))
        print (np.mean(disdata[i*3+1]))
        
from matplotlib import pyplot as plt

def plot_compare(data,mean,std,minval,maxval,inter,text):
    x = np.arange(minval, maxval,inter)
    y = normfun(x, mean, std)
    plt.plot(x,y,linewidth = 2,label=text)
    
def plot_dist(data,mean,std,minval,maxval,inter,xlabel,ylabel,title):
# x的范围为60-150，以1为单位,需x根据范围调试
    x = np.arange(minval-2*inter, maxval+2*inter,inter)
# x数对应的概率密度
    y = normfun(x, mean, std)
# 参数,颜色，线宽
    plt.plot(x,y, color='g',linewidth = 3)
#数据，数组，颜色，颜色深浅，组宽，显示频率
    plt.hist(data, bins =17, color = 'r',alpha=0.5,rwidth= 0.9, normed=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
#plot_iter_time("3nn_errdata.csv")
    
plot_diagram("rodata.csv")




















