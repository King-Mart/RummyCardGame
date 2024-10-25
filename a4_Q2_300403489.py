import listTools



def run_finder(lst : list[int]):
    """
    Finds if the received list is a run ( a list containing consecutive identical integers)
    
    Args:
        lst (list): The list to be checked

    Returns:
        bool: True if the list is a run, False otherwise
    """
    return listTools.comparePairLst(lst, lambda x, y: x == y)


print(run_finder(listTools.listinput(listTools.int_verifier)))