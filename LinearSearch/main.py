def linear_search(l, data):
    for i in range(len(l)):
        if l[i] == data:
            return i
    return None

if __name__ == "__main__":
    lis = [1,7,8,60,45,5,896,8,62,9,5,28,6,88]
    res = linear_search(lis,int(input('Data to find: ')))
    if res!=None:
        print('Data find at: %d'%(res))
    else:
        print('Data not find')


