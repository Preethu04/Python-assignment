import pprint

def get_3darray(n1, n2, n3, value): 
    return [[[value for col in range(n1)] for col in range(n2)] for row in range(n3)]


if __name__ == "__main__":
    pprint.pprint(get_3darray(3, 5, 8, 0))