
import listTools


def longest_run(lst : list[int]):
    """Gives you the lenght of the longest run in a list of numbers. A run is a seqeuence of consecutive identical elements

    Args:
        lst (list): The list containing the numbers

    Returns:
        int: Lenght of the longest run
    """
    if len(lst) < 2:
        return len(lst)
    #Make a first comparison and set its result as the start value
    #By default the value of the longest run is one

    longest = (lst[1] == lst[0])*1 + 1
    run = longest
    for i in range(len(lst))[2:]:
        #Check if the next element is the same if it is we increment the run count by one
        if lst[i] == lst[i-1]:
            run += 1
        else:
            #If the next element is different we set the longest run as themax between it and the current one
            longest = max(longest, run)
            #And we reset the run
            run = 1
    return max(longest, run)
    


print(longest_run(listTools.listinput(listTools.int_verifier)))