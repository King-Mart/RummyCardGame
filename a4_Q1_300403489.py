bad_input_error = True

while bad_input_error:
    raw_input = input("Please input a list of numbers separated by space : \n").strip().split(" ")
    try:
        raw_input = [int(i) for i in raw_input]
        bad_input_error = False
    except ValueError:
        print("Invalid input. Please input numbers separated by spaces.")
    denominator = input("Enter the number for which you want to verify the list's divisibility \n")
    try:
        denominator = int(denominator)
        bad_input_error = False
    except ValueError:
        print("Invalid input. Please input a number.")

def number_divisible(lst : list[int], denominator :int):
    divisible_count = 0
    for i in lst:
        if i % denominator == 0:
            divisible_count += 1
    return divisible_count


print(number_divisible(raw_input, denominator))



