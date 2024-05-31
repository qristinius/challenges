def PowSum(num,power):
    """
    Powering the number and summing up each digits of result number

    Args:
        num (int) : number that should get powered
        power (int) : power of number
    """

    print(f'The sum of powered number digits is: {sum([int(digit) for digit in str(num**power)])}')

PowSum(2,1000)
#%%
