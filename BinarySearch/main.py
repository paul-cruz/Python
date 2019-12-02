def binary_search(l,data):
    ri, li= len(l)-1, 0
    while li<=ri:
        medium=(li+ri)//2
        if(l[medium]==data):
            return medium
        elif(data>l[medium]):
            li=medium+1
        else:
            ri=medium-1
    return None

if __name__ == "__main__":
    lis=[21,7,9,8,100,5,10]
    res = binary_search(sorted(lis),int(input('Data to find: ')))

    if res!=None:
        print('Data find at: %d'%(res))
    else:
        print('Data not find')