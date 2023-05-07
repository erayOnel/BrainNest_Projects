# f_list = []
# fva = 0
# sva = 0
# while True:
#     f_list.append(fva)
#     f_list.append(sva)
#     fva += 3
#     sva += 5
#     if fva >= 1000 or sva >= 1000:
#         break
# print(sum(sorted(set(f_list))))


# f_list = [1, 2]
# while True:
#     f_list.append(sum(f_list[-2:]))
#     if f_list[-1] > 4000:
#         f_list = f_list[:-1]
#         break
# print([m for m in f_list if m % 2 == 0])


# def check_prime(number):
#     if number == 1:
#         return "Not Prime"
#     elif number == 2:
#         return "Prime"
#     else:
#         for q in range(2, number):
#             if number % q == 0:
#                 return "Not Prime"
#         return "Prime"
# def main_func(value):
#     f_list = []
#     co = 2
#     while not value == 1:
#         if value % co == 0:
#             if check_prime(co) == "Prime":
#                 f_list.append(co)
#             value = value / co
#         co += 1
#     return f_list[-1]
# print(main_func(600851475143))


# fva = 0
# for x in range(993, 99, -1):
#     for y in range(913, 99, -1):
#         pal = str(x * y) == str(x * y)[::-1]
#         if pal and x * y > fva:
#             fva = x * y
# print(fva)


# f_list = []
# s_list = []
# for m in range(1, 101):
#     f_list.append(m ** 2)
#     s_list.append(m)
# print(abs(sum(f_list) - (sum(s_list) ** 2)))


# def check_prime(number):
#     for q in range(2, number):
#         if number % q == 0:
#             return False
#     return True


# f_list = []
# co = 2
# while len(f_list) < 10001:
#     if check_prime(co):
#         f_list.append(co)
#     co += 1
#
# print(f_list[-1])
# # approximately takes 24 to 26 sec to end the process


# for a in range(998, 0, -1):
#     for b in range(1, 1000):
#         c = 1000 - (a + b)
#         if c == 0:
#             break
#         if a**2 + b**2 == c**2:
#             if a**2 < b**2 < c**2:
#                 print(a, b, c)


# def sieve_of_eratosthenes(n):
#     primes = [True] * n
#     primes[0] = primes[1] = False
#     for x in range(2, int(n**0.5)+1):
#         if primes[x]:
#             for j in range(x*x, n, x):
#                 primes[j] = False
#     return [x for x in range(n) if primes[x]]
#
# print(sieve_of_eratosthenes(20))
