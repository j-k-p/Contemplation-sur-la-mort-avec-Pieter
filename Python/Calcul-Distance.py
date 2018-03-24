#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import math

if __name__ == "__main__":

    filename = "sequence.csv"
    cr = csv.reader(open(filename,"rb"),delimiter = ",")
    x = 3.32
    y = -1.12
    tempvalue = "0"
    for row in cr:
        value = math.sqrt((x - float(row[0]))**2+(y - float(row[1]))**2)
        print tempvalue + " id-r t " + str(int(value*50000)) + ";"
        tempvalue = str(int(value*50000))
        print "0 id-r a " + row[0]+ ";"
        print "0 id-r b " + row[1]+ ";"
	x = float(row[0])
	y = float(row[1])
