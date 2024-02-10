# st = {5, 3, 4, 2, 8, 4, "hello"}
# print(type(st))
# print(st)
# print(st[0])
# st[0] = 100
# print(st)

# st = set([3, 6, 2, 7, 23])
# st = set(3, 6, 2, 7, 23) // error
# print(st)

st = {
    42,
    12.5,
    "hello",
    # [54, 3]   // list if hashable for st
    # {"one": 20, "two": 30} // dict is hashable fot set
    # {3, 5}, // set is hashable for set
    (3, 5, 6) # tuple is not hashable for set
}

# st.update([654, 666, 253])

# print(st)

# for x in st:
#     print(x)

# lst = [3, 6,5,3,3,4,3]
# st = list(set(lst))
# print(st)


# st.add((10, 20))
# st.update([100, 200, 300])
# print(st)

# st = {3, 6, 2, 7}
# x = st.remove(7)
# st.remove(60) # will give error

# st.discard(7)
# x = st.discard(70)
# print(x)
# st.clear()
# st2 = st
# st2.add(10)
# print(st)

# st = {2, 5}
# st2 = {6, 8}

# x = st.union(st2)
# print(x)

str1="abcDf1234caB896h125"
count=0
data = ""
for i in range(len(str1)):
    if ord(str1[i]) >= 48 and ord(str1[i]) <= 57:
        data = data + str1[i]
    else:
        if len(data) == 3:
            print(data)
        data = ""

print(data)



# print(chr(57))
