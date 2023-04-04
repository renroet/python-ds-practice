def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = f'{num1}'
    num2 = f'{num2}'
    ind_num1 = set(num1)
    ind_num2 = set(num2)
    count1 = {x: num1.count(x) for x in ind_num1}
    count2 = {x: num2.count(x) for x in ind_num2}
    return count1 == count2

    

