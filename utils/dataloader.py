"""
dataloader.py
Classes: Dataloader
Purpose: Provides the utilities needed to load data into nodes and edges from CSV files.
"""
import csv
import random
from structs.node import Node
from structs.edge import Edge

class Dataloader:

    # __init__
    # Constructor - instantiates an object of Dataloader given the path to the file.
    # Params: locFile (string), edgeFile (string)
    def __init__(self, locFile: str, edgeFile: str, speed: float = 0.0):
        try:
            self.__locFile = open(locFile, 'r')
            self.__edgeFile = open(edgeFile, 'r')
        except:
            raise Exception("File not found...")

        self.nodeList = []
        self.nodeDict = {}
        self.edgeList = []
        self.speed = speed

        random.seed(0)
        self.__readCSV()


    # readCSV (Private)
    # Reads the CSV files and constructs the node list and the edge list.
    # Will print out invalid locations and edges.
    # NOTE: will output on invalid lines of the input.
    def __readCSV(self):
        with self.__locFile as locCSV:
            reader = csv.reader(locCSV, delimiter=',')
            for row in reader:
                try:
                    lat = float(row[1])
                    lon = float(row[2])
                    pref = float(random.uniform(0,1))
                    self.nodeList.append(Node(row[0], lat, lon, pref))
                    self.nodeDict.update({row[0]: Node(row[0], lat, lon, pref)})
                except:
                    print("Not a valid location: " + row[0])

        with self.__edgeFile as edgeCSV:
            reader = csv.reader(edgeCSV, delimiter=',')
            for row in reader:
                try:
                    dist = float(row[3])
                    pref = random.uniform(0,0.1)
                    self.edgeList.append(Edge(row[0], self.nodeDict[row[1]], self.nodeDict[row[2]], dist, float(pref), self.speed))
                except:
                    print("One or more locations are invalid: " + row[1] + " " + row[2])