# 4.4 Нахождение всех делителей числа

# Первый вариант

# n = int(input())
# i=1
# while i <=n:
#     if n%i ==0:
#         print(i, end=" ")
#     i +=1


# Вариант в два раза быстрее

# n = int(input())
# i=1
# while i <=n//2:
#     if n%i ==0:
#         print(i, end=" ")
#     i +=1
# print(n)

# Вариант 3

# n = int(input())
# i=1
# while i <=n**0.5:
#     if n%i==0:
#         if i ==n//i:
#             print(i, n//i)
#         else:
#             print(i,n//i)
#
#     i +=1





abc = 'abcdefghijklmnopqrstuvwxyz'

list = []

for i in range(1,len(abc)+1):
    print(i)
    list.append(abc[i-1]*i)
print(list)








