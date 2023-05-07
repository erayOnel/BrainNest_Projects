# 1. Given two sets A and B, write a function to return the symmetric difference between them as a new set.
# The symmetric difference is the set of elements that are in either A or B,
# but not in both.

# def sym_diff(A, B):
#     return (A - B) | (B - A)


# 2. Given a list of numbers, write a function to return a set of all prime numbers from the list.

# def find_primes(numbers):
#     f_list = set()
#     for num in numbers:
#         if num < 2:
#             continue
#         for q in range(2, int(num ** 0.5) + 1):
#             if num % q == 0:
#                 break
#         else:
#             f_list.add(num)
#     return f_list


# 3. Given a list of words, write a function to return a set of all anagrams in the list.

# def find_anagrams(words_list):
#     f_set = set()
#     s_set = {}
#     for word in words_list:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in s_set:
#             s_set[sorted_word].append(word)
#         else:
#             s_set[sorted_word] = [word]
#     for sorted_word in s_set:
#         if len(s_set[sorted_word]) > 1:
#             f_set.update(s_set[sorted_word])
#     return f_set


# 4. Given a list of sets, write a function to return the Cartesian product of all sets in the list.

# def cartesian_product(sets):
#     if not sets:
#         return []
#     result = [[]]
#     for s in sets:
#         out_res = []
#         for x in result:
#             for y in s:
#                 out_res.append(x + [y])
#         result = out_res
#     return result
