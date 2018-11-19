def two_thousand(n):
    for x in range(n):
        yield (-1)**(x+1)


y = [ x for x in two_thousand(7) ]

print(y)