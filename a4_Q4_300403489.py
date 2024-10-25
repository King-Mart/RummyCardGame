
def read_raw(file):
    '''str->list of str
    Returns a list of strings that was stored in a file.'''
    raw = open(file).read().splitlines()
    # for i in range(len(raw)):
    #     raw[i]=raw[i].strip()
    # return raw
    return [i.strip() for i in raw]
def read_without_stars(file):
    '''str->list of str
    Returns a list of strings that was stored in a file.
    The function removes all the stars from the list.
    Opening this would be a better approach for solving the clean up'''
    with open(file) as to_filter:
        return [i for i in to_filter.read().splitlines() if '*' != i]

def clean_up(lst: list[str]):
    '''list of str->list of str

    The functions takes as input a list of characters.
    It returns a new list containing the same characters as l except that
    one of each characters that appears odd number of times in l is removed
    and all the * characters are removed

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''


    clean_board=[]

    #Sorting the list making sure all the stars are at the end
    lst = sorted(lst, key=lambda x: x if x != '*' else 'ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ')
    i = 0
    while i < len(lst)-1:
        if lst[i] == '*':
            return clean_board
        if lst[i] == lst[i+1]:
            clean_board += [lst[i], lst[i+1]]
            i += 2
        else:
            i += 1
    
    return clean_board
    


def is_rigorous(lst):
    '''list of str->bool
    Returns True if every character in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: You may assume that every element in the list appears even number of times
    (i.e. that the list is clean-up by clean_up function) Which means it will also be sorted

    >>> is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>> is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    i = 0
    while i < len(lst)-2:
        if lst[i] == lst[i+2]:
            return False
        i += 2
    return True

    
#main
file=input("Enter the name of the file: ")
file=file.strip() 
file = file if file.endswith('.txt') else file + '.txt'
b=read_raw(file)
print("\nBefore clean-up:\n", b)
b=clean_up(b)
print("\nAfter clean-up:\n", b)
if is_rigorous(b):
    print("\nThis list is now rigorous; it has no * and it has "+str(len(b))+" characters.")
else:
    print("\nThis list has no * and is not rigorous and it has "+str(len(b))+" characters.")
     
