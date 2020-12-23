def binary_search(_list, element):
    low = 0
    high = len(_list) - 1
    mid = 0

    while low <= high:

        mid = (low + high) // 2

        if _list[mid] < element :
             low = mid + 1

        elif _list[mid] > element:
            high = mid -1
        
        else:
            return mid

    return -1 # if element not present in list

if __name__ == '__main__':
    _list = [1,5,8,23,54,77,86,123]
    element = 23
    index = binary_search(_list, element)

    if index != -1:
        print(f"Element at index: {index}")

    else:
        print("Element not found")