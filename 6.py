def divisible_generator(n):
    for i in range(n):
        if i % 5 == 0 and i % 7 == 0:
            yield i

if __name__ == '__main__':
    n =  int(input("Enter number of values to check: "))
    result = (divisible_generator(n))
    for res in result:
        print(res,end = ",")
        

