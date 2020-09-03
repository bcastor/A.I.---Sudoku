'''
COURSE:        CS-550 Artificial Intelligence
SECTION:       01-MW 4:00-5:15pm
DATE:          15 April 2020
ASSIGNMENT:    05
@author Mariano Hernandez & Brandon Castor
DESCRIPTION:
    Constraint propagation
'''

# Title: function AC-3(csp) w/ nested function REVISE(csp, Xi, Xj)
# Author: Russell, Stuart and Peter Norvig
# Date: 2010
# Code Version: N/A Pseudocode
# Availability: Artificial Intelligence: A Modern Approach, 3rd ed.,
#               Chapter 6, Figure 6.3
def AC3(csp, queue=None, removals=None):
    """"AC3(CSP, QUEUE, REMOVALS)
    returns false if an inconsistency is found and true otherwise
    Arguments:
            csp -- a binary CSP with components (X, D, C)
            queue -- a queue of arcs, initially all the arcs in csp
            removals -- list of ruled out var=value
    """
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x
    # local variable:
    if queue is None:
        queue = [(X_i, X_j) for X_i in csp.variables for X_j in csp.neighbors[X_i]]
    
    
    # function REVISE(csp, X_i, X_j)
    def revise(csp, X_i, X_j):
        """"REVISE(CSP, X_i, X_j)
        returns true iff we revise the domain of Xi
        """
        # revised ← false
        revised = False
        
        # for each x in D_i do
        D_i = csp.curr_domains[X_i]
        for x in D_i:
            D_j = csp.curr_domains[X_j]
            # if no value y in D_j allows (x,y) to satisfy
            # the constraint between Xi and X_j then 
            if not any([csp.constraints(X_i, x, X_j, y) for y in D_j]):
                # delete x from D_i
                csp.prune(X_i, x, removals)
                # revised ← true
                return revised
                
        # return revised
        return revised
    
    
    # while queue is not empty do
    while queue:
        # (X_i, X_j) ← REMOVE-FIRST(queue)
        (X_i, X_j) = queue.pop()
        
        # if REVISE(csp, Xi, Xj) then
        if revise(csp, X_i, X_j):
            D_i = csp.domains[X_i]
            # if size of Di = 0 then return false
            if D_i is None: return False
            
            # for each X_k in X_i.NEIGHBORS - {X_j} do
            for X_k in csp.neighbors[X_i]:
                # add (Xk, Xi) to queue
                queue.append((X_k, X_i))
            
    # return true
    return True


