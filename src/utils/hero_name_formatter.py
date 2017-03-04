def hero_name_formatter(hero_name):
    """ Uppercase first letter fo hero name, and lowercases the rest """
    hero_name = str(hero_name)
    first_letter = hero_name[0].upper()
    remainder = hero_name[1:].lower()
    #
    return first_letter + remainder