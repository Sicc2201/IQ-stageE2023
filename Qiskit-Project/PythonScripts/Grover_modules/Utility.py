#########################################################################
"""
Title: Utility.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 11/08/23

"""
#########################################################################
""""
This file contains various utility functions Grover specific

Functions:

- CheckPower2(a)

- CheckCalendars(a, b)

- ShowResults(job, threshold)

"""
########################################################################

# imports
from math import floor, ceil, log2

# check if a number is a power of 2
def CheckPower2(a):
    return ceil(log2(a)) == floor(log2(a))

# Ensures that two participants has a valid calendar
def CheckCalendars(a, b):

    # check if calendars are the same size (not relevant anymore)
    if len(a) != len(b):
        raise Exception("the two calendar must be the same size")
    # check if calendars lenghts are a power of 2 (not relevant anymore)
    if not CheckPower2(len(a)):
        raise Exception("the two calendar's length must be a power of 2")
    if not CheckPower2(len(b)):
        raise Exception("the two calendar's length must be a power of 2")
    # check if both calendar are of lenght 4
    if len(a) != 4 or len(b) != 4:
        raise Exception("Calendars must be of length 4")
    print("calendars ok")
    return True

# Allow to clearly see the result of the job
def ShowResults(job, threshold=int(1024/3)):
    results = list(job.result().get_counts().items())
    best_results = []

    # result only consider elements over a certain threshold (not relevent for calendar of lenght 4)
    for r in results:
        # if value of result higher than the threshold, add it to best_results
        if r[1] >= threshold:
            best_results.append(r[0])
    results = []

    # for results over the threshold, convert binary to decimal
    for i in best_results:
        results.append(int(str(i), 2))

    if not results:
        print("\n********************************************\n\nthere are no solutions for these calendars\n\n********************************************")
    elif len(results) == 1:
        print("\n********************************************\n\nthe solution is position: ", results[0], "\n\n********************************************")
    else:
        print("\n********************************************\n\nthere are", len(results),"solutions: ", results, "\n\n********************************************")
