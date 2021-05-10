# Warmup section

def jumping_on_clouds(c):
    # Write your code here
    clouds = len(c)
    steps = 0
    i = 0
    while i < clouds - 1:
        if i + 2 < (clouds) and c[i + 2] == 0:
            steps += 1
            i += 2
        elif i + 1 < (clouds) and c[i + 1] == 0:
            steps += 1
            i += 1   
    return steps


def repeatedString(s, n):
    # Write your code here
    # first count the occurence of 'a' in the substring
    alphas = 0
    for c in s:
        if c == 'a':
            alphas += 1
    # the substring is repeated 'repeats' times in the n chars interval
    repeats = n // len(s)
    alphas = alphas * repeats
    
    parsed_chars = repeats * len(s)
    remaining_chars = n - parsed_chars
    for c in range(0, remaining_chars):
        if s[c] == 'a':
            alphas += 1
    return alphas

# Array section
import sys
def hourglassSum(arr):
    # Write your code here
    # The array will always have dimensions 6 x 6
    # thus the number of possible centroids is 16 -> 16 hourglasses
    rows = len(arr) -1
    cols = len(arr[0]) - 1
    max_sum = -sys.maxsize
    if rows == 5 and cols == 5:
        for row in range(1, rows):
            # parse from left to right
            for col in range(1, cols):
                top_sum = sum(arr[row - 1][col - 1:col + 2])
                bottom_sum = sum(arr[row + 1][col-1:col + 2])
                max_sum = max(max_sum, bottom_sum+top_sum+arr[row][col])
        return max_sum

def rotLeft(a, d):
    # Write your code here
    # this may have O(n*d) complexity
    # since pop the first element of an array may have O(n)  complexity
    n = len(a)
    if n <= d:
        # the same array occurs
        return a
    else:
        for i in range(d):
            popped = a.pop(0)
            a.append(popped)
    return a

def rotLeft2(a, d):
    n = len(a)
    if n <= d:
        # the same array occurs
        return a
    else:
        # reverse the list 
        a_rot = a[d:] # we sacrifice O(n) memory
        a.reverse() # O(n)
        for i in range(d): # O(d)
            popped = a.pop()
            a_rot.append(popped)
    return a_rot  

def minimumBribes(q):
    # Write your code here
    len_q = len(q)
    bribes = 0
    cut_liners = 0
    if len_q > 0:
        for j in range(len_q):
            jumps = q[j] - j 
            if jumps - 1 > 2:
                print("Too chaotic")
                return
            # count how many bribed the person in position j
            for i in range(0, j):
                if q[j] < q[i]:
                    bribes += 1
        print(bribes)

def minimumSwaps(arr):
    min_swaps = 0
    for i, v in enumerate(arr):
        if i == v - 1:
            continue
        else:
            arr[v - 1], arr[i] = v, arr[v - 1]
            min_swaps += 1
    print(arr)
    return min_swaps
    
# This solution timed out    
def arrayManipulation(n, queries):
    # number of queries
    n_queries = len(queries)
    max_element = 0
    my_arr = (n + 1) * [0]
    # for each query (operation)
    for query in queries:
        my_arr[query[0] - 1: query[1] + 1] = map(lambda x: x + query[2], my_arr[query[0]:query[1] + 1]) 
    max_element = max(my_arr) 
    return max_element
        

def arrayManipulation(n, queries):
    # number of queries
    n_queries = len(queries)
    max_element = 0
    sum_so_far = 0
    my_arr = (n + 1) * [0]
    # for each query (operation)
    for query in queries:
        # Since in the specified intervals 
        # the values are the same we keep only the bounds
        my_arr[query[0] - 1] += query[2]
        my_arr[query[1]] -= query[2]
        
    for e in my_arr:
        sum_so_far += e
        max_element = max(max_element, sum_so_far)
    return max_element
#---------------  Testing -----------------
# Warm up
steps = jumping_on_clouds([0,0,1,0,0,1,0])
print(steps)
alphas = repeatedString('aba', 10)
print(alphas)

# Array Section
arr = [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]

max_sum = hourglassSum(arr)
print(max_sum)

# a = [1, 2, 3, 4, 5]
# a = rotLeft(a, 4)
# print(a)

a_2 = [1, 2, 3, 4, 5]
a_2 = rotLeft2(a_2, 4)
print(a_2)

q = [2, 1, 5, 3, 4]
minimumBribes(q)

q = [2, 5, 1, 3, 4]
minimumBribes(q)

q = [1, 2, 5, 3, 4, 7, 8, 6]
minimumBribes(q)

q = [5, 1, 2, 3, 7, 8, 6, 4]
minimumBribes(q)

q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)

arr = [4, 3, 1, 2]
min_swaps = minimumSwaps(arr)
print(min_swaps)