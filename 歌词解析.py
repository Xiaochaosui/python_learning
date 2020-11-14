import time
musicLrc = """[00:03.50]《东边的山坡上有两头牛》
[00:10.10]作词：pange 作曲：pange
[00:11.60]演唱：xcs
[00:13.60]
[04:40.75][02:39.90][00:16.25]东边的山坡上有两头牛
[04:49.00]
[02:47.44][00:19.69]公牛对母牛说 I love you
[02:54.83][00:22.24]母牛对公牛说你羞不羞
[03:02.32][00:25.75]公牛说不羞不羞 I love you
[03:08.15][01:04.30]
[03:09.35][0:28.50]See it started at the park
"""
lrcDict = {}
lrcLineList = musicLrc.splitlines()
#print(lrcLineList)
for lrcLine in lrcLineList:
    #print(lrcLine)
    lrcList = lrcLine.strip(" ").split("]")
    #print(lrcList)
    #print(len(lrcList))
    for i in lrcList[:-1]:
        allTimeList = i.strip("[").split(":")
        #print(allTimeList)
        time1 = float(allTimeList[0])*60 + float(allTimeList[1])
        #print(time1)
        lrcDict[time1] = lrcList[-1]
#print(lrcDict)
timeList = list(lrcDict)
timeList.sort()
#print(timeList)


# 输入时间找到对应歌词
'''while 1:
    getTime = float(input("TIME:"))
    for n in range(len(timeList)):
        temp = timeList[n]
        if getTime < temp:
            break
    if n==0:
        print("Time is too short!")
    else:
        print(lrcDict.get(timeList[n - 1]))'''

# 按时间输出歌词
for k in range(len(timeList)):
    if k == 0:
        time.sleep(timeList[k])
    else:
        time.sleep(timeList[k]-timeList[k-1])
    print(lrcDict.get(timeList[k]))