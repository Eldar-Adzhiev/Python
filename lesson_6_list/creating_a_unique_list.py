import random

u_list = []
d_list = []

for i in range(100):

    dd = random.randint(0, 100)

    d_list.append(dd)

    if dd in u_list:
        continue
    else:
        u_list.append(dd)

print('d_list =', d_list)
print('u_list =', u_list)