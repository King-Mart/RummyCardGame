
'''
listTools.py

Author: Martin K. Dongmo

The purpose of this module is to regroup a set of small tools I can us to facilitate the development of future applications
'''

def listinput(verificator , sep=" "):
    """
    Returns a list of elements inputed by a user. Each element transformed by a verificator
    The verificator function should take a string as an argument and return a value of the type
    that the user desires. If the verificator raises a ValueError when given a string, the program
    will ask the user for input again until the verificator does not raise a ValueError.

    The function will keep on asking for valid input as long as the verificator raises a ValueError
    when given a string from the user's input.

    Precondition: The verificator function should take a string as an argument and return a value
                  of any type that the user desires. The verificator should raise a ValueError when
                  given a string that is not a valid input for the type that the user desires.
    """
    bad_input_error = True

    while bad_input_error:
        raw_input = input("Please input a list of numbers separated by space : \n").strip().split(sep)
        try:
            raw_input = [verificator(i) for i in raw_input]
            bad_input_error = False
            return raw_input
        except ValueError:
            print("Invalid input. Please input numbers separated by spaces.")

def int_verifier(input):

    
    """
    Converts an  input into an integer. Raises a value error if impossible.



    Param:
        input: The input to convert into an integer.

    Returns:
        int: The integer converted from the given input.

    Raises:
        ValueError: If the given input cannot be converted into an integer.
    """

    
    return int(input)

def is_bigger(n1, n2):
    """
    Returns True if n1 is bigger than n2, False otherwise.

    Param:
        n1 (int): The first number to compare.
        n2 (int): The second number to compare.

    Returns:
        bool: True if n1 > n2, False otherwise.
    """
    return n1 > n2

def is_smaller(n1, n2):
    """
    Returns True if n1 is smaller than n2, False otherwise.

    Param:
        n1 (int): The first number to compare.
        n2 (int): The second number to compare.

    Returns:
        bool: True if n1 < n2, False otherwise.
    """
    return not is_bigger(n1, n2)


def comparePairLst(lst : list, func ):
    
    """
    Outputs wether or not a given comparison function gives a constant result when applied
    to consecutive pairs of elements in a list.

    Param:
        lst (list): The list of elements to be compared.
        function (callable): A function that takes two arguments and returns a boolean value
                             indicating their relationship.

    Returns:
        bool: True if the result of the comparison function is the same for all consecutive
              pairs in the list, False otherwise.
    """
    
    if len(lst) < 2:
        return True
    #Make a first comparison and set its result as the standard
    const = func(lst[1], lst[0])
    for i in range(len(lst))[2:]:
        if not func(lst[i], lst[i-1]) == const :
            return False
    return True