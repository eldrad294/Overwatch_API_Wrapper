def get_dic_obj(dictionary, first, second=None):
    if first in dictionary:
        return dictionary[first]
    elif second in dictionary and second is not None:
        return dictionary[second]
    #
    return None