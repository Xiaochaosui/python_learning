# 无序数组 返回第K大的元素

# input：  1234
#          4
# output: 1

def max_K(q,i,j):
    key = q[i]
    while i<j:
        while i<j and q[j] > key:
            j -=1
        q[i] = q[j]
        while i<j and q[i] < key:
            i +=1
        q[j] = q[i]
    q[i] = key
    return i,q
def res(q,i,j,k):
        index,q = max_K(q,i,j)
        if index==k:
            return q[k]
        if index<k:
            return res(q,index+1,j,k)
        else:
            return res(q,i,index-1,k)
if __name__ == '__main__':
    a = input().split(" ")
    # for x in a:
    #     x = int(x)
    r = list(map(int,a))
    k = int(input())
    i = 0
    j = len(r)-1
    print(res(r,i,j,k))