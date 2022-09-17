

def gen_def():
    for i in [43, 65, 32]:
        yield i

s = gen_def()
# print(s)
# print(next(s))
# print(next(s))
# print(next(s))

for i in s:
    print(i)