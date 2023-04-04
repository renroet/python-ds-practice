def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_phrase = []
    for char in phrase:
        if char.upper() == to_swap.upper():
            char = char.swapcase()
        flipped_phrase.append(char)
    
    return ''.join(flipped_phrase)



    

