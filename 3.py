def remove_dups(_list):
    
    without_dups = []

    for e in _list:

        if e not in without_dups:
            without_dups.append(e)
        
    return without_dups[::-1]    
        



if __name__ == '__main__':

    _list = [12,23,35,24,88,120,155,88,120,155]
    print(remove_dups(_list))
