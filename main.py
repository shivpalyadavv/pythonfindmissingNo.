def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(45, n[-1]):
        if i not in numbers:
            output.append(i)
    return output


listOfNumbers = [45,4,47,48,49,51,52,54,56,60,61]
print(findMissingNumbers(listOfNumbers))