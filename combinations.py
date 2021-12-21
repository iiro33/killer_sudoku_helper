from itertools import combinations

numbers = list(range(10))
numbers.pop(0)

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def get_results(to_sum, elements_n, numbers=numbers, exclude=[]):
    results = []
    if len(exclude) == 0:
        combs = list(combinations(numbers, elements_n))
        for element in combs:
            if sum(element) == to_sum:
                results.append(element)
    else:
        elements_n = elements_n - len(exclude)
        to_sum = to_sum - sum(exclude)
        numbers = [i for i in numbers if i not in exclude]
        combs = list(combinations(numbers, elements_n))
        for element in combs:
            if sum(element) == to_sum:
                results.append(element)
    if len(results) == 0:
        print("No combinations found for sum: (" + str(to_sum) + ") with cells: (" + str(elements_n) + ")")
    else:
        print("Combinations for sum: (" + str(to_sum) + ") with cells: (" + str(elements_n) + ")")
        for i in results:
            print(i)

while True:
    to_sum = input("What is the sum of cells? (non integer to exit) ")
    if not represents_int(to_sum):
        break
    else:
        to_sum = int(to_sum)
        elements_n = int(input("How many cells? "))
        exclude = input("Numbers to exclude: (separate with ','; empty = none) ")
        if len(exclude) > 0:
            exclude = [int(i) for i in list(exclude.replace(",", ""))]
        else:
            exclude = []

    get_results(to_sum, elements_n, exclude=exclude)
    print("")

print("byebye")