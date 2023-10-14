# import re

# def solution(address:str):
#     resulst = re.findall(r'@[A-Za-z0-9|-]+\.[A-Z|a-z]{2,7}\b',address)[0]
#     return resulst[1:]


# print(solution("example-indeed@strange-example.com"))


# def solution(st):
#     reverse = st[::-1]
#     count = 0
#     new_reverse = reverse

#     while True:
#         if new_reverse == new_reverse[::-1]:
#             break
#         new_reverse = st[:count] + reverse
#         count += 1

#     return new_reverse


# print(solution("abcdc") == "abcdcba")


# def solution(votes, k):
#     max_number = max(votes)

#     return (
#         1
#         if (k == 0 and votes.count(max_number) == 1)
#         else len([x for x in votes if (x + k) > max_number])
#     )


# print(solution([5, 1, 3, 4, 1], 0))

# import re

# def solution(inputString):
#     return bool(re.match(r"[0-9A-F]{2}(?:-[0-9A-F]{2}){5}$",inputString))


# print(solution("02-03-04-05-06-07-"))

# from collections import Counter


# def solution(s):
#     count = 0
#     string_count = len(s)
#     end_count = 1
#     new_string = ""

#     while True:
#         if end_count == string_count:
#             if end_count - count == 1:
#                 new_string += s[count]
#             else:
#                 new_string += f"{end_count - count}{s[count]}"
#             break

#         if s[count] != s[end_count]:
#             new_string += f"{'' if (end_count - count) <= 1 else (end_count - count)}{s[count]}"
#             count = end_count

#         end_count += 1

#     return new_string


# print(solution("wwwwwwwawwwwwww"))


# def solution(n):
#     new_n = str(n)
#     len_n = len(new_n)

#     number = 0
#     count = 0
#     while True:
#         if count >= len_n:
#             break

#         temp = int("".join([x for index, x in enumerate(new_n) if index != count]))
#         if temp > number:
#             number = temp
#         count += 1
#     return number

import re

# def solution(text):
#     return max(re.split('[^a-zA-Z]', text), key=len)


# print(solution("ABCd"))

# def solution(time):
#     left,right = time.split(":")
    
#     if (left[0] == "1" or left[0] == "0") and left[1] > "9":
#         return False
    
#     elif left[0] == "2" and left[1] >= "4":
#         return False
    
#     if right[0] > "5" or right[1] > "9":
#         return False

#     return 0 <= int(left) < 24 and 0 <= int(right) < 60

# print(solution("13:58"))

# def solution(inputString):
#     return sum(map(int,re.findall("(\d+)",inputString)))


def solution(matrix):

    array = set()
    length_matrix = len(matrix)
    sub_length_matrix = len(matrix[0])
    for i in range(length_matrix):
        if (i+1) < length_matrix:
            for x in range(sub_length_matrix-1):
                array.add((*matrix[i][x:x+2],*matrix[i+1][x:x+2]))
    return len(array)
import math as mt
 
# function to find smallest number k such that
# the product of digits of k is equal to n
def solution(n):
    
    if n == 0:
        return 10
 
    if (n >= 0 and n <= 9):
        return n
     
    digits = list()

    for i in range(9,1, -1):
     
        while (n % i == 0):
            digits.append(i)
            n = n //i
         
    if (n != 1):
        return -1
 
    k = 0
    while (len(digits) != 0):
     
        k = k * 10 + digits[-1]
        digits.pop()
     
    return k

# print(solution(0))


from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_repeat = Counter(nums)
        
        return list(set([x for x in nums if x in list_repeat and list_repeat.get(x) > (len(nums)/3)]))


s = Solution()
print(s.majorityElement([3,2,2,2,3]))
        