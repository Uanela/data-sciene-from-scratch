from typing import Counter


def mode(x):
    """returns a list, might more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())

    return [value for value, count in counts.items() if max_count == count]

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index= int(p * len(x))
    return sorted(x)[p_index]

num_friends = [1, 2,3 ,4 ,2, 3, 5, 5 ]

print(mode(num_friends))
print(quantile(num_friends, 0.6), len( num_friends ))
