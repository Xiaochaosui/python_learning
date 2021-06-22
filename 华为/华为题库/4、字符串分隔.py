#
while 1:
    s = input()
    try:
        if len(s)<8:
            s1 = s + '0'*(8-len(s))
            print(s1)
        else:
            for i in range(len(s)//8):
                s1 = s[i*8:(i+1)*8]
                print(s1)
            if len(s)%8 !=0:
                s1 = s[(i+1)*8:] + '0' * (8-len(s)%8)
                print(s1)
    except:
        break

# while True:
#     try:
#         s=input()
#         while len(s)>8:
#             print(s[:8])
#             s=s[8:]
#         print(s.ljust(8,"0"))
#     except:
#         break
