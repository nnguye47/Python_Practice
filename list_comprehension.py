example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [num for num in example if num % 2 == 0]
print(evens)

odds = [number for number in example if number % 2 == 1]
print(odds)


example_2 = [True, False, False, True, False, True, False, True]

bits = [1 if bool == True else 0 for bool in example_2]
print(bits)