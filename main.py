list = []
while True:
    a = int(input("enter no."))
    b = int(input("enter no."))
    c = int(input("choice"))
    if c == 1:
        m = a - b
        print(m)
    if c == 2:
        m = a + b
        print(m)
    k = (input("enter"))
    aa = m
    if k == "yes":
        list.append(aa)
        continue

if k == "no":
    list.append(aa)
    print(list)
    if o == "riverse":
        for i in range(0,aa):
            print(aa)
            aa = aa - 1
            if aa == 0:
                break


