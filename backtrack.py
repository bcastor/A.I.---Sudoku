'''
COURSE:        CS-550 Artificial Intelligence
SECTION:       01-MW 4:00-5:15pm
DATE:          15 April 2020
ASSIGNMENT:    05
@author Mariano Hernandez & Brandon Castor
DESCRIPTION:
    Backtrack
'''

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """"BACKTRACKING_SEARCH(
        CSP, SELECT_UNASSIGNED_VARIABLE, ORDER_DOMAIN_VALUES, INFERENCE)
    Solves particular CSP using backtrack search
    Arguments:
        csp -- a constraint satisfaction problem
        select_unassigned_variable -- function handle for selecting variables
        order_domain_values -- function handle for selecting elements of a domain
        inference -- set of inferences
    """
    
    # Title: function BACKTRACK(assignment,csp)
    # Author: Russell, Stuart and Peter Norvig
    # Date: 2010
    # Code Version: N/A Pseudocode
    # Availability: Artificial Intelligence: A Modern Approach, 3rd ed.,
    #               Chapter 6, Figure 6.5
    def backtrack(assignment):
        """BACKTRACK(ASSIGNMENT)
        # function BACKTRACK(assignment,csp) returns a solution, or failure
        Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        Arguments:
            assignment -- current assignment
        """
        
        # if assignment is complete then return assignment
        if len(assignment) == len(csp.variables): return assignment    # TODO understand what this  does
        
        # var ← SELECT-UNASSIGNED-VARIABLE(csp)
        var = select_unassigned_variable(assignment, csp)
        # for each value in ORDER-DOMAIN-VALUES(var,assignment,csp) do
        for value in order_domain_values(var, assignment, csp):
            
            # if value is consistent with assignment then
            if csp.nconflicts(var, value, assignment) == 0:
                # add {var = value} to assignment
                csp.assign(var, value, assignment)
                # inferences ←INFERENCE(csp,var,value)
                removals = csp.suppose(var, value)  # TODO understand what suppose does
                inferences = inference(csp, var, value, assignment, removals)
                
                # if inferences != failure then    # TODO understand what inferences are
                if inferences:
                    # add inferences to assignment
                    # result ← BACKTRACK(assignment, csp)
                    result = backtrack(assignment)
                    
                    # if result != failure then
                    if result is not None:
                        # return result
                        return result
                    
                # remove {var = value} and inferences from assignment
                csp.restore(removals)
                csp.unassign(var, assignment)
        # return failure
        return None
    
    
    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result


