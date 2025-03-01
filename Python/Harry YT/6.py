#set
l = [1,2,3,4]
s_from_list= set(l)
print(s_from_list)
print(type(s_from_list))

s = set()
print(type(s))
s.add(1)
s.add(2)
s1 = s.union({1,2,3})
print(s, s1)
s1 = s.intersection({1,2,3})
print(s, s1)
s1 = {4,6}
print(s.isdisjoint(s1))

