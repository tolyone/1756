import B
import dir2.dir1

x = 6


def foo(x):
    y = x*x
    return y


res = foo(x)

print(res)

B.bar()
res = foo(x)
print(res)