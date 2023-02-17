from collections import Counter

def task_1(str):
    freq = {}

    for char in str:
        if char.isalpha():
            char = char.lower()
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    print(freq)
    return freq


def task_2(list):
    counter = Counter(list)

    unique_elements = counter.keys()

    total = sum(unique_elements)
    print(total)
    return total


def task_3(cities):
    result = ", ".join(cities) + "."

    print(result)
    return result


def task_4(a, b):
    set1 = set(a)
    set2 = set(b)

    intersection = list(set1 & set2)
    print(intersection)
    return intersection
