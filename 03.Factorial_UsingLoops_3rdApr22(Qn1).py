# code for Ratio of  two factoerial
def facto(n):
    f =1 
    for i in range(1,n):
       f = f*i
    i+=1
    return f 

if __name__ == '__main__':
    n = int(input())
    m = int(input())
  
print(facto(n)//facto(m))
