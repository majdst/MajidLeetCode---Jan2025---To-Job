From www.codewars.com:

Complete the method so that it'll find the greatest product of five consecutive digits in the given string of digits.



For example: the greatest product of five consecutive digits in the string "123834539327238239583" is 3240.



The input string always has more than five digits.



Adapted from Project Euler.



\## Approach 1: Naive O(n.k)



The first version of the code uses a nested loop. For every window of size 'k', it recomputes the product from scratch. This means the complexity is O(n.k). For small strings this is fine, but if the string is large (say 100k) and 'k' is also large, the runtime becomes too slow. This inefficiency comes from re-multiplying overlapping again and again.



Approach 2: Sliding O(n)



The improved version avoids recomputing the full product each time. It uses a sliding window, multiplying by the new digit and dividing by the old digit when possinle. Zeros reset the product window. This reduces complexity to O(n)

