class reversetler:

    def __init__(self, _list):
        self._list = _list

    def iterator(self):

        for i in range(len(self._list)-1, -1, -1):
            yield self._list[i]

if __name__ == '__main__':

    iter = reversetler([1,2,3,4,5,6]).iterator()

    for i in iter:
        print(i)

