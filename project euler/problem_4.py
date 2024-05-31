def MaxPalindromes(start=100, end=1000):
    """
    Finding Maximum Palindrome from specific range

    Args:
    start (int) : lower boundary
    end (int) : upper boundary

    """

    # empty list
    palindromes = []

    # finding palinderomes in range and appending it to list
    for i in range(start,end):
        for j in range(start,end):
            if str(i*j) == str(i*j)[::-1]:
                palindromes.append(i*j)

    # returning max value of it
    return max(palindromes)

MaxPalindromes()
    




#%%
