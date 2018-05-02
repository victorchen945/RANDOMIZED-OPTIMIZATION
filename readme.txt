The code is implemented in jython, 
the packages and environment need to run the code:
jdk 1.8.0/jre1.8.0
jython 2.7.0
python 2.7.0
matplotlib
numpy
pandas
ABAGAIL package from https://github.com/pushkar/ABAGAIL

The folders structure and files:
-bin: default package
-docs: defualt package
-jython: from default package, contains my edited code
 -continuouspeaks.py   problem1 continuouspeaks
 -travelingsalesman.py problem2 tsp
 -knapsack.py          problem3 knapsack
 -3nn                  part1 finding nn weight
 -PLOTTER_3nn.py       plot graphs for part1 nn weight finding
 -PLOTTER_problems.py  plot graphs for part2 randomized problems
-src: default package£¬with dataset in
  -opt
   -test
    -student.txt <--this is dataset
-outputs:
  -data: output data in csv files
  -graph: ploted graph via matplotlib.pyplot
-zchen612_analysis.pdf  analysis report

to run the code:
run continuouspeaks.py,travelingsalesman.py,knapsack.py,3nn.py in jython, they will generate csv datafiles
then run PLOTTER_3nn.py ,PLOTTER_problems.py to plot graphs