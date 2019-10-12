err = []
i1 = 0
while i1 < 15:
    i1 += 5
    for p in range(0, 1):
        p=int(input("Введите число: "))
        p += 5
        err.append(p)
        for i in range(0, 1):
            i = input()
            err.append(i)
            print(err, p, i)

from test import Person
p1 = Person()
p1.setname("Bill", "Ross")
p1.name, p1.surname
