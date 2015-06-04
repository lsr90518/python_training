def yes():
    while True:
        yield "y"

y = yes()
print(y.next())
print(y.next())


def countup(start, step):
    while True:
        yield start
        start += step


count = countup(1,2)
print(count.next());
print(count.next());


def loop(end, num):
    yield from (n for _ in range(num) for n in range(end))


l = loop(3,2)
print(l.next())
