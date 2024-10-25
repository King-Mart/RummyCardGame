import listTools
bad_input_error = True

while bad_input_error:
    raw_input = listTools.listinput(listTools.int_verifier)
    denominator = input("Enter the number for which you want to verify the list's divisibility \n")
    try:
        denominator = int(denominator)
        bad_input_error = False
    except ValueError:
        print("Invalid input. Please input a number.")

def number_divisible(lst : list[int], denominator :int) -> int:
    '''
    Returns the number of numbers in the list that are divisible by the given denominator

    param:
        lst (list): The list of numbers to be compared.
        denominator (int): The number to be used for comparison.

    Returns:
        int: The number of numbers in the list that are divisible by the given denominator
    
    >>> number_divisible([1,2,3,4,5],2)
    2
    >>> number_divisible([1,2,3,4,5],3)
    1
    >>> number_divisible([1,2,3,4,5],10)
    0
    '''

    return sum(1 if x % denominator == 0 else 0 for x in lst)


print(f"The number of numbers divisible by {denominator} in the list you've inputed is {number_divisible(raw_input, denominator)}")



