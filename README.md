# CS4260-assignment-2
Assignment 2 for CS 4260 Fall 2023

Contributors: Alex Oh

To run: 
1. Install requirements
2. Change the config file for desired parameters. (An example is provided in the repository).


Comments on this Assignment:
Results were not surprising and worked relatively as expected. Since this anytime search will search paths with higher
preference first, they will typically provide good results starting at the beginning, however this may not be the optimal
result. This can be seen in some of the tests, particularly the first test, where the second found solution was actually
the best solution so far. This is not unreasonable as a path with high preference will be searched first and continued
to be put into the front of the frontier, while the optimal solution may lie with the next path on the frontier. This could
easily happen when the ending of that path significantly impacts the total preference of the path.

There were also some situations in which the program took much longer to run, in particular the third test. This can be 
attributed to the fact that an anytime search keeps branching and does not check for duplicates in its path, since round
trips sometimes require passing through the same node (although their preferences aren't increased in double counting).
It is important to note that all tests did meet the time requirement, as the path would be discarded if it was over the
time limit. Note: a seed is set on the Dataloader class to make the results reproducible. This can be commented out if
different preferences should be generated each time.


Ran on:
Python 3.10.12
pip 22.0.2
