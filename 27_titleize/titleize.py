def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.split()
    new_phrase = []

    for word in phrase:
        new_phrase.append(word.capitalize())
    
    new_phrase = ' '.join(new_phrase)

    return new_phrase
