vmap = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}

x = input("Enter a string: ")
for i in range(len(x)):
    if x[i] in vmap:
        vmap[x[i]] += 1

for i in vmap:
    print(f"{i}: {vmap[i]}")
