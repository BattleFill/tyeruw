
def summirovanie():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("in list a: ", a)
    return sum(a)
def socrat():
    a = [1, 43, 43, 1, 23, 6, 1, 99, 6, 11]
    print("in list a: ", a)
    for x in a:
        if a.count(x) > 1:
            a.remove(x)
    print("bez povtorov ")
    return a
def rt():
    a = ['a', "b", "c", "d", "e", "f", "g", "h", "i", "y"]
    print(('in list'),a)
    s = input('Chto iskat?')
    pos = a.index(s)
    print('on position')
    return pos
def we():
    a = [('e', 'f'), ('s, f'), ('re','hp') ,('sdf', 'er')]
    print('in kortehe', a)
    del a [1]
    return a
while True:
    print("\nChoose an action")
    print("1.")
    print("2.")
    print("3.")
    print("4.")
    print("5.")
    print("6.")
    print("7.")
    print("8.")
    vibor = int(input("What will be your choice?: "))
    if vibor == 1:
        g = summirovanie()
        print(g)
    elif vibor == 2:
        a = [1, 43, 3, 4, 23, 6, 7, 99, 9, 10]
        print("in list a: ", a)
        print("max = ", max(a))
    elif vibor == 3:
        g = socrat()
        print(g)
    elif vibor == 4:
        a = [1, 43, 43, 1, 23]
        print("in list a: ", a)
        b = [6, 1, 99, 6, 11]
        print("in list b: ", b)
        c = a + b
        print("vmeste: ", c)
    elif vibor == 5:
        g = rt()
        print(g)
    elif vibor == 6:
        a = (21, 47, 4, 66, 2, 4)
        print(('V pervom kartehe'),a)
        b = (22, 4, 65,  34, 23, 34)
        print(('vo vtorom'),a)        
        c = a + b 
        print(('vmeste: '),c)
    elif vibor == 7:
        g = we()
        print(g)
    elif vibor == 8:
        a = ['16', '48', '32', '48', '10', '24', '32', '10', '48', '32', '24', '10', '48', '32', '48', '10', '32', '10', '48', '16', '48', '32', '48', '10', '56'] 
        print(('in kortehe'),a)
        ser = input('chto iskat? ')
        print(a.count(ser))
    else:
        break