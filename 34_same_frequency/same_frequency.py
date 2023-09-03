def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count1 = counter(num1)
    count2 = counter(num2)

    return count1 == count2

def counter(num):

    counts = {}

    for x in str(num):
        counts[x] = counts.get(x, 0) + 1

    return counts