def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    trunc_lst = list(range(n))
    dif = n - 3
    if len(phrase) >= n:
        for x in range(dif):
            trunc_lst[x] = phrase[x]
        trunc_lst[-3::] = ['.'] * 3
        new_phrase = ''.join(trunc_lst)
        return new_phrase
    else:
        return phrase
   
        
            
            
    #     trunc_phrase = new_phrase[:-3:] + '...'
    #     return trunc_phrase
    # else
    