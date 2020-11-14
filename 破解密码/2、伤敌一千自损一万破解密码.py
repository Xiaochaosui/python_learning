import itertools

myList = list(itertools.product("0123456789",repeat=4))
#print(myList)
passwd = ("".join(x) for x in itertools.product("0123456789",repeat=10))
while True:
    try:
        str = next(passwd)
        print(str)
    except:
        break
#print(len(myList))
