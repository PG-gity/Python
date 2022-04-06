# code for Ratio of  two factoerial
def facto(n):
    if(n>0):
        return n*facto(n-1)
    else:
        return 1    


if __name__== '__main__':

    n = int(input())
    m = int(input())
    print((facto(n)/facto(m)))
      