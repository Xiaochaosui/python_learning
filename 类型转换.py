# list-->set
l1 = [1,2,3,4]
s1 = set(l1)

# tuple-->set
t1 = (1,2,3,4)
s2 = set(t1)

# set-->list
s3 = {1,2,3,4}
print(type(s3))
l3 = list(s3)
print(l3)

# set-->tuple
t4 = tuple(s3)
print(t4)
