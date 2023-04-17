import sys
import collections
# Warmup section
class WarmUp:

    @staticmethod
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

    @staticmethod
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
            
class Arrays:
    @staticmethod
    # Array section
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def minimumSwaps(arr):
        min_swaps = 0
        correct_index = 0
        # iterate through the array
        for i in range(len(arr)):
            # it is in the right place, thus continue
            if i + 1 == arr[i]:
                continue
            else:
                # when they are not equal
                while arr[i] != i + 1:
                    # the index that corresponds to the value arr[i] is:
                    correct_index = arr[i] - 1
                    # make the swap
                    arr[correct_index], arr[i] = arr[i], arr[correct_index]
                    min_swaps += 1
                    # now on the position i the value that was previously on position correct, is placed
                    # we continue swap until the chain of swaps initiated by i are resolved.

        return min_swaps

    @staticmethod
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
            
    @staticmethod
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

class Practice:
    @staticmethod
    def hasPathSumRec(root, targetSum):
        if not root:
            return False
        # we are in a leaf
        else:
            print(root.val, targetSum)
            if ((targetSum - root.val) != 0) and ((not root.left) and (not root.right)):
                return False
            elif ((targetSum - root.val) == 0) and ((not root.left) and (not root.right)):                  
                return True
            else:
                return hasPathSumRec(root.left, targetSum - root.val) or hasPathSumRec(root.right, targetSum - root.val)

    @staticmethod
    # Practice Section
    def compareTriplets(a, b):
        scores = 2 * [0]
        tasks_n = len(a)
        for i in range(tasks_n):
            if a[i] > b[i]:
                scores[0] += 1
            elif a[i] < b[i]:
                scores[1] += 1
        return scores     

    @staticmethod
    def checkIfExist(arr) -> bool:
        mults = []
        zeros = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0 or arr[i] != 0:
                mults.append(arr[i] // 2) 
            elif arr[i] == 0:
                zeros += 1
        idxs = list(filter(lambda x: x in mults, arr))
        if zeros > 1:
            return True
        if idxs:
            return True
        else:
            return False

    @staticmethod
    def validMountainArray(arr) -> bool:
        peak = False
        if len(arr) > 2:
            i = 0
            while i < len(arr) - 1:
                if arr[i] == arr[i + 1]:
                    return False
                if (arr[i] > arr[i + 1]) and (peak == False):
                    if i > 0:
                        peak = True
                    else:
                        return False
                if arr[i] < arr[i + 1] and peak == True:
                    return False
                i += 1
            return (True and peak)
            
    # Hit runtime error in some test cases
    # this is anticipated since for very large inputs 
    # the recursion is !forbided!
    @staticmethod
    def queensAttack(n, k, r_q, c_q, obstacles):
        visitedSquares = 0
        def moveSquares(n, k, i, j, obstacles):
            # check the bounds and the obstacles
            nonlocal visitedSquares
            if 0 >= i or n < i or 0 >= j or n < j: # out of bounds
                return 
            if [i, j] in obstacles:              # the current i,j pos is contained in obstacles
                return 
            # move to the board
            if i != r_q and j != c_q:            # we move  diagonally
                if i > r_q:
                    if j > c_q:                  # up right
                        visitedSquares += 1
                        moveSquares(n, k, i + 1, j + 1, obstacles) 
                    else:           
                        visitedSquares += 1             # down right
                        moveSquares(n, k, i + 1, j - 1, obstacles) 
                else:
                    if j > c_q:                  # up left
                        visitedSquares += 1
                        moveSquares(n, k, i, j + 1, obstacles) 
                    else:                        # down lrft
                        visitedSquares += 1
                        moveSquares(n, k, i, j - 1, obstacles) 
            if i == r_q:                         # we move up/down
                if j > c_q:
                    visitedSquares += 1
                    moveSquares(n, k, i, j + 1, obstacles) 
                else:
                    visitedSquares += 1
                    moveSquares(n, k, i, j - 1, obstacles) 
    
            if j == c_q:                        # we move left/right
                if i > c_q:
                    visitedSquares += 1
                    moveSquares(n, k, i + 1, j, obstacles) 
                else:
                    visitedSquares += 1
                    moveSquares(n, k, i - 1, j, obstacles) 
            return 
                                    
        moveSquares(n, k, r_q + 1, c_q, obstacles)
        moveSquares(n, k, r_q - 1, c_q, obstacles)
        moveSquares(n, k, r_q, c_q + 1, obstacles)
        moveSquares(n, k, r_q, c_q - 1, obstacles)
        moveSquares(n, k, r_q + 1, c_q + 1, obstacles)
        moveSquares(n, k, r_q + 1, c_q - 1, obstacles)
        moveSquares(n, k, r_q - 1, c_q + 1, obstacles)
        moveSquares(n, k, r_q - 1, c_q - 1, obstacles)
        
        return visitedSquares

    @staticmethod
    def queensAttack_brute(n, k, r_q, c_q, obstacles):   
        # limits
        up = n - r_q
        down = r_q - 1
        left = c_q - 1
        right = n - c_q
        up_right = min(up, right)   # the minimum of the distances that we are going
        down_right = min(down, right)
        up_left = min(up, left)
        down_left = min(down, left)

        for i_ob, j_ob in obstacles:
            if r_q == i_ob:
                if j_ob < c_q:
                    if c_q - j_ob - 1 < left:
                        left = c_q - j_ob -1
                else:
                    if j_ob - c_q - 1 < right:
                        right = j_ob - 1 - c_q

            elif c_q == j_ob:
                if i_ob < r_q:
                    if r_q - i_ob - 1 < down:
                        down = r_q - i_ob -1
                else:
                    if i_ob - r_q - 1 < up:
                        up = i_ob - 1 - r_q
            # up right
            elif i_ob > r_q and j_ob > c_q:
                if i_ob - r_q == j_ob - c_q:
                    if i_ob - r_q - 1 < up_right:
                        up_right = i_ob - r_q - 1

            # up left
            elif i_ob > r_q and j_ob < c_q:
                if i_ob - r_q == c_q - j_ob:
                    if i_ob - r_q - 1 < up_left:
                        up_left = i_ob - r_q - 1

            # down right
            elif i_ob < r_q and j_ob > c_q:
                if r_q - i_ob == j_ob - c_q:
                    if r_q - i_ob - 1 < down_right:
                        down_right = r_q - i_ob - 1

            # down left
            elif i_ob < r_q and j_ob < c_q:
                if r_q - i_ob ==  c_q - j_ob:
                    if r_q - i_ob - 1 < down_left:
                        down_left = r_q - i_ob - 1
                        
        visitedSquares = up + down + left + right + up_right + up_left + down_left + down_right
        return visitedSquares

    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x >= 0:
            quot = x
            remainder = x
            x_str = str(x)
            rev_str = ""
            i = 0
            while quot >= 1:
                quot, remainder = (quot // 10, quot % 10)
                # create the revrese number
                rev_str += str(remainder)
                # check i
                if rev_str[i] != x_str[i]:
                    return False
                i += 1
            return True
        else:
            return False
    
    @staticmethod
    def isPalindrome2(x: int) -> bool:
        stack_x = list(str(x))
        for c in x:
            if c != stack_x.pop():
                return False
            return True
    @staticmethod
    def isPalindrome3(x: int) -> bool:
        return x ==  reversed(str(x))

    @staticmethod
    def invertTree(self, root: TreeNode) -> TreeNode:
    
        def dfs(root):
            # post order
            if not root:
                return
            else:
                
                dfs(root.left)
                
                dfs(root.right)
                
                temp = root.left
                root.left = root.right
                root.right = temp
            
        dfs(root)
        return root

# the commplexity is on the getMin() method		
class MinStack:
    import sys
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        if self.data:
            self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        minVal =  sys.maxsize
        queue = self.data.copy()
        while queue:
            minVal = min(queue.pop(), minVal)
        return minVal

class MinStack:
    import sys

    def __init__(self):

	    self.data = []
	    self.minValue = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minValue or val <= self.minValue[-1]:
            self.minValue.append(val)
            

    def pop(self) -> None:
        if self.data:
            if self.data.pop() == self.minValue[-1]:
                self.minValue.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        print(self.minValue)

def isValidBST(self, root: TreeNode) -> bool:
    # we will traverse the tree in order 
    res  = []

    def inOrder(root):

        if not root:
            return 
        
        inOrder(root.left)
        res.append(root.val)
        inOrder(root.right)
        
    inOrder(root)
    
    for i in range(len(res) - 1):
        if res[i] >= res[i + 1]:
            return False
    return True


def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
    def search_BinaryTree(root, val):
        if root:
            if root.val == val:
                return root
            elif root.val > val:
                # go left
                return search_BinaryTree(root.left, val) 
            else:
                # go right
                return search_BinaryTree(root.right, val)
        else:
            return None
    if root:
        root = search_BinaryTree(root, val)
    return root        
            
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # watch out, python  user defined objects are mutable
    if head:
        curr, next = head, head.next
        curr.next = None                 # head shows to None

        while next:
            tmp = next.next              # save next.next(val, pointer) to tmp in order to keep the list
            next.next = curr             # now the pointer that points to next should now to point to curr
            curr = next                  # to iterate to the next node
            next = tmp                   # and now next shows to the next.next node

        return curr   

def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next or not head.next.next: # empty list,list with one element, two elements
        return False
    else:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

def plusOne(self, digits: List[int]) -> List[int]:
    arr2str = ""
    for d in digits:
        arr2str += str(d)
        
    tmp = int(arr2str) + 1
    
    str2arr = str(tmp)
    digits2 = []
    for c in str2arr:
        digits2.append(int(c))
        
    return digits2
    
def strStr(self, haystack: str, needle: str) -> int:
    if needle:
        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if needle == haystack[i:i+l]: # to check the whole word
                    return i
    return -1

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = head
    while node:
        if node.next is None:
            break
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
    return head
    
#---------------  Testing -----------------
def mainWarmUp():
    # Warm up
    steps = WarmUp.jumping_on_clouds([0,0,1,0,0,1,0])
    print(steps)
    alphas = WarmUp.repeatedString('aba', 10)
    print(alphas)

def mainArrays():
    # Array Section
    arr = [[1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]]

    max_sum = Arrays.hourglassSum(arr)
    print(max_sum)

    # a = [1, 2, 3, 4, 5]
    # a = rotLeft(a, 4)
    # print(a)

    a_2 = [1, 2, 3, 4, 5]
    a_2 = Arrays.rotLeft2(a_2, 4)
    print(a_2)

    q = [2, 1, 5, 3, 4]
    Arrays.minimumBribes(q)

    q = [2, 5, 1, 3, 4]
    Arrays.minimumBribes(q)

    q = [1, 2, 5, 3, 4, 7, 8, 6]
    Arrays.minimumBribes(q)

    q = [5, 1, 2, 3, 7, 8, 6, 4]
    Arrays.minimumBribes(q)

    q = [1, 2, 5, 3, 7, 8, 6, 4]
    Arrays.minimumBribes(q)

    arr = [4, 3, 1, 2]
    min_swaps = Arrays.minimumSwaps(arr)
    print(min_swaps)

def mainPractice():
    alice = [5, 6, 7]
    bob = [3, 6, 10]
    scores = Practice.compareTriplets(alice, bob)
    print(scores)

    result = Practice.checkIfExist([0, 0])
    print(result)

    result = Practice.validMountainArray([9,8,7,6,5,4,3,2,1,0])
    print(result)

if __name__ == '__main__':
    # mainWarmUp()
    # mainArrays()
    mainPractice()