#########################################################################
"""
Title: Utility.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
A file for general utility in the contexte of low information protocol of AND

"""
########################################################################

# Allow to clearly see the result of the job
def ShowResults(job):
    results = list(job.result().get_counts().items())

    if not results:
        print("\n********************************************\n\nthere is no solution\n\n********************************************")
    else:
        print("\n********************************************\n\nthe solution is: ", results[0][0], "\n\n********************************************")
