import listTools

lstInput = listTools.listinput(listTools.int_verifier)

def run_finder(lst):
    '''This function finds if the received list is a run ( a list containing )
       It works by checking if each pair of elements are different
    param:
        lst (list): The list to be checked

    returns:
        bool: True if the list is a run, False otherwise'''

    return listTools.comparePairLst(lst, lambda x, y: x != y)
