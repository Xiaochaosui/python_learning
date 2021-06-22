#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def threeSum(self , num ):
        # write code here
        b = []
        nLen = len(num)
        num.sort()
        if nLen >=3:
            for k in range(nLen):
                if num[k] > 0:
                    break
                if k >0 and num[k] == num[k-1]:
                    continue
                i = k + 1
                j = nLen - 1
                t = 0-num[k]
                while i < j:
                    if num[i] + num[j] == t:
                        b.append([num[k],num[i],num[j]])
                        while i <j and num[i] == num[i+1]:
                            i += 1
                        while i <j and num[j] == num[j-1]:
                            j -= 1
                        i += 1
                        j -= 1
                    elif num[i] + num[j] > t:
                        j -= 1
                    elif num[i] + num[j] < t:
                        i += 1


        return b