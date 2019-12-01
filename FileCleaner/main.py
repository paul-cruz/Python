def clean_file(l):
    for i in range(len(l)):
        if '\n' in l[i]:
            l[i] = l[i][:-1]
        l[i].rstrip()
    l = ''.join(l)
    return l

if __name__ == "__main__":
    f = open('input.txt','r')
    print = open('output.txt','w')
    lis = f.readlines()
    print.write(clean_file(lis)+'\n')
    print.close()