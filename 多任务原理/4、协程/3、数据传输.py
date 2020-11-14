def run():
    data = ''
    r = yield data
    print(1,r,data)
    r = yield data
    print(2,r,data)
    r = yield data
    print(3,r,data)
    r = yield data


m = run()

print(m.send(None))
print(m.send('a'))
print(m.send('b'))
print(m.send('c'))
print("*"*6)
